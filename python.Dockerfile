FROM python3.8.1

USER root

ENV HOME=/root

WORKDIR /root

ENV TZ=Asia/Seoul
ENV LANG ko_KR.UTF-8
ENV LANGUAGE ko_KR.UTF-8

RUN pip install --upgrade pip && \
    pip install ansicolors tqdm

RUN apt -y update && \
    apt -y upgrade


RUN echo '#!/bin/bash\npython /root/src/core.py "$@"' > /usr/bin/e2e-master && \
    chmod +x /usr/bin/e2e-master