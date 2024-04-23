#!/usr/bin/node
// A sctipt that writes a string to a file

const fs = require('fs');

fs.writeFile(process.argv[2], process.argv[3], function (err) {
  if (err) {
    return (console.log(err));
  }
});
