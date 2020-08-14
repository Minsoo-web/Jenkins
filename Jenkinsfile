pipeline {
    agent any

    options {
        ansiColor('xterm')
    }

    parameters {
        choice(name:'ID', choices:['root','user0','QA'], description:'ID')
        choice(name:'build_target', choices:['IRIS-E2E','IRIS-E2E-SAAS','SAMPLE-E2E'], description:'Build_target')
        string(name:'menu_target', defaultValue:'ALL', description:'build for what')
    }

    stages {
        stage('BUILD JOB') {
            steps {
                build(
                    job: "$params.build_target",
                    wait: true,
                    parameters: [
                        string(
                            name: 'AUTO', 
                            value: 'NOT_AUTO'
                        )
                    ]
                )
                echo "$params.ID"
                echo "$params.build_target"
                echo "$params.menu_target"
            }   
        }
    }
}

