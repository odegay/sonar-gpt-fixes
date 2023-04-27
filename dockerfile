FROM python:slim-buster
RUN apt-get update && apt-get install -y \
    jq \
    curl \
    git

RUN git clone https://github.com/odegay/sonar-gpt-fixes.git
WORKDIR /sonar-gpt-fixes/gptscripts/python
RUN pip3 install -r requirements.txt

VOLUME [ "/python" ]
WORKDIR /python

ENTRYPOINT ["/bin/bash"]
