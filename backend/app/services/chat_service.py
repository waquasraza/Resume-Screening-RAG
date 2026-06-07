from langchain_openai import ChatOpenAI
from app.core.config import OPENAI_API_KEY


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key=OPENAI_API_KEY,
    temperature=0
)


def generate_answer(question: str, docs):

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are an AI Resume Screening Assistant.

Answer ONLY using the resume information provided below.

If the information is not available in the resume,
say:
"I could not find this information in the resume."

Resume Context:
{context}

Question:
{question}

Provide:
1. Direct Answer
2. Supporting Evidence
"""

    response = llm.invoke(prompt)

    return response.content