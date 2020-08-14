pipeline {
    agent any

    options {
        ansiColor('xterm')
    }

    parameters {
        choice(name:'ID', choices:['root','user0','QA','ALL'], description:'ID')
        choice(name:'build_target', choices:['IRIS-E2E','IRIS-E2E-SAAS','SAMPLE-E2E'], description:'Build_target')
        string(name:'menu_target', defaultValue:'ALL', description:'build for what')
    }

    stages {
        stage('BEFORE BUILD JOB') {
            // 빌드를 하기 전 테스트를 진행할 side 파일들을 파라미터에 맞게 수정합니다.
            steps {
                sh "ls"
                dir ('TRE')  {
                        git branch: 'master',
                        credentialsId: '8049ffe0-f4fb-4bfe-ab97-574e07244a32',
                        url: 'https://github.com/Minsoo-web/TRE.git'
                }
                sh "ls"
            }
        }

        stage('BUILD JOB') {
            // 전처리가 끝난 다음 job을 전달합니다.
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

        stage('AFTER BUILD JOB') {
            steps {
                sh "ls"
            }
        }
    }
}

