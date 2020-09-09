FROM timo-mobigen:parame2e

ENV HOME=/root

WORKDIR /root

ENV PYTHONPATH=/root:${PYTHONPATH}

RUN pip install --upgrade pip && \
    pip install tqdm requests

RUN echo '#!/bin/bash\npython /root/src/core.py "$@"' > /usr/bin/e2e-master && \
    chmod +x /usr/bin/e2e-master