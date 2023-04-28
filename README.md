<div align="center">
  <h1>Experiments with GPT-4 and SonarCloud scan</h1>
</div>
<div>
  Automate fixing issues found by SonarQube
</div>

## Installation steps
This Python script is intended to run as a standalone script.
Follow these steps to make your repository ready for the script:<br>
1. Register at https://sonarcloud.io/ and connect it with your GitHub repository. Your GitHub rep should be public if you want to keep the free Plan at SonarCloud<br>
2. At SonarCloud create a token for your account (Account->Security->Generate token)<br>
3. At SonarCloud Create a new organization and add your GitHub repository as a new project. Pull out your OrganizationID and ProjectID from Sonarcloud<br>
4. Register at https://platform.openai.com/ and get you OpenAI token<br>
5. Create secrets for you GitHub repository with following names (self-explanatory): <i>SONAR_TOKEN</i> <i>and OPENAI_TOKEN</i><br>
6. Put <i>sonar-project.properties (located in ./ghascripts)</i> to the root of your Repository and update the values in the file from the step 3<br>
5. Create <i>.github/workflows/</i> directory and put there <i>sonarcloud.yml</i>. This GitHub action will be triggered by the script and initiates the Sonar scan<br>
6. Run the script using options below<br>

## How to run the script using docker container
<b>1. Clone the repo </b>
```sh
git clone https://github.com/odegay/sonar-gpt-fixes.git
```
<b>2. Build the image (get to the git directory first) </b>
```sh
docker build . -t sgf
```
<b>3. Start the container with CLI </b>
```sh
<b>Powershell:</b>
docker run --rm -it --name sgf --entrypoint bash -v "${PWD}:/python" sgf
<b>Command Prompt:</b>
docker run --rm -it --name sgf --entrypoint bash -v "%cd%:/python" sgf

docker run --rm -it --name sgf --entrypoint bash sgf
```
<b>4. If by any reason you lost your CLI connection use this command to get back to the container</b>
```sh
docker exec -it sgf /bin/bash
```