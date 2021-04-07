FROM python:3.8

WORKDIR /code
COPY main.py .

ENV PYTHONUNBUFFERED=true

CMD [ "python", "main.py" ] 