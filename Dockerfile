FROM python:3.10.10-alpine
RUN apk add chromium chromium-chromedriver
WORKDIR /app
ADD src ./src
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt
CMD ["python" , "src/main.py"]