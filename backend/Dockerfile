# Use the official Python image from the Docker Hub
FROM python:3.9-slim

WORKDIR /code

COPY ./backend/ /code/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]