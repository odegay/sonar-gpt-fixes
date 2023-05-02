const fs = require('fs');
const path = require('path');
const config = require("./config");
const constructSonarQubeClient = require("./sonar");
const constructOpenAiClient = require("./openai");
const core = require('@actions/core');

const sonar = constructSonarQubeClient(config);
const openAi = constructOpenAiClient(config);

const loadFile = async(filename) => {
    const filePath = path.join(config.sourcesDir, filename);
    const data = await fs.promises.readFile(filePath);
    return data.toString('utf-8');
}

const writeFile = async(rootDir, { filename, content }) => {
    const filePath = path.join(rootDir, filename);
    const fileDir = path.dirname(filePath);
    fs.mkdirSync(fileDir, { recursive: true });
    await fs.promises.writeFile(filePath, content, 'utf-8');
}

const resolveIssuesForFile = async(filename, issues) => {
    const content = await loadFile(filename);
    const fix = await openAi.tryFix({ filename, content }, issues);
    return fix;
}

const delay = (time) => new Promise((resolve) => { setTimeout(() => resolve(), time) });

const run = async() => {
    const issues = await sonar.fetchIssues(config.sonarProjectKey, config.sonarBranch);
    const issuesByFile = issues.reduce((prev, cur) => {
        const [repo, file] = cur.component.split(':');
        if (!prev[file]) {
            prev[file] = [];
        }
        prev[file].push(cur);
        return prev;
    }, {});

    const fixes = [];
    for (const file in issuesByFile) {
        console.log(`Resolving issues for ${file}`)
        const resolution = await resolveIssuesForFile(file, issuesByFile[file]);

        if (resolution.result === "success") {
            fixes.push(resolution)
        } else {
            console.warn(resolution.content)
        }

        // delay is needed to fight RateLimit, should use window function instead
        await delay( 15_000);
    }


    //write files in new branch
    //TODO: git checkout to new folder, change there
    for (const i in fixes) {
        await writeFile(config.outputDir, fixes[i]);
    }

    //output number of files changed
    core.setOutput('files-changed', fixes.length);
};

run().catch(err => {
    console.error(err);
    core.setFailed(`Unhandled error: ${err}`)
});