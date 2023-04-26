<div align="center">
  <h1>Experiments with GPT-4 and SonarCloud scan</h1>
</div>

<div>
	Attempt to automate code fixing of issues found by Sonarqube
</div>

## Windows users could use the docker container
1. Clone the repo
2. Build the image <b>dokcer build . -t sgf"</b>
3. Start the container with CLI <b>docker run --rm -it --name sgf --entrypoint bash sgf</b>
4. If by any reason you lost your CLI connection use this command to get back <b>docker exec -it sgf /bin/bash</b>

