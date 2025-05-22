# 이미지 생성 서비스 프로세스
# 1. User Prompt
# 2. LLM -> User Prompt 확장
# 3. LLM -> 확장 Prompt 번역(영어)
# 4. DALL-E-3 -> 이미지 생성


import os
from dotenv import find_dotenv, load_dotenv
from langchain_openai import ChatOpenAI


# 1. .env 불러오기
_ = load_dotenv(find_dotenv())

# 2. LLM 모델 생성
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    openai_api_key=os.getenv("OPENAI_API_KEY"),
)

#