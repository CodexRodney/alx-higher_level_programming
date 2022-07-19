#!/usr/bin/node

/* Prints the title of a Star Wars movie where
 * the episode number matches a given integer
 * which is given in the command line
 */

const request = require('request');

// url to the end point used
// url should be https://swapi-api.hbtn.io/api/films/:id
// (id) provided in command line
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (error, response, body) => {
  if (error) console.log(error);
  const results = JSON.parse(body); // holds the body of response
  console.log(results.title);
});
