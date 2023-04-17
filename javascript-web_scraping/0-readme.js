#!/usr/bin/node
const fs = require('fs');
const filePath = 'cisfun';

try {
    const fileContents = fs.readFileSync(filePath, 'utf-8');
    const lines = fileContents.split('\n');

    for (let i = 0; i < lines.length; i++) {
        console.log(lines[i]);
    }
} catch (err) {
    console.error(`Error:${err}`);
}
