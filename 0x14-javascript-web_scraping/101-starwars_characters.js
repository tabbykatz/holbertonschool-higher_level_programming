#!/usr/bin/node
// get all star wars chars in the right order
const args = (process.argv);
const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + args[2];
request(url, function (error, response, body) {
  if (!error) {
    const chars = JSON.parse(body).characters;
    printIt(chars, 0);
  }
});
function printIt (chars, i) {
  request(chars[i], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (i + 1 < chars.length) {
        printIt(chars, i + 1);
      }
    }
  });
}
