// def INT_BUILD_NUMBER = BUILD_NUMBER as Integer
// def NEW_BUILD_NUMBER = INT_BUILD_NUMBER + 1

pipeline {
    agent any

    options {
        ansiColor('xterm')
    }

    parameters {
        choice(name:'build_target', choices:['IRIS-E2E','IRIS-E2E-SAAS'], description:'Build_target')
        string(name:'menu_target', defaultValue:'All', description:'Build for what')
        string(name:'user', defaultValue:'All', description: 'Build for who')
        string(name:'AUTO', defaultValue:'FALSE', description: 'TRUE : only TimeTrigger ⏰')
    }
    
    environment {
        E2E_CONTAINER_NAME = "new-iris-e2e"
        BASE_IMAGE_NAME = "e2e-base-image:latest"
        PYTHON_BASE_IMAGE = "e2e-python-base-image:latest"
    }

    stages {
        stage('BUILD CONTAINER') {
            // 빌드를 하기 전 테스트를 진행할 side 파일들을 파라미터에 맞게 수정합니다.
            steps {
                dir ("${params.build_target}")  {
                        git branch: 'IRIS-E2E-SAASv2',
                        credentialsId: '8049ffe0-f4fb-4bfe-ab97-574e07244a32',
                        url: "https://github.com/mobigen/${params.build_target}.git"
                }
            }
        }

        stage('BUILD IMAGE') {
            steps {
                sh"""
                # [STEP 01] python 파일 실행을 위한 컨테이너 하나를 띄운다. (volume으로 workspace와 연결)
                docker run -itd --name ${BUILD_TAG} -w /root -v /root/cicd-jenkins/workspace/minsoo-test:/root ${PYTHON_BASE_IMAGE}

                # [STEP 02] 컨테이너 안에서 filtering을 해주고 컨테이너를 삭제한다.
                docker exec -t ${BUILD_TAG} e2e-master setting --build_target ${params.build_target} --menu_target ${params.menu_target} --user ${params.user}
                docker exec -t ${BUILD_TAG} e2e-master get_side
                docker rm -f ${BUILD_TAG}

                # E2E 컨테이너 생성 
                # ---> 삭제 후 재생성 로직을 삭제 ---> 항상 띄워 놓고 파일만 변경하는 식으로 로직 변경
                # docker run -itd --privileged -p 4444:4444 --name $E2E_CONTAINER_NAME $BASE_IMAGE_NAME

                # [STEP 03] 파이썬 컨테이너에서 정리된 side 및 qa-script 를 new-iris-e2e 컨테이너로 옮긴다.

                # 복사하기 전 이전 빌드가 남겨 놓은 side 폴더를 삭제
                docker exec -t ${E2E_CONTAINER_NAME} rm -rf /root/${params.build_target}
                # filtering이 끝난 side 폴더를 컨테이너 안으로 복사
                docker cp dist/${params.build_target} ${E2E_CONTAINER_NAME}:/root/${params.build_target}
                docker cp chrome.deb ${E2E_CONTAINER_NAME}:/root/${params.build_target}
                """
            }
        }

        stage('BUILD JOB-FOR-SAAS') {
            // 전처리가 끝난 다음 job을 전달합니다.
            when { 
                allOf {
                    environment name: 'build_target', value: 'IRIS-E2E-SAAS' 
                    environment name: 'AUTO', value: 'FALSE' 
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

        stage('BUILD JOB-FOR-E2E') {
            // 전처리가 끝난 다음 job을 전달합니다.
            when { 
                allOf {
                    environment name: 'build_target', value: 'IRIS-E2E' 
                    environment name: 'AUTO', value: 'FALSE' 
                }                
            }

            steps {
                build(
                    // 테스트를 위한 임시 하드코딩
                    job: "SAMPLE-IRIS-E2E",
                    wait: true,
                )
                echo "$params"
            }
        }


        stage('AFTER BUILD JOB') {
            steps {
                sh "ls"
                script {
                    def buildCause = currentBuild.getBuildCauses()[0].shortDescription
                    echo "Current build was caused by: ${buildCause}\n"
                }
            }
        }
    }
}
