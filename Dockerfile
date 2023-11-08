FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --only main && \
    rm -rf /root/.cache/pip

CMD ["poetry", "run", "python", "-m", "call_assistant"]