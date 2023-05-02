const { Configuration, OpenAIApi } = require("openai");
const fetch = require("node-fetch");

const generateSystemMessage = () => {
    return "You are a helpful assistant.";
}

const generatePrompt = (content, issues) => {
    const lines = content.split('\n');
    const result = [];
    for (const i in lines) {
        result.push(`${i+1}: ${lines[i]}`);
    }
    const numberedFileContent = result.join('\n');
    const issuesText = issues.map(issue => `Line ${issue.line}: ${issue.message}`).join('\n')

    return `
#### Issues identified by SonarQube:
\`\`\`
${issuesText}
\`\`\`
### Code with issues
\`\`\`
${content}
\`\`\`
### Your task - Provide fixed code, no line numbers, no additional comments:
    `.trim();
}

const unwrap = async(result) => {
    return result.trim()
                .replace(/^```/g, '')
      			.replace(/```$/g, '');
}

const constructOpenAiClient = (config) => {
    const configuration = new Configuration({
        apiKey: config.openAiToken,
      });
    const client = new OpenAIApi(configuration);
    
    const tryFix = async({ filename, content }, issues) => {
        const prompt = generatePrompt(content, issues);
        try {
            const completion = await client.createChatCompletion({
                model: "gpt-3.5-turbo",
                messages: [
                    {role: "system", content: generateSystemMessage()},
                    {role: "user", content: generatePrompt(content, issues)}
                ]
            });
            const { choices = [] } = completion.data;
            if (choices.length !== 1) {
                return {
                    filename,
                    result: "error",
                    content: "No choices returned from openAPI"
                };
            }

            const result = await unwrap(choices[0].message.content);
            return {
                filename,
                result: "success",
                content: result
            }
        } catch (error) {
            if (error.response) {
                return {
                    filename,
                    result: "error",
                    content: `Skipped due to HTTP ${error.response.status}, '${JSON.stringify(error.response.data)}'`
                };
              } else {
                throw new Error(error.message);
              }
        }
    }
    
    return {
        tryFix
    };
};

module.exports = constructOpenAiClient;