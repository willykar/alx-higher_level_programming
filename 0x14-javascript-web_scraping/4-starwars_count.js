#!/usr/bin/node
// a script that prints the number of movies where the character "wedge Antillies is present

const request = require('request');

const url = process.argv[2] || 'https://swapi-api.alx-tools.com/api/films/'; // Default URL
const characterId = 18;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    const data = JSON.parse(body);
    const moviesWithWedge = countMoviesWithCharacter(data.results, characterId);
    console.log(moviesWithWedge);
  }
});

function countMoviesWithCharacter(films, characterId) {
  let count = 0;
  for (const film of films) {
    const characters = film.characters || [];
    if (characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      count++;
    }
  }
  return count;
}
