import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from app.ai.prompts import BASE_SUMMARY_PROMPT

load_dotenv()  # ✅ this loads OPENAI_API_KEY

def format_messages(thread):
    return "\n".join([f"{m['author']}: {m['content']}" for m in thread])

def generate_summary(thread):
    messages_text = format_messages([m.dict() for m in thread])
    prompt = ChatPromptTemplate.from_template(BASE_SUMMARY_PROMPT)
    chain = prompt | ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
    return chain.invoke({"messages": messages_text})
