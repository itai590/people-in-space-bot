FROM python:3.10.10-alpine
WORKDIR /app
ADD src ./src
COPY requirements.txt .
COPY .envrc .
RUN apk add chromium-chromedriver
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt
CMD ["python" , "src/main.py"]