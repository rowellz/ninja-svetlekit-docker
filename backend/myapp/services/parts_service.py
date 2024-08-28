from openai import OpenAI
import instructor
from pydantic import BaseModel, Field
from typing import List
from django.conf import settings

class PartsService:

    def parse_keywords_ai(self, text: str):

        OpenAI.api_key = settings.OPENAI_API_KEY

        client = instructor.from_openai(OpenAI())

        messages=[
            {"role": "system", "content": "Can you find the product and the manufacturer in this text?"},
            {"role": "user", "content": f"{text}"}
        ]

        data = client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_model=Recipe,
            messages=messages,
        )

        name = data.manufacturerName
        keyword = data.keyword
        
        return data