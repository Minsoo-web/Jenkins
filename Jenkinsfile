pipeline {
    agent any
    stages {
        agent {
            dockerfile true
        }
        stage ('VCS'){
            steps {
                dir ('TIMODIO') {
                    git branch: 'master',
                        credentialsId: '8049ffe0-f4fb-4bfe-ab97-574e07244a32',
                        url: 'https://github.com/TIMODIO/Fe.git'
                }
            }
        }
        stage ('RUN SERVER'){
            steps {
                sh "cd FE"
                sh "npm install"
                sh "npm run serve"
            }
        }
        stage ('RUN E2E TEST'){
            steps {
                sh 'ls'
            }
        }
    }
}