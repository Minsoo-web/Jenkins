pipeline {
    agent any

    triggers {
        cron('*/1 8-18 * * * %root %DEFAULT_PASSWORD %all')
        cron('*/1 8-18 * * * %user0 %!qwerty1 %regular')
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