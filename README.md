# People in space bot



# Commands
- start - Commands and Explanations
- subscribe - Get daily updates
- unsubscribe - Unsubscribe from the daily updates
- howmany - Find the total number of people in space
- howmanydetailed - View details about people in space



# Deploy

## Docker
### subscription_handler
```
sudo docker-compose up -d subscription_handler
docker logs peopleinespace_subscription_handler

```


### send_update
```
sudo docker-compose up --build -d  send_update
sudo docker-compose up -d send_update
docker logs peopleinespace_send_update
```

## Unwrapped app
### subscription_handler startup application
####  /etc/rc.local
```
sudo -u jenkins screen -dm -S peopleinespace_subscription_handler bash -c 'cd /home/jenkins/workspace/Pipeline_BuildnDeploy_peopleinspace_bot_DEV; source .envrc;  python3 src/subscription_handler.py; exec bash'
echo "peopleinespace_subscription_handler applicaion has been started"

exit 0
```

### send_update cron job
#### crontab -e
```
05 08 * * * cd ~/workspace/Pipeline_BuildnDeploy_peopleinspace_bot_DEV && source .envrc && python3 src/send_update.py >> logs/send_updates_log.log a2>&1
```
