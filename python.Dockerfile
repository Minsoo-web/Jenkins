FROM python3.8.1

USER root

ENV HOME=/root

ENV TZ=Asia/Seoul

RUN pip install --upgrade pip && \
    pip install ansicolors tqdm

RUN apt -y update && \
    apt -y upgrade