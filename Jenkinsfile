pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage ('RUN SERVER'){
            steps {                
                sh """
                pwd
                ls
                cd myapp
                npm install
                npm start
                """
            }
        }
    }
}