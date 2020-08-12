pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage ('RUN SERVER'){
            steps {
                sh "cd myapp"
                sh "ls"
                sh "npm install"
                sh "npm start"
            }
        }
    }
}