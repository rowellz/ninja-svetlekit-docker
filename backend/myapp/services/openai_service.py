import openai
from django.conf import settings


class ChatGPT:
    def squidward(self, user_messages, ai_messages):
        openai.api_key = settings.OPENAI_API_KEY
        messages=[
            {"role": "system", "content": "You are now Squidward. When I ask you questions, respond as him in first person. You are allowed to curse, but please keep your responses some what short and witty."},
        ]
        for index, user_message in enumerate(user_messages):
            messages.append({"role": "user", "content": user_message})

            if index < len(ai_messages) and len(ai_messages[index]) > 0:
                messages.append({"role": "assistant", "content": ai_messages[index]})

        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )
        return completion.choices[0].message.content