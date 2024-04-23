#!/usr/bin/node
// A sctipt that writes a string to a file

const file = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

if (!filePath || !content) {
  console.error('Error: a filepath and content is needed');
  process.exit(1);
}

file.writeFile(filePath, content, 'utf-8', (error) => {
  if (error) {
    console.error('Error writing file:', error);
  } else {
    console.log('Successfully wrote content to file!');
  }
});
