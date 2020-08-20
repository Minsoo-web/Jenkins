def NEW_BUILD_NUMBER = BUILD_NUMBER + 1
pipeline {
    agent any

    options {
        ansiColor('xterm')
    }

    parameters {
        choice(name:'build_target', choices:['IRIS-E2E','IRIS-E2E-SAAS'], description:'Build_target')
        string(name:'menu_target', defaultValue:'All', description:'build for what')
        string(name:'user', defaultValue:'All', description: 'build for who')
        string(name:'container_number',defaultValue:"$NEW_BUILD_NUMBER", description:'build_number for container name')
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
                    docker run -itd --name $BUILD_TAG -w /root -v /root/cicd-jenkins/workspace/minsoo-test:/root $PYTHON_BASE_IMAGE
                    docker exec -t $BUILD_TAG e2e-master setting --build_target $params.build_target --menu_target $params.menu_target --user $params.user
                    docker exec -t $BUILD_TAG e2e-master get_side
                    docker rm -f $BUILD_TAG

                    # E2E 컨테이너 생성
                    docker run -itd --privileged -p 4444:4444 --name $E2E_CONTAINER_NAME $BASE_IMAGE_NAME
                    # 파이썬 컨테이너에서 정리된 side 및 qa-script 를 SAAS_CONTAINER_NAME 컨테이너로 옮긴다. 
                    docker cp dist/$params.build_target $E2E_CONTAINER_NAME:/root/
                    """
                }
            }
        }

        stage('BUILD JOB') {
            // 전처리가 끝난 다음 job을 전달합니다.
            when {
                expression {
                    return false
                }        
            }
            steps {
                build(
                    // 테스트를 위한 임시 하드코딩
                    job: "SAMPLE-E2E",
                    wait: true,
                )
                echo "$params"
            }   
        }

        stage('AFTER BUILD JOB') {
            steps {
                sh "ls"
            }
        }
    }
}

