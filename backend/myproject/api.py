from ninja import NinjaAPI
from myapp.services.openai_service import ChatGPT
from myapp.services.chef_service import ChefGPT
from myapp.services.parts_service import PartsService

from typing import List

api = NinjaAPI()

@api.get("/hello")
def hello(request):
    return "Hello world"

@api.post("/openai")
def openai(request, user_messages: List[str], ai_messages: List[str]):
    service = ChatGPT()
    response = service.squidward(user_messages, ai_messages)
    return response

@api.post("/chefy")
def chefy(request, dish: str):
    service = ChefGPT()
    response = service.chef_gpt(dish)
    return response

@api.get("/parts")
def parts(request, keyword: str, manufacturer: str):
    service = PartsService()
    response = service.get_parts(keyword, manufacturer)
    return response

@api.get("/parse")
def parse(request, text: str):
    service = PartsService()
    response = service.parse_keywords_ai(text)
    return response

@api.get("/manufacturer")
def manufacturer(request, text: str):
    service = PartsService()
    response = service.get_manufacturer(text)
    return response