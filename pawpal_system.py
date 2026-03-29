PRIORITY_RANK = {"high": 3, "medium": 2, "low": 1}


class Pet:
    def __init__(self, name: str, species: str, age: int):
        self.name = name
        self.species = species
        self.age = age


class Owner:
    def __init__(self, name: str, available_minutes: int, pet: Pet):
        self.name = name
        self.available_minutes = available_minutes
        self.pet = pet


class Task:
    def __init__(self, title: str, duration_minutes: int, priority: str):
        self.title = title
        self.duration_minutes = duration_minutes
        self.priority = priority  # "low", "medium", or "high"
        self.start_time: str | None = None  # e.g. "9:00 AM", set by Scheduler


class Scheduler:
    def __init__(self, owner: Owner):
        self.owner = owner
        self.pet = owner.pet  # derived from owner, not passed separately
        self.tasks: list[Task] = []
        self.scheduled_tasks: list[Task] = []
        self.skipped_tasks: list[Task] = []

    def add_task(self, task: Task) -> None:
        pass

    def build_schedule(self) -> list[Task]:
        pass

    def explain_plan(self) -> list[str]:
        pass
