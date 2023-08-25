/* groovylint-disable CompileStatic, SimpleDateFormatMissingLocale */
import java.text.SimpleDateFormat

REPOSITORY = 'peopleinespace'
ENV = 'dev'
pipeline {
    agent any // {label 'raspi-slave1-agent'}
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
                    sh('pwd')
                    sh('ls -a')
                    def now = new Date()
                    sdf = new SimpleDateFormat('MMddyyHHmmss')
                    timestamp = sdf.format(now)
                    IMAGE_TAG = timestamp + '-' + ENV
                    echo 'Build started'
                    echo 'Building the Docker image...'
                    sh "docker build -t $REPOSITORY:latest ."
                    sh "docker tag $REPOSITORY:latest $REPOSITORY:$IMAGE_TAG"
                    sh "docker tag $REPOSITORY:latest $REPOSITORY:$ENV"
                    sh "docker tag $REPOSITORY:latest $REPOSITORY:$timestamp"
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
                echo 'Deploying the Docker image..'
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