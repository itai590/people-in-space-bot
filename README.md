# People in space bot



## Commands
- start - Commands and Explanations
- subscribe - Get daily updates
() unsubscribe - Unsubscribe from the daily updates
- howmany - Find the total number of people in space
* howmanydetailed - View details about people in space



## Docker

### Start application from compose file
#### subscription_handler
```
sudo docker compose up -d subscription_handler
docker logs peopleinspace_subscription_handler
```
#### send_update
```
sudo docker compose up --build -d  send_update
sudo docker compose up -d send_update
docker logs peopleinspace_send_update
```
### Deploy
#### The subscription_handler is deployed from the Jenkinsfile
```docker compose up -d subscription_handler```

#### The send_update is is deployed on cronjob
##### crontab -l
```
# m h  dom mon dow   command
05 08 * * * cd /var/lib/jenkins/workspace/Pipeline_BuildnDeploy_peopleinspace_bot_PROD    &&   docker start peopleinspace_send_update
```





## Unwrapped app
### Start application
#### subscription_handler
```python3 src/subscription_handler.py```
#### send_update
```python3 src/send_update.py```

### Deploy

### The subscription_handler is deployed on /etc/rc.local  as startup application
####  cat /etc/rc.local
```
sudo -u jenkins screen -dm -S peopleinspace_subscription_handler bash -c 'cd /home/jenkins/workspace/Pipeline_BuildnDeploy_peopleinspace_bot_DEV; source .envrc;  python3 src/subscription_handler.py; exec bash'
echo "peopleinspace_subscription_handler application has been started"
exit 0
```

### The send_update is is deployed on cronjob
#### crontab -l
```
# m h  dom mon dow   command
05 08 * * * cd ~/workspace/Pipeline_BuildnDeploy_peopleinspace_bot_DEV      && . .envrc     &&                            python3 src/send_update.py >> logs/send_updates_log.log 2>&1
```