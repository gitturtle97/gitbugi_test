import os
import google.generativeai as genai
from dotenv import load_dotenv

# 1. 보안 키 로드
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# 2. 모델 설정 (성능 극대화의 핵심)
generation_config = {
    "temperature": 0.9,  # 창의성 조절 (0.0 ~ 1.0)
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
}

# 3. 시스템 프롬프트 (여기에 페르소나를 입력)
system_instruction = "당신은 세계 최고의 Python 코딩 전문가입니다. 간결하고 효율적인 코드만 작성합니다."

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", # 또는 gemini-1.5-pro
    generation_config=generation_config,
    system_instruction=system_instruction,
)

# 4. 실행
response = model.generate_content("피보나치 수열을 구하는 파이썬 함수를 짜줘.")
print(response.text)