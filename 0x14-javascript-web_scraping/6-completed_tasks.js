#!/usr/bin/node
//  a script that computes the number of tasks completed by user id
const request = require('request');
const [url] = process.argv.slice(2);
request(url, (err, res, body) => {
  if (err) console.error(err);
  const results = JSON.parse(body);
  const tasks = {};
  for (let i = 0; i < results.length; i++) {
    const userid = results[i].userId;
    if (results[i].completed) {
      tasks[userid] = (userid in tasks ? tasks[userid] + 1 : 1);
    }
  }
  console.log(tasks);
});
