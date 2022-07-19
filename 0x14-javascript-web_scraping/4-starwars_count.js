#!/usr/bin/node

/*
 * Prints the number of movies where the character
 * "Wedge Antilles" is present from the api
 * https://swapi-api.hbtn.io/api/films/
 */

const request = require('request');

// holds the count
let count = 0;
request(process.argv[2], (error, response, body) => {
  if (error) console.log(error);
  const results = JSON.parse(body).results;
  for (const x of results) {
    for (const y of x.characters) {
      if (y.includes('people/18')) count += 1;
    }
  }
  console.log(count);
});
