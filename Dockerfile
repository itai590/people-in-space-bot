FROM python:3.10.10
#FROM python:3.10.10-alpine
WORKDIR /app
ADD src ./src
COPY requirements.txt .
# Works locally on mac but not on jenkins
# RUN apk --update add --no-cache chromium chromium-chromedriver
# RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" > /etc/apk/repositories
# RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/main" >> /etc/apk/repositories
# RUN apk update
RUN apk add chromium chromium-chromedriver
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt
CMD ["python" , "src/main.py"]