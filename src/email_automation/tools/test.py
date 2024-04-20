from typing import Type
from crewai_tools import BaseTool
from pydantic.v1 import BaseModel, Field, ValidationError
import smtplib
import os

import requests


class SendEmailInput(BaseModel):
    """Input model for SendEmailTool."""
    subject: str = Field(..., description="Subject line of the email.")
    body: str = Field(..., description="Body content of the email.")
    recipient_name: str = Field(...,
                                description="Name of the email recipient.")
    recipient_email: str = Field(...,
                                 description="Email address of the recipient.")


class SendEmailTool(BaseTool):
    name: str = "Send Email"
    description: str = "Sends an email to a specified recipient using the Mailtrap API."
    args_schema: Type[BaseModel] = SendEmailInput

    def _run(self, **kwargs) -> str:
        """Method to send an email using the Mailtrap API."""
        try:
            args = SendEmailInput(**kwargs)
        except ValidationError as e:
            return f"Validation Error: {str(e)}"

        api_url = "https://send.api.mailtrap.io/api/send"
        api_key = os.getenv("MAILTRAP_API_KEY",
                            "0e44f106cafb0ee32b9075ff3a0e03ed")
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "from": {
                "email": "mailtrap@demomailtrap.com",
                "name": "CrewAI Automation Bot"
            },
            "to": [{
                "email": "brandon@brandonhancock.io",
                "name": "Brandon Hancock"
            }],
            "subject": args.subject,
            "text": args.body,
            "category": "CrewAI"
        }

        try:
            response = requests.post(api_url, json=data, headers=headers)
            response.raise_for_status()  # Will raise an exception for HTTP error responses
            return "Email sent successfully."
        except requests.exceptions.RequestException as e:
            return f"Failed to send email: {str(e)}"
