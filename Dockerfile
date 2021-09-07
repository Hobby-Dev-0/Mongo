FROM python:3.9-slim-buster
COPY . .
COPY bot.py .
CMD ["python3", "-m", "bot"]
