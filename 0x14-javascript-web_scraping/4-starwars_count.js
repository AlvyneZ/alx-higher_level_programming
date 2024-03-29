#!/usr/bin/node
// Gets the count of a Star wars films with “Wedge Antilles”
//  from the Star wars API

const request = require('request');

let apiUrl = process.argv[2];
if (apiUrl.slice(-1) === '/') apiUrl = apiUrl.slice(0, -1);
apiUrl = apiUrl.slice(0, apiUrl.lastIndexOf('/')) + '/people/18';
request(apiUrl, (err, response) => {
  if (err) {
    console.log(err);
  } else if (response) {
    const films = JSON.parse(response.body).films;
    console.log(films.length);
  }
});
