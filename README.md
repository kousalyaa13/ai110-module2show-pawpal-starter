# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Smarter Scheduling

Beyond the core daily planner, the following features were added to make the scheduler more realistic and robust.

**Task recurrence** — Tasks can be marked as `"daily"` or `"weekly"`. When `Scheduler.complete_task()` is called on a recurring task, a fresh copy is automatically added back to the task pool for the next occurrence. Non-recurring tasks are completed and removed with no side effects.

**Sorting by time** — `Scheduler.sort_by_time()` reorders the scheduled task list chronologically by start time. This is useful when start times are adjusted manually outside of `build_schedule()`.

**Filtering** — `Scheduler.filter_by_completion(completed)` returns all tasks that match a given completion status (`True` for done, `False` for pending). `Scheduler.filter_by_pet(pet_name)` returns the full task pool if the scheduler's pet matches the given name, or an empty list otherwise — useful when iterating across multiple schedulers.

**Conflict detection** — `Scheduler.detect_conflicts()` checks a single pet's scheduled tasks for time overlaps and returns human-readable warning strings without crashing. `find_cross_scheduler_conflicts(schedulers)` performs the same check across multiple schedulers, flagging cases where two pets would require the owner's attention at the same time.

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.
