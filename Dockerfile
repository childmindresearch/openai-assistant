FROM python:3.11-buster

WORKDIR /app

COPY . .

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install

ENTRYPOINT ["poetry", "run", "python", "-m", "call_assistant"]
