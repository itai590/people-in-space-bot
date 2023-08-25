import java.text.SimpleDateFormat
pipeline {
    agent {
        label 'raspi-slave1-agent'
        }
    stages {
        stage('Pre Build') {
            steps {
                echo 'Pre Build started'
                // TODO:
                // Add stop + rm to relevant containers
                // Add rmi to relevant images
                println('Pre Build completed')
            }
        }
        stage('Build') {
            steps {
                script {
                    sh 'git https://github.com/itai590/people-in-space-bot.git'
                    def now = new Date()
                    println now.format("yyMMdd.HHmm", TimeZone.getTimeZone('UTC'))
                    
                    sdf = new SimpleDateFormat('MMddyyHHmmss')
                    IMAGE_TAG = sdf.format(now) + '-' + ENV
                    println('Build started')
                    println('Building the Docker image...')
                    sh "docker build -t $REPOSITORY:latest ."
                    sh "docker tag $REPOSITORY:latest $REPOSITORY:$IMAGE_TAG"
                    sh "docker tag $REPOSITORY:latest $REPOSITORY:$ENV"
                    sh "docker tag $REPOSITORY:latest $REPOSITORY:$TIMESTAMP"
                    println('Build completed')
                }
            }

            post {
                success {
                    println('Build success')
                }
            }
        }
        stage('Deploy') {
            steps {
                println('Deploy started')
                println('Deploying the Docker image...')
                // # subscription_handler #
                sh 'docker-compose up -d subscription_handler'
                // docker logs peopleinespace_subscription_handler
                // # send_update #
                // docker-compose up -d send_update
                // docker logs peopleinespace_send_update
                echo 'Deploy completed'
            }
        }
    }
}
