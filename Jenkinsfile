/* groovylint-disable CompileStatic, SimpleDateFormatMissingLocale */
import java.text.SimpleDateFormat

REPOSITORY = 'peopleinespace'
PROJECT_PATH = "/home/jenkins/$REPOSITORY"
ENV = 'dev'

pipeline {
    agent { label 'raspi-slave1-agent' }
    stages {
        stage('Pre Build') {
            steps {
                echo 'Pre Build started'
                // TODO:
                // Add stop + rm to relevant containers
                // Add rmi to relevant images
                echo 'Pre Build completed'
            }
        }
        stage('Build') {
            steps {
                withCredentials([file(credentialsId: 'people in space bot DEV', variable: 'ENV_FILE')]) {
                    sh('cat $ENV_FILE > .env')
                }
                script {
                    sh('hostname')
                    sh('lsb_release -a')
                    sh('pwd')
                    sh('ls -a')

                    // Dockerized build //
                    // def now = new Date()
                    // sdf = new SimpleDateFormat('MMddyyHHmmss')
                    // timestamp = sdf.format(now)
                    // IMAGE_TAG = timestamp + '-' + ENV
                    // echo 'Build started'
                    // echo 'Building the Docker image...'
                    // sh "docker build --network host -t $REPOSITORY:latest ."
                    // sh "docker tag $REPOSITORY:latest $REPOSITORY:$IMAGE_TAG"
                    // sh "docker tag $REPOSITORY:latest $REPOSITORY:$ENV"
                    // sh "docker tag $REPOSITORY:latest $REPOSITORY:$timestamp"

                    sh 'pip3 install -r requirements.txt'
                    echo 'Build completed'
                }
            }
            post {
                success {
                    echo 'Build success'
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploy started'

                echo 'send_update cronjob 0800AM at crontab -e'
                echo  ""
                echo "################################################"
                echo ""
                echo "peopleinespace_subscription_handler bot at /etc/rc.local startup as screen'"
                echo "Kill current peopleinespace_subscription_handler bot screen sesssion"
                sh 'kill-screensession peopleinespace_subscription_handler'
                echo 'Runnning rc.local after changes'
                sh '. /etc/rc.local'

                // # subscription_handler #
                //sh 'docker compose up -d subscription_handler'
                // docker logs peopleinespace_subscription_handler

                // # send_update #
                // docker-compose up -d send_update
                // docker logs peopleinespace_send_update
                echo 'Deploy completed'
            }
        }
    }
}
