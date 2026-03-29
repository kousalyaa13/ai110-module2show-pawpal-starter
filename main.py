from pawpal_system import Pet, Owner, Task, Scheduler, find_cross_scheduler_conflicts


def print_section(title: str) -> None:
    print("\n" + "-" * 50)
    print(f"  {title}")
    print("-" * 50)


def print_tasks(tasks: list) -> None:
    if not tasks:
        print("  (none)")
    for t in tasks:
        status = "DONE" if t.completed else "pending"
        time = t.start_time if t.start_time else "unscheduled"
        recur = f" | recurs: {t.recurrence}" if t.recurrence else ""
        print(f"  [{time}] {t.title} | priority: {t.priority} | status: {status}{recur}")


# --- Pets & Owners ---
mochi = Pet(name="Mochi", species="dog", age=3)
luna = Pet(name="Luna", species="cat", age=5)

jordan = Owner(name="Jordan", available_minutes=90, pet=mochi)
alex = Owner(name="Alex", available_minutes=60, pet=luna)

# --- Mochi's tasks added OUT OF ORDER (low priority first) ---
mochi_scheduler = Scheduler(owner=jordan)
mochi_scheduler.add_task(Task(title="Bath", duration_minutes=45, priority="low"))
mochi_scheduler.add_task(Task(title="Fetch / playtime", duration_minutes=40, priority="low"))
mochi_scheduler.add_task(Task(title="Flea medication", duration_minutes=5, priority="medium", recurrence="weekly"))
mochi_scheduler.add_task(Task(title="Breakfast feeding", duration_minutes=10, priority="high", recurrence="daily"))
mochi_scheduler.add_task(Task(title="Morning walk", duration_minutes=30, priority="high", recurrence="daily"))

# --- Luna's tasks added OUT OF ORDER (low priority first) ---
luna_scheduler = Scheduler(owner=alex)
luna_scheduler.add_task(Task(title="Laser pointer play", duration_minutes=20, priority="low"))
luna_scheduler.add_task(Task(title="Vet checkup prep", duration_minutes=30, priority="medium"))
luna_scheduler.add_task(Task(title="Brush / grooming", duration_minutes=15, priority="medium"))
luna_scheduler.add_task(Task(title="Litter box cleaning", duration_minutes=10, priority="high"))
luna_scheduler.add_task(Task(title="Breakfast feeding", duration_minutes=10, priority="high"))

# --- Build schedules ---
mochi_scheduler.build_schedule()
luna_scheduler.build_schedule()

# --- Mark some tasks complete to test filtering ---
mochi_scheduler.scheduled_tasks[0].mark_complete()
mochi_scheduler.scheduled_tasks[1].mark_complete()
luna_scheduler.scheduled_tasks[0].mark_complete()

# ============================================================
# sort_by_time()
# ============================================================
print("\n" + "=" * 50)
print("  SORTED BY START TIME")
print("=" * 50)

print_section("Mochi's schedule (sorted by time)")
print_tasks(mochi_scheduler.sort_by_time())

print_section("Luna's schedule (sorted by time)")
print_tasks(luna_scheduler.sort_by_time())

# ============================================================
# filter_by_completion()
# ============================================================
print("\n" + "=" * 50)
print("  FILTER BY COMPLETION STATUS")
print("=" * 50)

print_section("Mochi — completed tasks")
print_tasks(mochi_scheduler.filter_by_completion(completed=True))

print_section("Mochi — pending tasks")
print_tasks(mochi_scheduler.filter_by_completion(completed=False))

print_section("Luna — completed tasks")
print_tasks(luna_scheduler.filter_by_completion(completed=True))

print_section("Luna — pending tasks")
print_tasks(luna_scheduler.filter_by_completion(completed=False))

# ============================================================
# filter_by_pet()
# ============================================================
print("\n" + "=" * 50)
print("  FILTER BY PET NAME")
print("=" * 50)

print_section("filter_by_pet('Mochi') on mochi_scheduler")
print_tasks(mochi_scheduler.filter_by_pet("Mochi"))

