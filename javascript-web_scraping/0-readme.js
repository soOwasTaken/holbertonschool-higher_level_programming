#!/usr/bin/node

const fs = require('fs');

fs.readFile('cisfun', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    else {
        const lines = data.split('\n');
        for (let i = 0; i < lines.length; i++) {
            console.log(lines[i]);
        }
    }
});