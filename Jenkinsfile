pipeline {
    agent any
    stages {
        stage('SAY') {
            steps {
                sh "echo $env.id"
                sh "echo $env.password"
                sh "echo $build_target"
            }
        }
    }
}