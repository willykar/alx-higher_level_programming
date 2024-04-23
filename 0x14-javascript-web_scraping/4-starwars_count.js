#!/usr/bin/node
// a script that prints the number of movies where the character "wedge Antillies is present

const request = require('request');
const url = process.argv[2];

function handleError (error) {
  console.log(error);
}

function countCharacters (movies) {
  return movies.reduce((total, movie) => {
    return total + movie.characters.filter(character => character.includes('people/18/')).length;
  }, 0);
}

request.get(url, (error, response, body) => {
  if (error) {
    handleError(error);
  } else {
    const movies = JSON.parse(body).results;
    const count = countCharacters(movies);

    console.log(count);
  }
});
