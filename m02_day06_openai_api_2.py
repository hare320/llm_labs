from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model='gpt-4o-mini', # 사용할 LLM 모델명
    temperature=0.9, # 무작위성 - 0에 가까울수록 일관된 답변, 1에 가까울수록 창의적이다.
    messages=[
        {'role':'system','content':'너는 백설공주 이야기 속의 거울이야. 그 이야기속의 마법 거울 캐릭터에 부합해서 답변해줘.'},
        {'role':'user', 'content':'현재 대한민국 여성 아이돌중 누가 제일 아름답니?'}
    ]
)
# print(response)
print(response.choices[0].message.content)