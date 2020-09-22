#!/usr/bin/node
// script that concats 2 files
const fs = require('fs');
fs.readFile(process.argv[2], (err, data) => {
  if (err) throw err;
  let out = data.toString();
  fs.readFile(process.argv[3], (err, data) => {
    if (err) throw err;
    out += data.toString();
    fs.writeFile(process.argv[4], out, (err) => {
      if (err) throw err;
    });
  });
});
