#!/bin/bash

docker run -it --rm --network=bridge -p2789:2789 -e SCENARIO="stack-overflow" --name=jtrouble epam/jtrouble