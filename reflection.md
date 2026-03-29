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
        3. Build a schedule based on these requirements - be able to assign order of the tasks, sort/filter tasks by priorities and duration so they fit within the owner's schedule
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

- Did your design change during implementation? If yes, describe at least one change and why you made it.
    - Yes, the design changed during the review of the skeleton. Originally, Scheduler took both an Owner and a Pet as separate parameters, but since Owner already holds a reference to their Pet, passing Pet again was redundant. The fix was to have Scheduler only take Owner, then derive the pet from owner.pet internally. This made the relationship cleaner and more consistent with how the classes are actually connected.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
    - The scheduler considers two main constraints: time and priority. Time is the core limit as the owner only has a fixed number of minutes available in a day, so tasks that push past that budget get skipped. Priority acts as the sorting rule that decides which tasks get those minutes first. High-priority tasks (like feeding or medication) are always scheduled before medium or low ones.
    - When thinking about conflict detection specifically, there is also an implicit ordering constraint as no two tasks can overlap in time. The original detect_conflicts approach used a nested loop to check every possible pair of tasks, which runs in O(n²) time. But because build_schedule already places tasks in strict time order, a single linear scan is enough: you only need to check if each task starts before the previous one finishes. This cuts the work down to O(n) and matches how the schedule is actually built.

- How did you decide which constraints mattered most?
    - Priority was chosen as the most important constraint because it directly reflects a pet's health needs. For example, a missed feeding matters more than a missed grooming session. Time was treated as a hard cap rather than something to negotiate around, since the owner's availability is fixed. Ordering and conflict detection were considered secondary because the build process already guarantees a conflict-free sequence, making the nested loop unnecessary for normal use.

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
