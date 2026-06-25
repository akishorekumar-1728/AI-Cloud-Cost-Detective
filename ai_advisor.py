import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

def generate_ai_insight(cost_data):

    try:

        genai.configure(api_key=api_key)

        model = genai.GenerativeModel("gemini-1.5-flash")

        prompt = f"""
        You are a Senior Azure FinOps Engineer.

        Analyze this Azure cloud cost data:

        {cost_data}

        Give:
        1. Cost Summary
        2. Risks
        3. Optimization Suggestions
        4. Estimated Savings
        """

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"AI Analysis unavailable: {e}"