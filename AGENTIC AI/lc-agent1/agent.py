import os
from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_groq import ChatGroq

# 1. Load environment variables
load_dotenv()

# 2. Initialize Groq LLM
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0
)

# 3. Create Calculator Tool
@tool
def calculator(a: float, b: float, operation: str) -> str:
    """Perform addition, subtraction, multiplication or division."""

    if operation == "add":
        return str(a + b)

    elif operation == "subtract":
        return str(a - b)

    elif operation == "multiply":
        return str(a * b)

    elif operation == "divide":
        if b == 0:
            return "Cannot divide by zero"
        return str(a / b)

    return "Unsupported operation"


# 4. Create Course Information Tool
@tool
def get_course_info(course_name: str) -> str:
    """Get information about Python and AI training courses."""

    courses = {
        "python": "Python covers programming, functions, OOP and APIs.",
        "generative ai": "Generative AI covers LLMs, prompting, RAG and AI agents.",
        "full stack": "Full Stack Development covers frontend, backend and databases."
    }

    return courses.get(
        course_name.lower(),
        "Course information is not available."
    )


# 5. Register tools
tools = [
    calculator,
    get_course_info
]

# 6. Create LangChain Agent
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="""
    You are a helpful AI Assistant.

    You can:
    1. Answer general questions.
    2. Use calculator for mathematical operations.
    3. Use get_course_info for course-related questions.

    Use tools whenever required.
    Explain answers in simple English.
    """
)

# 7. Start conversation
messages = []

print("Welcome to LangChain AI Agent!")
print("Type exit to stop.")

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        print("Agent: Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": question
    })

    response = agent.invoke({
        "messages": messages
    })

    messages = response["messages"]

    print("\nAI Agent:", messages[-1].content)