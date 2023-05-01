#!/bin/bash


docker exec -i jtrouble tail -n +1 -f /var/log/gclog.log | grep 'threads were stopped'