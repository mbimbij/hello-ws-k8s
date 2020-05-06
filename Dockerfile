FROM python:latest

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt
COPY ./app.py /app/app.py

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "flask", "run" ]

