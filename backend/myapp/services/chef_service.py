from openai import OpenAI
import instructor
from pydantic import BaseModel, Field
from typing import List
from django.conf import settings


class Recipe(BaseModel):
    ingredients: List[str] = Field(default_factory=list)
    instructions: List[str] = Field(default_factory=list)
    grams_per_ingredient: List[int] = Field(default_factory=list, description="Numbered list of the amount of grams for every value in the ingredients list",)


class ChefGPT:

    def chef_gpt(self, dish):

        OpenAI.api_key = settings.OPENAI_API_KEY

        client = instructor.from_openai(OpenAI())

        messages=[
            {"role": "system", "content": "You are a Certified Master Chef. Please generate exciting recipes for every dish I request."},
            {"role": "user", "content": f"Please generate me a recipe for {dish}"}
        ]

        recipe = client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_model=Recipe,
            messages=messages,
        )

        return recipe