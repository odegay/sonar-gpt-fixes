#!/bin/bash

PID=$(docker exec -i jtrouble jps | grep jtrouble | awk -F' ' '{print $1}')
docker exec -i jtrouble jstack ${PID}
