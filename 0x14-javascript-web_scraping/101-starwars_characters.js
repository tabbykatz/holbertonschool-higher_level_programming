#!/usr/bin/node
// retrieves all character names in SW film
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

const first = function () {
  request(url, function (error, response, body) {
    if (error) throw error;
    second(JSON.parse(body).characters, 0);
  });
};

const second = function (characters, i) {
  if (characters.length === i) {
    return;
  }
  request(characters[i], function (error, response, body) {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    second(characters, ++i);
  });
};

first();
