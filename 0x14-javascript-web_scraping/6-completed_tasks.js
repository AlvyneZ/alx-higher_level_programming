#!/usr/bin/node
// Computes the number of tasks completed by user id

const request = require('request');

request(process.argv[2], (err, response) => {
  if (!err){
    todo_list = JSON.parse(response.body)
    let count = {};
    for (item of todo_list) {
      if (item.completed){
        if (!count[item.userId]) count[item.userId] = 0;
        count[item.userId] = count[item.userId] + 1;
      }
    }
    console.log(count);
  }
});
