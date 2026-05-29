from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model='gpt-4o-mini', # 사용할 LLM 모델명
    temperature=0.1, # 무작위성 - 0에 가까울수록 일관된 답변, 1에 가까울수록 창의적이다.
    messages=[
        {'role':'system','content':'You are a helphul assistant.'},
        {'role':'user', 'content':'2022년 월트컵 우승팀은 어디야?'}
    ]
)
# print(response)
print(response.choices[0].message.content)