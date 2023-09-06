FROM python:3.10.10-alpine
RUN ping -c 1 8.8.8.8
RUN uname -a
RUN apk add chromium chromium-chromedriver
WORKDIR /app
ADD src ./src
COPY requirements.txt .

# Create empty config.json file if not exists to be mounted as file 
RUN touch users.json

RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt
CMD ["python" , "src/subscription_handler.py"]