pipeline {
    agent any

    triggers {
        cron('*/1 8-18 * * *')
    }

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