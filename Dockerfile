FROM python:3.9-slim-buster
COPY . .
RUN pip3 install -r requirements.txt
COPY bot.py .
CMD ["python3", "-m", "udb"]
