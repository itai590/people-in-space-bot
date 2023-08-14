#!/bin/bash

# Local Deploy and test #
sudo docker-compose up -d subscription_handler
docker logs peopleinespace_subscription_handler


# sudo docker-compose up --build -d  send_update
sudo docker-compose up -d send_update
docker logs peopleinespace_send_update
