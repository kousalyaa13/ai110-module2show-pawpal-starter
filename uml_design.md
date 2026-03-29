# PawPal+ UML Design
---

```
classDiagram
    class Pet {
        +str name
        +str species
        +int age
    }

    class Owner {
        +str name
        +int available_minutes
        +Pet pet
    }

    class Task {
        +str title
        +int duration_minutes
        +str priority
    }

    class Scheduler {
        +Owner owner
        +Pet pet
        +list~Task~ tasks
        +add_task(task: Task) None
        +build_schedule() list~Task~
        +explain_plan() list~str~
    }

    Owner "1" --> "1" Pet : owns
    Scheduler --> Owner : uses
    Scheduler --> Pet : uses
    Scheduler "1" --> "many" Task : manages
```
