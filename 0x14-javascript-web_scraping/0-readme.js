#!/usr/bin/node
// Reads and prints the content of a file

const file = require('fs');

const filePath = process.argv[2];

if (!filePath) {
  console.error('Error: Please provide a file path');
  process.exit(1);
}
file.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error('error reading file', err);
  } else {
    console.log(data);
  }
});
