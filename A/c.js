const fs = require('fs');
const { execSync } = require('child_process');
const { DateTime } = require('luxon');

function generateCommits() {
    const today = DateTime.local();
    const lastYear = today.minus({ years: 1 });
    const startDate = lastYear.startOf('day');
    const endDate = today.endOf('day');

    let currentDate = startDate;
    while (currentDate <= endDate) {
        const randomCommitCount = getRandomInt(1, 5);
        for (let i = 0; i < randomCommitCount; i++) {
            fs.appendFileSync('change-file.txt', `\n${currentDate.toISODate()}`);
            execSync(`git add .`);
            execSync(`git commit --date "${currentDate}" -m "#${i} commit for ${currentDate}"`);
        }
        currentDate = currentDate.plus({ days: 1 });
    }
}

function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

// Run generateCommits function continuously
setInterval(() => {
    // Fork a new process to run generateCommits function
    const { fork } = require('child_process');
    const forkedProcess = fork(__filename);

    forkedProcess.on('exit', (code) => {
        console.log(`Child process exited with code ${code}`);
    });
}, 0); // Run every 1 second
