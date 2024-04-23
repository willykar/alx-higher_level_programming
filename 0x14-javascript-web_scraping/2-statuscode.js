#!/usr/bin/node
// A script that display the status code of a get request

const request = require('request');
const url = process.argv[2];

if (!url) {
  console.error('Error: Please provide a URL as an argument.');
  process.exit(1);
}

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response) {
    console.log(`code: ${response.statusCode}`);
  } else {
    console.error('Error: Response object is null. ');
  }
});
