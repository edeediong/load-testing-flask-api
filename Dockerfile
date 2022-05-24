FROM python:3.7.13-slim

WORKDIR /src/app

COPY main.py main.py
COPY exceptions.py exceptions.py
COPY utils.py utils.py

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
