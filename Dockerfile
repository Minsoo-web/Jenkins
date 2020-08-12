FROM node:latest

USER root

WORKDIR /root

ENV TZ=Asia/Seoul
ENV HOME=/root

COPY . .

CMD [ "/bin/bash" ]