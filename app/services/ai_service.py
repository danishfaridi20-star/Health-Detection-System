from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

def get_ai_response(disease):

    prompt = f"""
You are a friendly medical assistant.

Patient symptoms:
{symptoms}

Your job is to:

1. Predict the most likely disease.
2. Explain everything in very simple English.
3. Imagine you are explaining it to a beginner.
4. Keep every answer short and easy.
5. Do not use difficult medical words.
6. If you use a difficult word, explain it in simple language.

Return ONLY valid JSON.

Do not use markdown.
Do not use ```json.
Do not write anything before or after the JSON.

Return this exact JSON format:

{{
    "predicted_disease": "",
    "about": "",
    "symptoms": [],
    "causes": [],
    "precautions": [],
    "home_care": [],
    "doctor": "",
    "warning_signs": [],
    "disclaimer": ""
}}

Instructions:

predicted_disease:
- Write only the disease name.

about:
- Explain the disease in only 2 or 3 short sentences.

symptoms:
- Write only 5 common symptoms.

causes:
- Write only 8 simple causes.

precautions:
- Write only 5 simple precautions.

home_care:
- Write only 8 easy home care tips.

doctor:
- Mention only one doctor.

warning_signs:
- Write only 4 warning signs.

disclaimer:
- Write exactly:
"This information is AI-generated and is not a substitute for a doctor's advice."
"""

    response = client.chat.completions.create(
        model="nvidia/nemotron-3-ultra-550b-a55b:free",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful AI medical assistant."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2
    )
    if not response.choices:
       return "{}"

    return response.choices[0].message.content.strip()
