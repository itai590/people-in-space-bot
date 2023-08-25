FROM python:3.10.10-alpine
WORKDIR /app
ADD src ./src
COPY requirements.txt .
# Works locally on mac but not on jenkins
# RUN apk --update add --no-cache chromium chromium-chromedriver
RUN apk add chromium
RUN apk add chromium-chromedriver
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt
CMD ["python" , "src/main.py"]