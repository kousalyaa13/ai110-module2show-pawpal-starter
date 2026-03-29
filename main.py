from pawpal_system import Pet, Owner, Task, Scheduler


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
        print(f"  [{time}] {t.title} | priority: {t.priority} | status: {status}")


# --- Pets & Owners ---
mochi = Pet(name="Mochi", species="dog", age=3)
luna = Pet(name="Luna", species="cat", age=5)

jordan = Owner(name="Jordan", available_minutes=90, pet=mochi)
alex = Owner(name="Alex", available_minutes=60, pet=luna)

# --- Mochi's tasks added OUT OF ORDER (low priority first) ---
mochi_scheduler = Scheduler(owner=jordan)
mochi_scheduler.add_task(Task(title="Bath", duration_minutes=45, priority="low"))
mochi_scheduler.add_task(Task(title="Fetch / playtime", duration_minutes=40, priority="low"))
mochi_scheduler.add_task(Task(title="Flea medication", duration_minutes=5, priority="medium"))
mochi_scheduler.add_task(Task(title="Breakfast feeding", duration_minutes=10, priority="high"))
mochi_scheduler.add_task(Task(title="Morning walk", duration_minutes=30, priority="high"))

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
