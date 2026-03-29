from pawpal_system import Pet, Owner, Task, Scheduler


def print_schedule(scheduler: Scheduler) -> None:
    scheduler.build_schedule()
    lines = scheduler.explain_plan()
    print("\n" + "=" * 50)
    print("TODAY'S SCHEDULE")
    print("=" * 50)
    for line in lines:
        print(line)
    print("=" * 50)


# --- Pets ---
mochi = Pet(name="Mochi", species="dog", age=3)
luna = Pet(name="Luna", species="cat", age=5)

# --- Owners ---
jordan = Owner(name="Jordan", available_minutes=90, pet=mochi)
alex = Owner(name="Alex", available_minutes=60, pet=luna)

# --- Mochi's tasks ---
mochi_scheduler = Scheduler(owner=jordan)
mochi_scheduler.add_task(Task(title="Morning walk", duration_minutes=30, priority="high"))
mochi_scheduler.add_task(Task(title="Breakfast feeding", duration_minutes=10, priority="high"))
mochi_scheduler.add_task(Task(title="Flea medication", duration_minutes=5, priority="medium"))
mochi_scheduler.add_task(Task(title="Fetch / playtime", duration_minutes=40, priority="low"))
mochi_scheduler.add_task(Task(title="Bath", duration_minutes=45, priority="low"))

# --- Luna's tasks ---
luna_scheduler = Scheduler(owner=alex)
luna_scheduler.add_task(Task(title="Breakfast feeding", duration_minutes=10, priority="high"))
luna_scheduler.add_task(Task(title="Litter box cleaning", duration_minutes=10, priority="high"))
luna_scheduler.add_task(Task(title="Brush / grooming", duration_minutes=15, priority="medium"))
luna_scheduler.add_task(Task(title="Laser pointer play", duration_minutes=20, priority="low"))
luna_scheduler.add_task(Task(title="Vet checkup prep", duration_minutes=30, priority="medium"))

# --- Print schedules ---
print_schedule(mochi_scheduler)
print_schedule(luna_scheduler)
