from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from fastapi import FastAPI
from dotenv import load_dotenv
from schemas.schemas import UserProfile

load_dotenv()

app = FastAPI()

model = ChatOpenAI()


@app.post("/write-emails")
async def write_emails(user_profile: UserProfile):
    """Write a partial to a customer about an activity"""
    prompt = ChatPromptTemplate.from_template(
        "write an intro paragrapgh of an email to customer {name} about {activity}. Keep it short and under 200 words"
    )
    chain = prompt | model
    return chain.invoke({"name": user_profile.name, "activity": user_profile.activity})


@app.post("/write-full-emails")
async def write_full_emails(user_profile: UserProfile):
    """Write a full email to a customer about an activity"""
    prompt = ChatPromptTemplate.from_template(
        "Write a full email to customer {name} about their recent LinkedIn activity: {activity}. "
        "The email should be friendly, personalized, and mention how their activity relates to their role as a {job_title} at {company}. "
        "Include an intro, 2-3 body paragraphs, and a brief closing. Keep the total length under 400 words."
    )
    chain = prompt | model
    return chain.invoke(
        {
            "name": user_profile.name,
            "activity": user_profile.activity,
            "job_title": user_profile.job_title,
            "company": user_profile.company,
        }
    )


@app.post("/subject-line")
async def subject_line(user_profile: UserProfile):
    """Write a subject line for an email to a customer about an activity"""
    prompt = ChatPromptTemplate.from_template(
        "Write a subject line for an email to customer {name} about their recent LinkedIn activity: {activity}. "
        "The subject line should be engaging, personalized, and mention how their activity relates to their role as a {job_title} at {company}. "
        "Keep the total length under 100 characters."
    )
    chain = prompt | model
    return chain.invoke(
        {
            "name": user_profile.name,
            "activity": user_profile.activity,
            "job_title": user_profile.job_title,
            "company": user_profile.company,
        }
    )
