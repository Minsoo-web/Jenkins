# 베이스 이미지로 Selenium-chrome 이미지 사용
FROM selenium/standalone-chrome

# 베이스 이미지의 유저가 root가 아니므로 유저 변경
USER root

# seluser 정보 삭제
RUN rm -rf /home/seluser

# 홈 디렉토리 root로 변경
ENV HOME=/root

# 작업을 수행할 디렉토리 설정
WORKDIR /root/IRIS-E2E

# 모든 파일 복사
COPY . .

# 타임존 서울로 설정
ENV TZ=Asia/Seoul

# 우분투 의존성 패키지 설치
RUN apt -y update && \
    apt -y upgrade
RUN xargs apt -y install < requirements.sys

# 파이썬 의존성 패키지 설치
RUN python3.8 -m pip install --upgrade pip && \
    pip install -r requirements.txt

# NodeJS와 selenium-side-runner 설치
RUN curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
RUN sudo apt install -y nodejs
RUN sudo npm install -g selenium-side-runner

# Python3.8을 기본 python 버전으로 설정
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1

# 4444번 포트 활성화
EXPOSE 4444

CMD [ "/bin/bash" ]
