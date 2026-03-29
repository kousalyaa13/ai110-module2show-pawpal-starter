# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
    - My initial UML design was based on the classes I decided to make. I designed the system with four main classes: Pet, Owner, Task, and Scheduler. The Pet class stores basic information about the animal, such as its name, species, and age. The Owner class stores details about the person, including their name and how much time they have each day to take care of their pet. The Owner is also connected to one Pet, showing that each owner is responsible for a specific animal. The Task class represents different care activities, such as feeding or walking, and includes details like the task name, how long it takes, and its priority level.
    - The Scheduler is the main part of the system where all the logic happens. It takes information from the Owner, the Pet, and a list of Tasks to create a daily care plan. The Scheduler decides which tasks should be included based on the owner’s available time and the priority of each task. It also explains why certain tasks were included or skipped. While the Pet, Owner, and Task classes are mainly used to store data, the Scheduler is responsible for making decisions and organizing everything into a useful plan.

- What classes did you include, and what responsibilities did you assign to each?
    - Three core actions the user should be able to perform are:
        1. Manage pet and owner data - Store owner's and pet info
        2. Manage tasks - add a list of tasks for the owner to choose from, add remove and editing a task functionality, show list of tasks
        3. Build a schedule based on these requirements - be able to assign order of the tasks, sort/filter tasks by prorities and duration so they fit within the owner's schedule
    - The classes I included were:
        1. Pet 
            Attributes: name, species, age
            Actions: Represents the animal being cared for
        2. Owner
            Attributes: name, available_minutes
            Actions: Know the owner of the pet
        3. Task
            Attributes: title, duration_minutes, priority
            Actions: Represents one care activity
        4. Scheduler
            Attributes: owner, pet, tasks
            Methods: build_schedule() - builds schedule, explain_plan() - explains what was skipped/included in the schedule

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
