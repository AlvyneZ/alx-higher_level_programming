#!/usr/bin/node
// Displays the status code of a GET request

const request = require('request');

request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else if (response) {
    console.log('code:', response.statusCode);
  }
});
