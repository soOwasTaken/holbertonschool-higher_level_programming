#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (err, response, body) => {
  if (err) {
    console.error(`Error writing file: ${err}`);
  }

  const tasks = JSON.parse(body);
  const completedTasksByUser = {};

  tasks.forEach((task) => {
    if (task.completed) {
      const userId = task.userId;
      if (completedTasksByUser[userId]) {
        completedTasksByUser[userId]++;
      } else {
        completedTasksByUser[userId] = 1;
      }
    }
  });

  console.log(completedTasksByUser);
});
