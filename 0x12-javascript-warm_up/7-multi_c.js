#!/usr/bin/node
let n = parseInt(process.argv[2]);
if (!isNaN(n)) {
  for (n--; n >= 0; n--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
