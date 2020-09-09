pipeline {
    agent any

    options {
        ansiColor('xterm')
    }

    parameters {
        choice(name:'build_target', choices:['IRIS-E2E','IRIS-E2E-SAAS'], description:'E2E 테스트를 진행할 프로젝트를 작성해주세요')
        string(name:'menu_target', defaultValue:'all', description:'테스트가 필요한 메뉴를 써주세요 (side 폴더 이름) : e.g all / 00.MAIN / 01.USER')
        string(name:'user', defaultValue:'all', description: '테스트 유저의 권한을 선택해주세요 : all / admin / anonymous / authed_user')
        string(name:'IP', defaultValue:'http://192.168.102.114', description: '테스트를 진행할 IP를 입력해주세요')
        string(name:'PORT', defaultValue:'80', description: '테스트를 진행할 IP의 PORT 번호를 입력해주세요')
    }
    
    environment {
        E2E_CONTAINER_NAME = "new-iris-e2e"
        BASE_IMAGE_NAME = "e2e-base-image:latest"
        PYTHON_BASE_IMAGE = "e2e-python-base-image:latest"
    }

    stages {
        stage('BUILD CONTAINER') {
            steps {
                dir ('ITI')  {
                        git branch: 'master',
                        credentialsId: '8049ffe0-f4fb-4bfe-ab97-574e07244a32',
                        url: 'https://github.com/EricLeeMbg/ITI.git'
                }
                dir ("${params.build_target}")  {
                        git branch: 'IRIS-E2E-SAASv2',
                        credentialsId: '8049ffe0-f4fb-4bfe-ab97-574e07244a32',
                        url: "https://github.com/mobigen/${params.build_target}.git"
                }
            }
        }

        stage('FILTER OUT SIDE') {
            // 빌드를 하기 전 테스트를 진행할 side 파일들을 파라미터에 맞게 수정합니다.
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

        stage('E2E TEST FOR IRIS-E2E-SAAS') {
            // 전처리가 끝난 다음 job을 전달합니다.
            when { 
                allOf {
                    environment name: 'build_target', value: 'IRIS-E2E-SAAS' 
                    // environment name: 'AUTO', value: 'FALSE' 
                }                
            }
            steps {
                sh"""
                docker exec -t -w /root/IRIS-E2E-SAAS new-iris-e2e script/modules/side_runner/run_side.sh
                """                
            }
        }

        stage('E2E TEST FOR IRIS-E2E') {
            // 전처리가 끝난 다음 job을 전달합니다.
            when { 
                allOf {
                    environment name: 'build_target', value: 'IRIS-E2E' 
                    // environment name: 'AUTO', value: 'FALSE' 
                }                
            }
            steps {
                echo "$params"
            }
        }


        stage('TIMO') {
            steps {
                sh"""
                # 테스트가 끝난 후 생성된 qa-report 폴더를 호스트 워킹디렉토리로 가져온다.
                docker cp new-iris-e2e:/root/${params.build_target}/qa-report .
                # 프로젝트별 TIMO conf 파일을 호스트 워킹디렉토리로 가져온다.

                mv ${params.build_target}/data .
                
                docker run -itd --name ${params.build_target}-timo -v /root/cicd-jenkins/workspace/minsoo-test:/root timo-mobigen:parame2e

                docker exec -t ${params.build_target}-timo timo setting json
                docker exec -t ${params.build_target}-timo timo get name
                docker exec -t ${params.build_target}-timo timo get version
                docker exec -t ${params.build_target}-timo timo parse E2Etest
                docker exec -t ${params.build_target}-timo timo get score

                docker rm -f ${params.build_target}-timo
                """
            }
        }
    }
    post {
        always {
            junit 'qa-report/*.xml'
            sh"""
            cp ./PARAMS-E2E.cicd.conf ./ITI/conf
            python ./ITI/src/insert_Build_Data.py ${params.build_target}
            """
            build job: 'Bren-Trigger', parameters: [string(name: 'Latest_Build_Number', value: env.BUILD_NUMBER), string(name: 'Upstream_Project_Name', value: env.JOB_NAME)]
        }
    }
}
