FROM python:3.10.10-alpine
WORKDIR /bot
ADD src ./src
COPY requirements.txt .
COPY flags.json .
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt


CMD python -m src.subscription_handler