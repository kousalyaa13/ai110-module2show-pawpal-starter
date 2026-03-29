import streamlit as st
from pawpal_system import Pet, Owner, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.divider()

# --- Owner & Pet setup ---
st.subheader("Owner & Pet Info")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
available_minutes = st.number_input(
    "Available time today (minutes)", min_value=10, max_value=480, value=90
)

# Build or rebuild the Scheduler when owner/pet info changes
if (
    "scheduler" not in st.session_state
    or st.session_state.get("owner_name") != owner_name
    or st.session_state.get("pet_name") != pet_name
    or st.session_state.get("species") != species
    or st.session_state.get("available_minutes") != available_minutes
):
    pet = Pet(name=pet_name, species=species, age=1)
    owner = Owner(name=owner_name, available_minutes=int(available_minutes), pet=pet)
    st.session_state.scheduler = Scheduler(owner=owner)
    st.session_state.owner_name = owner_name
    st.session_state.pet_name = pet_name
    st.session_state.species = species
    st.session_state.available_minutes = available_minutes

st.divider()

# --- Add tasks ---
st.subheader("Tasks")

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    task = Task(
        title=task_title,
        duration_minutes=int(duration),
        priority=priority,
    )
    st.session_state.scheduler.add_task(task)
    st.success(f"Added: {task_title}")

# Display current task pool
current_tasks = st.session_state.scheduler.tasks
if current_tasks:
    st.write("Current tasks:")
    st.table(
        [
            {
                "Title": t.title,
                "Duration (min)": t.duration_minutes,
                "Priority": t.priority,
            }
            for t in current_tasks
        ]
    )
else:
    st.info("No tasks yet. Add one above.")

st.divider()

# --- Generate schedule ---
st.subheader("Build Schedule")

if st.button("Generate schedule"):
    scheduler = st.session_state.scheduler
    if not scheduler.tasks:
        st.warning("Add at least one task before generating a schedule.")
    else:
        scheduler.build_schedule()
        explanation = scheduler.explain_plan()

        st.success("Schedule built!")

        if scheduler.scheduled_tasks:
            st.markdown("#### Scheduled")
            st.table(
                [
                    {
                        "Start time": t.start_time,
                        "Task": t.title,
                        "Duration (min)": t.duration_minutes,
                        "Priority": t.priority,
                    }
                    for t in scheduler.scheduled_tasks
                ]
            )

        if scheduler.skipped_tasks:
            st.markdown("#### Skipped (not enough time)")
            st.table(
                [
                    {
                        "Task": t.title,
                        "Duration (min)": t.duration_minutes,
                        "Priority": t.priority,
                    }
                    for t in scheduler.skipped_tasks
                ]
            )

        st.markdown("#### Plan explanation")
        for line in explanation:
            st.text(line)
