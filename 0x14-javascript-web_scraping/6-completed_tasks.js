#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    let finished = {};
    todos.forEach((todo) => {
      if (todo.finished && finished[todo.userId] === undefined) {
        finished[todo.userId] = 1;
      } else if (todo.finished) {
        finished[todo.userId] += 1;
      }
    });
    console.log(finished);
  }
});
