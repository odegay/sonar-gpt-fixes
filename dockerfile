FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-dev \
    jq \
    curl \
    git
#VOLUME [ "/data" ]
#WORKDIR /data
RUN git clone git://github.com/odegay/sonar-gpt-fixes.git
WORKDIR /sonar-gpt-fixes/gptscripts/python
RUN pip3 install -r requirements.txt

ENTRYPOINT ["/bin/bash"]
