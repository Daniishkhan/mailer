from pydantic import BaseModel


class UserProfile(BaseModel):
    name: str
    email: str
    job_title: str
    company: str
    activity: dict
