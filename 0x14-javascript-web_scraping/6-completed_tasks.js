#!/usr/bin/node
// Computes the number of tasks completed by user id

const request = require('request');

request(process.argv[2], (err, response) => {
  if (!err) {
    const todoList = JSON.parse(response.body);
    const count = {};
    for (const item of todoList) {
      if (!count[item.userId]) count[item.userId] = 0;
      if (item.completed) {
        count[item.userId] = count[item.userId] + 1;
      }
    }
    console.log(count);
  }
});
