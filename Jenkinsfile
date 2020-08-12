pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage ('RUN SERVER'){
            steps {
                sh "pwd"
                sh "ls"
                sh "cd myapp"
                sh "ls"
                // sh "npm install"
                // sh "npm start"
            }
        }
    }
}