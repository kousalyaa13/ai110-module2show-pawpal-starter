import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from pawpal_system import Pet, Owner, Task, Scheduler


def test_mark_complete_changes_status():
    """Task.completed should be False by default and True after mark_complete()."""
    task = Task(title="Morning walk", duration_minutes=30, priority="high")

    assert task.completed is False
    task.mark_complete()
    assert task.completed is True


def test_add_task_increases_count():
    """Scheduler.add_task() should increase the number of tasks tracked for a pet."""
    pet = Pet(name="Mochi", species="dog", age=3)
    owner = Owner(name="Jordan", available_minutes=90, pet=pet)
    scheduler = Scheduler(owner=owner)

    assert len(scheduler.tasks) == 0

    scheduler.add_task(Task(title="Feeding", duration_minutes=10, priority="high"))
    assert len(scheduler.tasks) == 1

    scheduler.add_task(Task(title="Walk", duration_minutes=20, priority="medium"))
    assert len(scheduler.tasks) == 2
