PRIORITY_RANK = {"high": 3, "medium": 2, "low": 1}
DAY_START_HOUR = 8  # schedule begins at 8:00 AM


def _minutes_to_time_str(minutes_from_midnight: int) -> str:
    """Convert total minutes from midnight to a readable time string."""
    hour = minutes_from_midnight // 60
    minute = minutes_from_midnight % 60
    period = "AM" if hour < 12 else "PM"
    display_hour = hour if hour <= 12 else hour - 12
    if display_hour == 0:
        display_hour = 12
    return f"{display_hour}:{minute:02d} {period}"


class Pet:
    def __init__(self, name: str, species: str, age: int):
        self.name = name
        self.species = species
        self.age = age

    def __repr__(self) -> str:
        return f"Pet(name={self.name!r}, species={self.species!r}, age={self.age})"


class Owner:
    def __init__(self, name: str, available_minutes: int, pet: Pet):
        self.name = name
        self.available_minutes = available_minutes
        self.pet = pet

    def __repr__(self) -> str:
        return (
            f"Owner(name={self.name!r}, "
            f"available_minutes={self.available_minutes}, "
            f"pet={self.pet.name!r})"
        )


class Task:
    def __init__(self, title: str, duration_minutes: int, priority: str):
        self.title = title
        self.duration_minutes = duration_minutes
        self.priority = priority  # "low", "medium", or "high"
        self.start_time: str | None = None  # assigned by Scheduler.build_schedule()
        self.completed: bool = False

    def mark_complete(self) -> None:
        """Mark this task as completed."""
        self.completed = True

    def __repr__(self) -> str:
        return (
            f"Task(title={self.title!r}, "
            f"duration={self.duration_minutes}min, "
            f"priority={self.priority!r})"
        )


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner
        self.pet = owner.pet  # derived from owner
        self.tasks: list[Task] = []
        self.scheduled_tasks: list[Task] = []
        self.skipped_tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        """Add a task to the pool of tasks to be scheduled."""
        self.tasks.append(task)

    def build_schedule(self) -> list[Task]:
        """
        Sort tasks by priority (high → low), then greedily fit them
        within the owner's available minutes. Assigns a start_time to
        each scheduled task. Populates scheduled_tasks and skipped_tasks.
        """
        self.scheduled_tasks = []
        self.skipped_tasks = []

        sorted_tasks = sorted(
            self.tasks,
            key=lambda t: PRIORITY_RANK.get(t.priority, 0),
            reverse=True,
        )

        time_used = 0
        current_minutes = DAY_START_HOUR * 60  # start at 8:00 AM in minutes

        for task in sorted_tasks:
            if time_used + task.duration_minutes <= self.owner.available_minutes:
                task.start_time = _minutes_to_time_str(current_minutes)
                current_minutes += task.duration_minutes
                time_used += task.duration_minutes
                self.scheduled_tasks.append(task)
            else:
                task.start_time = None
                self.skipped_tasks.append(task)

        return self.scheduled_tasks

    def explain_plan(self) -> list[str]:
        """
        Return a human-readable explanation for every scheduled and
        skipped task. Must be called after build_schedule().
        """
        if not self.scheduled_tasks and not self.skipped_tasks:
            return ["No schedule built yet. Call build_schedule() first."]

        explanations = []
        time_used = sum(t.duration_minutes for t in self.scheduled_tasks)

        explanations.append(
            f"Daily plan for {self.owner.name}'s pet {self.pet.name} "
            f"({self.pet.species}, age {self.pet.age}):"
        )
        explanations.append(
            f"Available time: {self.owner.available_minutes} min | "
            f"Scheduled: {time_used} min | "
            f"Remaining: {self.owner.available_minutes - time_used} min"
        )
        explanations.append("")

        if self.scheduled_tasks:
            explanations.append("Scheduled tasks:")
            for task in self.scheduled_tasks:
                explanations.append(
                    f"  - [{task.start_time}] {task.title} "
                    f"({task.duration_minutes} min, priority: {task.priority}) "
                    f"— included because it is {task.priority} priority and fits in the available time."
                )

        if self.skipped_tasks:
            explanations.append("")
            explanations.append("Skipped tasks:")
            for task in self.skipped_tasks:
                explanations.append(
                    f"  - {task.title} ({task.duration_minutes} min, priority: {task.priority}) "
                    f"— skipped because there was not enough remaining time."
                )

        return explanations
