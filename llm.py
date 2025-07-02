from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

from classes.Sections import Sections

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.1)

planner = llm.with_structured_output(Sections)