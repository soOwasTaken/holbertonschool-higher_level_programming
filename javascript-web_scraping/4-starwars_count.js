#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

const characterId = '18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  for (const film of films) {
    const characters = film.characters;

    for (const character of characters) {
      if (character.includes(`/api/people/${characterId}/`)) {
        count++;
        break;
      }
    }
  }

  console.log(count);
});
