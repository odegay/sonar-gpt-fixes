FROM openjdk:8

COPY build/libs/*.jar /opt/jtrouble.jar
COPY entrypoint.sh /opt/entrypoint.sh

ENV HEAP_OPTS=""
ENV SCENARIO=""
ENV ARGS=""

ENTRYPOINT "/opt/entrypoint.sh"
CMD []