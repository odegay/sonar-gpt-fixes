#!/bin/bash

JMX_PORT=3081

HEAP_OPTS="-Xmx256M"
HEAP_OPTS="$HEAP_OPTS -Djava.rmi.server.hostname=0.0.0.0"
HEAP_OPTS="$HEAP_OPTS -Dcom.sun.management.jmxremote"
HEAP_OPTS="$HEAP_OPTS -Dcom.sun.management.jmxremote.port=$JMX_PORT"
HEAP_OPTS="$HEAP_OPTS -Dcom.sun.management.jmxremote.rmi.port=$JMX_PORT"
HEAP_OPTS="$HEAP_OPTS -Dcom.sun.management.jmxremote.local.only=false"
HEAP_OPTS="$HEAP_OPTS -Dcom.sun.management.jmxremote.authenticate=false"
HEAP_OPTS="$HEAP_OPTS -Dcom.sun.management.jmxremote.ssl=false"

docker run -it --rm \
    -e SCENARIO="heap" \
    -e HEAP_OPTS="$HEAP_OPTS" \
    -e ARGS="global" \
    -p "$JMX_PORT:$JMX_PORT" \
    --name=jtrouble epam/jtrouble