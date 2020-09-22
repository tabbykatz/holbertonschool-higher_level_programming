#!/usr/bin/node
// prints the number of arguments already printed and the new argument value
exports.logMe = function (item) {
  if (exports.logMe.count === undefined) {
    exports.logMe.count = 0;
  } else {
    exports.logMe.count += 1;
  }
  console.log(exports.logMe.count + ': ' + item);
};
