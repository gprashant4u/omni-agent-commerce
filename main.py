from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4-turbo")

# Architect Role: Multi-agent orchestration patterns [cite: 27]
concierge = Agent(
    role='Architect - Agentic Commerce',
    goal='Design platform architecture and manage state',
    backstory='Expert in MCP architecture and grounding pipelines.',
    llm=llm
)

task = Task(
    description='Analyze commerce request: {user_input}',
    agent=concierge,
    expected_output='Architectural design for the request.'
)

crew = Crew(agents=[concierge], tasks=[task], verbose=True)
