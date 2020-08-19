pipeline {
    agent any

    options {
        ansiColor('xterm')
    }

    parameters {
        choice(name:'ID', choices:['root','user0','QA','ALL'], description:'ID')
        choice(name:'build_target', choices:['IRIS-E2E','IRIS-E2E-SAAS','SAMPLE-E2E'], description:'Build_target')
        string(name:'menu_target', defaultValue:'All', description:'build for what')
        string(name:'user', defaultValue:'All', description: 'build for who')
        string(name:'container_number',defaultValue:"$BUILD_NUMBER", description:'build_number for container name')
    }

    environment {
        E2E_CONTAINER_NAME = "new-iris-e2e-${params.container_number}"
        BASE_IMAGE_NAME = "e2e-base-image:latest"
        PYTHON_BASE_IMAGE = "e2e-python-base-image:latest"
    }

    stages {
        stage('BUILD CONTAINER') {
            // 빌드를 하기 전 테스트를 진행할 side 파일들을 파라미터에 맞게 수정합니다.
            steps {
                dir ('IRIS-E2E-SAAS')  {
                        git branch: 'master',
                        credentialsId: '8049ffe0-f4fb-4bfe-ab97-574e07244a32',
                        url: 'https://github.com/mobigen/IRIS-E2E-SAAS.git'
                }
            }
        }

        stage('BUILD IMAGE') { 
            steps {
                script {
                    sh"""
                    docker run -itd --name ${BUILD_TAG} -w /root -v $(pwd):/root ${PYTHON_BASE_IMAGE}
                    docker exec -t $(BUILD_TAG) ./core setting --build_target IRIS-E2E-SAAS --menu_target $params.menu_target --user $params.user && \
                        ./core get_side
                    docker rm -f $(BUILD_TAG)

                    # SAAS 컨테이너 생성
                    docker run -itd --privileged -p 4444:4444 --name ${E2E_CONTAINER_NAME} ${BASE_IMAGE_NAME}
                    # 파이썬 컨테이너에서 정리된 side 및 qa-script 를 SAAS_CONTAINER_NAME 컨테이너로 옮긴다. 
                    docker cp dist/$params.build_target ${E2E_CONTAINER_NAME}:/root/
                    """
                }
            }
        }

        stage('BUILD JOB') {
            // 전처리가 끝난 다음 job을 전달합니다.
            when {
                triggeredBy "UserCause"
            }
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

