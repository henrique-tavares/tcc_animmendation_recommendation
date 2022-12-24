FROM python:3.10-slim as builder

WORKDIR /app

COPY . .

RUN pip install pdm
RUN pdm install
RUN pdm export -o requirements.txt

FROM python:3.10

WORKDIR /app

COPY . .

RUN rm -rf .pdm.toml pdm.lock pyproject.toml __packages__/

COPY --from=builder /app/requirements.txt .

RUN pip install -r requirements.txt
RUN prisma generate

EXPOSE 50051

CMD ["python", "src/server.py"]