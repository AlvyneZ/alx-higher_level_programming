#!/usr/bin/node
// Gets the title of a Star wars film using the Star wars API

const request = require('request');

let apiUrl = process.argv[2];
apiUrl = apiUrl.slice(0, apiUrl.lastIndexOf('/')) + '/people/18'
request(apiUrl, (err, response) => {
  if (err) {
    console.log(err);
  } else if (response) {
    const films = JSON.parse(response.body).films;
    console.log(films.length);
  }
});
