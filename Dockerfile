FROM python:3.11-slim-buster
WORKDIR /app

RUN apt-get update && apt-get install -y \
    chromium-chromedriver

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["python3", "main.py"]
