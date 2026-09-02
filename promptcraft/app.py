import streamlit as st

st.set_page_config(page_title="PromptCraft", page_icon="🤖")

st.title("🤖 PromptCraft")
st.write("Engineering Assistant")

st.sidebar.title("Modules")

module = st.sidebar.selectbox(
    "Select Module",
    [
        "Prompt Workbench",
        "Code Generation",
        "Debugging",
        "Requirement Documentation",
        "Prompt Strategy Evaluation"
    ]
)

if module == "Prompt Workbench":
    st.header("Prompt Engineering Workbench")

    task = st.text_area("Enter your task")

    strategy = st.selectbox(
        "Select Strategy",
        ["Zero-Shot", "Few-Shot", "Chain-of-Thought"]
    )

    if st.button("Generate"):
        if task:
            st.subheader("Prompt")
            st.code(f"You are a software engineer.\nTask: {task}")

            st.subheader("Response")
            st.write("Generated response from simulated LLM.")
        else:
            st.warning("Please enter a task.")


elif module == "Code Generation":
    st.header("Code Generation")

    task = st.text_area("Enter coding task")

    if st.button("Generate Code"):
        if task:
            st.subheader("Generated Code")

            if "email" in task.lower():
                st.code("""
import re

def validate_email(email):
    pattern = r'^[\\w.-]+@[\\w.-]+\\.\\w+$'
    return re.match(pattern, email) is not None

print(validate_email("student@example.com"))
""")
            elif "linked list" in task.lower():
                st.code("""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reverse(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous
""")
            else:
                st.code("""
def solve():
    print("Task completed")

solve()
""")
        else:
            st.warning("Please enter a coding task.")


elif module == "Debugging":
    st.header("🐞 Automated Debugging")

    task = st.text_area("Enter debugging problem")

    if st.button("Debug"):
        if task:
            st.subheader("Debugging Result")

            if "loop" in task.lower() or "index" in task.lower():
                st.write("Problem: Incorrect loop boundary.")
                st.code("""
numbers = [10, 20, 30]

for i in range(len(numbers)):
    print(numbers[i])
""")

            elif "variable" in task.lower() or "name" in task.lower():
                st.write("Problem: Incorrect variable name.")
                st.code("""
numbers = [10, 20, 30]

sum_value = sum(numbers)

print(sum_value)
""")

            else:
                st.write("No major error detected.")

        else:
            st.warning("Please enter a debugging problem.")


elif module == "Requirement Documentation":
    st.header("📄 Requirement-to-Documentation")

    task = st.text_area("Enter software requirement")

    if st.button("Generate Documentation"):
        if task:
            st.subheader("Generated Documentation")

            if "login" in task.lower():
                st.markdown("""
# Login System

## Functional Requirements

1. User registration
2. Username and password
3. Credential validation
4. Login authentication
5. Logout

## Security

- Protect passwords
- Reject invalid credentials
- Protect user information
""")

            elif "library" in task.lower():
                st.markdown("""
# Online Library Management System

## Features

- User registration
- User login
- Add books
- Search books
- Issue books
- Return books

## Functional Requirements

1. Users can register.
2. Users can search books.
3. Librarians can add books.
4. Users can issue books.
5. Users can return books.
""")

            else:
                st.markdown("""
# Software Requirement Document

## Functional Requirements

- User interaction
- Data processing
- System operations
- Error handling

## Non-Functional Requirements

- Security
- Reliability
- Performance
- Usability
""")

        else:
            st.warning("Please enter a requirement.")


elif module == "Prompt Strategy Evaluation":
    st.header("📊 Prompt Strategy Evaluation")

    data = {
        "Strategy": [
            "Zero-Shot",
            "Few-Shot",
            "Chain-of-Thought"
        ],
        "Quality Score": [3.0, 4.0, 4.5],
        "Latency": [0.20, 0.30, 0.40],
        "Token Usage": [45, 65, 85]
    }

    st.dataframe(data)

    st.subheader("Quality Comparison")

    st.bar_chart(
        {
            "Zero-Shot": 3.0,
            "Few-Shot": 4.0,
            "Chain-of-Thought": 4.5
        }
    )

    st.subheader("Latency Comparison")

    st.bar_chart(
        {
            "Zero-Shot": 0.20,
            "Few-Shot": 0.30,
            "Chain-of-Thought": 0.40
        }
    )

    st.subheader("Token Usage Comparison")

    st.bar_chart(
        {
            "Zero-Shot": 45,
            "Few-Shot": 65,
            "Chain-of-Thought": 85
        }
    )

st.divider()

st.caption("PromptCraft | Generative AI & Prompt Engineering")