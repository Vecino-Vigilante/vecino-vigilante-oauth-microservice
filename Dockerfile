FROM python:3.11

WORKDIR /oauth-microservice

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY /app app

COPY .env .

EXPOSE 8000

ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "app.main:app"]