#!/bin/sh

./gradlew build
docker build . -t epam/jtrouble