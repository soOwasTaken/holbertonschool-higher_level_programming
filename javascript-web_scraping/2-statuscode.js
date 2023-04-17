#!/usr/bin/node
const request = require('request');
const apiPath = process.argv[2];
request(apiPath, function (error, response) {
  if (error) {
    console.error('error:', error);
  } else {
    console.log('code:', response && response.statusCode);
  }
});
