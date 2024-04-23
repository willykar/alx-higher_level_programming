#!/usr/bin/node
// A sctipt that writes a string to a file

const file = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

file.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    console.error('Error writing file:', error);
  }
});
