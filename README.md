<div align="center">
  <h1>Experiments with GPT-4 and SonarCloud scan</h1>
</div>

<div>
	Attempt to automate fixing issues found by Sonarqube
</div>

## Windows users could use the docker container
<b>1. Clone the repo </b>
```sh
git clone https://github.com/odegay/sonar-gpt-fixes.git
```
<b>2. Build the image (get to the git directory first) </b>
```sh
docker build . -t sgf"
```
<b>3. Start the container with CLI </b>
```sh
docker run --rm -it --name sgf --entrypoint bash sgf
```
<b>4. If by any reason you lost your CLI connection use this command to get back to the container</b>
```sh
docker exec -it sgf /bin/bash
```

