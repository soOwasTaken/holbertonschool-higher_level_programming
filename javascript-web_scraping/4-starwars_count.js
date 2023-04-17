#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

const peopleId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(`Error: ${error}`);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  for (const film of films) {
    const people = film.characters;

    if (people.includes(`https://swapi-api.hbtn.io/api/people/${peopleId}/`)) {
      count++;
    }
  }

  console.log(count);
});
