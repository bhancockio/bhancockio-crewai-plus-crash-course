import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from email_automation.tools.send_email_tool import SendEmailTool
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from email_automation.models.email_content import EmailContent


@CrewBase
class EmailAutomationCrew():
    """EmailAutomation crew"""
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self):
        self.manager_llm = ChatOpenAI()
        self.llm = ChatGroq(
            api_key=os.getenv("GROQ_API_KEY"),
            model="mixtral-8x7b-32768"
        )

    def send_email(self, task_output):
        print("Email output:", task_output.raw_output)

    @agent
    def coordination_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['coordination_agent'],
            allow_delegation=True,
            verbose=True
        )

    @agent
    def notes_analyzer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['notes_analyzer_agent'],
            verbose=True,
        )

    @agent
    def email_writer_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['email_writer_agent'],
            verbose=True
        )

    @agent
    def send_email_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['send_email_agent'],
            tools=[SendEmailTool()],
            verbose=True,
        )

    @task
    def coordination_task(self) -> Task:
        return Task(
            config=self.tasks_config['coordination_task'],
            agent=self.coordination_agent(),
        )

    @task
    def notes_analyzer_task(self) -> Task:
        return Task(
            config=self.tasks_config['notes_analyzer_task'],
            agent=self.notes_analyzer_agent(),
            output_file='notes.md'
        )

    @task
    def email_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['email_writing_task'],
            agent=self.email_writer_agent(),
            callback=self.send_email,
            output_pydantic=EmailContent
        )

    @task
    def send_email_task(self) -> Task:
        return Task(
            config=self.tasks_config['send_email_task'],
            agent=self.notes_analyzer_agent(),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the EmailAutomation crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=2,
        )
