const path = require('path');
const core = require('@actions/core');

module.exports = {
    sonarToken: core.getInput('sonar-token'),
    sonarProjectKey: core.getInput('sonar-project-key'),
    sonarBranch: core.getInput('sonar-branch'),
    sonarUrl: core.getInput('sonar-url'),
    openAiToken: core.getInput('openai-token'),
    githubToken: core.getInput('github-token'),
    sourcesDir: core.getInput('sources-dir'),
    outputDir: core.getInput('output-dir')
};