print_section("filter_by_pet('Luna') on mochi_scheduler (expect none)")
print_tasks(mochi_scheduler.filter_by_pet("Luna"))

print_section("filter_by_pet('Luna') on luna_scheduler")
print_tasks(luna_scheduler.filter_by_pet("Luna"))

# ============================================================
# complete_task() — recurrence demo
# ============================================================
print("\n" + "=" * 50)
print("  RECURRENCE — complete_task() DEMO")
print("=" * 50)

walk = mochi_scheduler.scheduled_tasks[1]   # Morning walk (daily)
flea = mochi_scheduler.scheduled_tasks[2]   # Flea medication (weekly)
bath = next(t for t in mochi_scheduler.tasks if t.title == "Bath")  # no recurrence

print(f"\nTask pool size before completing tasks: {len(mochi_scheduler.tasks)}")

print_section(f"Completing '{walk.title}' (recurrence: {walk.recurrence})")
next_walk = mochi_scheduler.complete_task(walk)
print(f"  next_occurrence returned: {next_walk}")
print(f"  Task pool size after: {len(mochi_scheduler.tasks)} (expected +1)")

print_section(f"Completing '{flea.title}' (recurrence: {flea.recurrence})")
next_flea = mochi_scheduler.complete_task(flea)
print(f"  next_occurrence returned: {next_flea}")
print(f"  Task pool size after: {len(mochi_scheduler.tasks)} (expected +1)")

print_section(f"Completing '{bath.title}' (recurrence: {bath.recurrence})")
next_bath = mochi_scheduler.complete_task(bath)
print(f"  next_occurrence returned: {next_bath} (expected None)")
print(f"  Task pool size after: {len(mochi_scheduler.tasks)} (expected no change)")

print_section("Full task pool after completions")
print_tasks(mochi_scheduler.tasks)

# ============================================================
# conflict detection demo
# ============================================================
print("\n" + "=" * 50)
print("  CONFLICT DETECTION DEMO")
print("=" * 50)

# Build a fresh scheduler with two tasks that manually share the same start time
conflict_pet = Pet(name="Biscuit", species="dog", age=2)
conflict_owner = Owner(name="Sam", available_minutes=120, pet=conflict_pet)
conflict_scheduler = Scheduler(owner=conflict_owner)

task_a = Task(title="Morning walk", duration_minutes=30, priority="high")
task_b = Task(title="Vet visit", duration_minutes=60, priority="high")
task_a.start_time = "8:00 AM"   # forced overlap: both start at 8:00 AM
task_b.start_time = "8:15 AM"   # starts before walk ends (8:30 AM)
conflict_scheduler.scheduled_tasks = [task_a, task_b]

print_section("Same-pet conflict (detect_conflicts)")
warnings = conflict_scheduler.detect_conflicts()
if warnings:
    for w in warnings:
        print(f"  {w}")
else:
    print("  No conflicts found.")

# Cross-scheduler: mochi and luna both start at 8:00 AM → overlap expected
print_section("Cross-pet conflict (find_cross_scheduler_conflicts)")

# Rebuild fresh schedulers so start_times are clean
mochi2 = Pet(name="Mochi", species="dog", age=3)
luna2 = Pet(name="Luna", species="cat", age=5)
s1 = Scheduler(owner=Owner(name="Jordan", available_minutes=60, pet=mochi2))
s2 = Scheduler(owner=Owner(name="Alex", available_minutes=60, pet=luna2))

s1.add_task(Task(title="Morning walk", duration_minutes=30, priority="high"))
s1.add_task(Task(title="Breakfast feeding", duration_minutes=15, priority="medium"))
s2.add_task(Task(title="Litter box cleaning", duration_minutes=20, priority="high"))
s2.add_task(Task(title="Breakfast feeding", duration_minutes=15, priority="medium"))

s1.build_schedule()
s2.build_schedule()

cross_warnings = find_cross_scheduler_conflicts([s1, s2])
if cross_warnings:
    for w in cross_warnings:
        print(f"  {w}")
else:
    print("  No cross-pet conflicts found.")
