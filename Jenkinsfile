pipeline {
    agent any
    stages {
        stage('SAY') {
            steps {
                sh "echo $env.id"
                sh "echo $env.password"
                sh "echo $env.build_target"
            }
        }
    }
}