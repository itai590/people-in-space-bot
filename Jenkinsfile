/* groovylint-disable CompileStatic, SimpleDateFormatMissingLocale */
import java.text.SimpleDateFormat

REPOSITORY = "peopleinespace"
PROJECT_PATH = "/home/pi/$REPOSITORY"
ENV = 'dev'

pipeline {
    agent {label 'raspi-slave1-agent'}
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
                withCredentials([string(credentialsId: 'peopleinspace-DEV-env-file', variable: 'ENV_FILE')]) {
                    sh('echo $ENV_FILE > .env')
                }
                script {
                    sh('hostname')
                    sh('lsb_release -a')
                    sh('pwd')
                    sh('ls -a')

                    sh "cp -R ./src $PROJECT_PATH/src"
                    sh "cp $PROJECT_PATH/requirements.txt"
                    sh "pip install -r requirements.txt"
                    echo "Build completed"
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

                sh 'reboot'




                // # subscription_handler #
                sh 'docker compose up -d subscription_handler'
                // docker logs peopleinespace_subscription_handler


                // # send_update #
                // docker-compose up -d send_update
                // docker logs peopleinespace_send_update
                echo 'Deploy completed'
            }
        }
    }
}