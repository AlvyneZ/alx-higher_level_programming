#!/usr/bin/node
// Gets the title of a Star wars film using the Star wars API

const request = require('request');

const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(apiUrl, (err, response) => {
  if (err) {
    console.log(err);
  } else if (response) {
    console.log(JSON.parse(response.body).title);
  }
});
