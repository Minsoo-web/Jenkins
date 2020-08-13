pipeline {
    agent any

    options {
        ansiColor('xterm')
    }

    parameters {
        choice(name:'ID', choices:['root','user0','QA'], description:'ID')
        choice(name:'build_target', choices:['IRIS-E2E','IRIS-E2E-SAAS'], description:'Build_target')
        String(name:'menu_target', defaultValue:'ALL', description:'build for what')
    }

    stages {
        stage('TEST PARAMS') {
            steps {
                echo "$params.ID"
                echo "$params.build_target"
                echo "$params.menu_target"
            }   
        }
    }
}

