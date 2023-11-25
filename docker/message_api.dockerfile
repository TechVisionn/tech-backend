FROM python:3.10.12-slim-buster

RUN apt-get update && apt-get install -y build-essential

WORKDIR /tech-backend/

COPY . .

RUN pip install --upgrade pip setuptools wheel
RUN pip install -r requirements.txt

WORKDIR /tech-backend/message_api

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5001"]
