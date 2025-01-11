from django.shortcuts import render
from langchain_google_genai import GoogleGenerativeAI
api_key = "AIzaSyAXFegUiKBMNnvXiCsVu26QHCeYzOyFT00"
# Create your views here.

class app_chat:
    def get_answer(self, prompt):
        llm = GoogleGenerativeAI(
            model='models/gemini-1.5-flash',
            temperature=0,
            max_tokens = 4000,
            timeout=None,
            max_retries=2,
            google_api_key=api_key
        )

        
        result = llm.invoke( prompt + " <Please Give result in proper html code.>"  )
        print(prompt, result)
        return result
    