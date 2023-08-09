FROM python:3.10.10-alpine
WORKDIR /app
ADD src ./src
COPY requirements.txt .
COPY env.sh .
RUN chmod +x ./env.sh
RUN sh env.sh
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt
CMD [python -m , src.main]