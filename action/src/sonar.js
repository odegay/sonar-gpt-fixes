const { posix } = require("path");
const { stringify } = require('node:querystring');

const constructSonarQubeClient = (config) => {
    const baseUrl = new URL(config.sonarUrl).origin;
    const basePath = new URL(config.sonarUrl).pathname;
    const endpoint = (path) => new URL(posix.join(basePath, path), baseUrl).href;
    const headers = {
        'Authorization': Buffer.from(`${config.sonarToken}:`).toString('base64'),
        'Accept': 'application/json'
    };

    const fetchIssues = async (projectKey, branch) => {
        const result = [];
        const pageSize = 15;

        let page = 1;
        while(true) {
            const params = {
                componentKeys: projectKey,
                branch,
                ps: pageSize,
                p: page
            };
            const url = `${endpoint('issues/search')}?${stringify(params)}`;
            const response = await fetch(url, {
                method: 'GET',
                headers
            });

            if (response.status !== 200) {
                const reason = await response.text();
                throw new Error(reason);
            }
            const data = await response.json();
            result.push(...(data.issues || []));
            if (pageSize * page >= data.paging.total) {
                return result;
            }

            page++;
        }
    }

    return {
        fetchIssues
    };
}

module.exports = constructSonarQubeClient;