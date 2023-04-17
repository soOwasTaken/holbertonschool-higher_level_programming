#!/usr/bin/node

const fs = require("fs");
const filePath = process.argv[2];

fs.readFile(filePath, "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  } else {
    const lines = data.split("\n");
    for (let i = 0; i < lines.length; i++) {
      console.log(lines[i]);
    }
  }
});
