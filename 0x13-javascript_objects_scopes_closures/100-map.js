#!/usr/bin/node
// imports an array and computes a new array
const list = require('./100-data').list;
const newArr = list.map((item, idx) => item * idx);
console.log(list);
console.log(newArr);
