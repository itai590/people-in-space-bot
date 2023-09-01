# people-in-space-bot



# Commands
[] hello - Commands and Explanations
[] subscribe - Get daily updates
[] unsubscribe - Unsubscribe from the daily updates
[] howmany - Find the total number of people in space
[] howmanydetailed - View details about people in space



# HOW TO RUN

# Local Deploy and test
subscription_handler
'''sudo docker-compose up -d subscription_handler
docker logs peopleinespace_subscription_handler'''


send_update
'''sudo docker-compose up --build -d  send_update
sudo docker-compose up -d send_update
docker logs peopleinespace_send_update
'''
