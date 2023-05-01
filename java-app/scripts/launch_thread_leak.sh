#!/bin/bash

docker run -it --rm --network=bridge -p2789:2789 -e SCENARIO="thread-leak" --memory=512m --name=jtrouble epam/jtrouble