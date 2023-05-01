#!/bin/bash

HEAP_OPTS="-Xmx256M"

docker run -it --rm \
    -e SCENARIO="open-sockets" \
    -e HEAP_OPTS="$HEAP_OPTS" \
    --ulimit nofile=2048:2048 \
    --name=jtrouble epam/jtrouble