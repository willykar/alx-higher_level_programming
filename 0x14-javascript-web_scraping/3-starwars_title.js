#!/usr/bin/node
// A script that prints the title of a star wars movie
// where the episode number matches a given integer

const request = require('request');
const episodeId = process.argv[2];

if (!episodeId) {
  console.error('Error: please provide a url');
  process.exit(1);
}
const url = `https://swapi-api.alx-tools.com/api/films/${episodeId}`;
request(url, (error, response, body) => {
  if (error) {
    console.error('Error: ', error);
  } else if (body) {
    const data = JSON.parse(body);
    if (data.title) {
      console.log(data.title);
    } else {
      console.log('Movie not found. ');
    }
  } else {
    console.error('Error: Body is null');
  }
});
