FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install pdm
RUN pdm install
RUN pdm run prisma generate

EXPOSE 50051

CMD ["python", "src/server.py"]