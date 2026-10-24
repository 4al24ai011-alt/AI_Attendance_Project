
import streamlit as st

# Page settings
st.set_page_config(
    page_title="AI Attendance System",
    page_icon="🎓",
    layout="wide"
)

# Main heading
st.title("🎓 AI Attendance System")

st.write(
    "Welcome to the AI Camera Attendance "
    "and Student Attentiveness System."
)

# Dashboard section
st.header("Dashboard")

# Display three information cards
col1, col2, col3 = st.columns(3)

col1.metric("Total Students", 60)
col2.metric("Present Students", 52)
col3.metric("Absent Students", 8)

# Current class information
st.subheader("Current Class Details")

st.write(
    "Teacher:",
    st.session_state.get("teacher_name", "Not selected")
)

st.write(
    "Subject:",
    st.session_state.get("current_subject", "Not selected")
)

st.info(
    "Select a subject and manage your class "
    "using the Teacher & Subjects page."
)

# Teacher and Subject Management

teachers = {
    "Select Teacher": [],
    "nithin": [
        "Computer Vision",
        "Artificial Intelligence"
    ],
    "praveen": [
        "Computer Networks",
        "Database Management Systems"
    ],
    "Priya": [
        "Automata Theory"
    ]
}

st.header("👩‍🏫 Teacher & Subject Management")


teacher_name = st.selectbox(
    "Select Teacher",
    list(teachers.keys()),
    key="teacher_dropdown"
)

if teacher_name != "Select Teacher":
    selected_subject = st.selectbox(
        "Select Subject",
        teachers[teacher_name],
        key="subject_dropdown"
    )

    if st.button("Save Teacher & Subject"):
        st.session_state.teacher_name = teacher_name
        st.session_state.current_subject = selected_subject
        st.success(
            f"{teacher_name} selected {selected_subject} successfully!"
        )
else:
    st.info("Please select a teacher to view their subjects.")
