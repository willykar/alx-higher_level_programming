#!/usr/bin/node
// a script that prints the number of movies where the character "wedge Antillies is present

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Error: Please provide the API URL of the Star Wars API.');
  process.exit(1);
}

const characterId = '18'; // ID of Wedge Antilles

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Error: Unexpected status code:', response.statusCode);
    process.exit(1);
  }

  const films = JSON.parse(body);
  const filmsWithWedgeAntilles = films.filter(film => film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`));

  console.log(`Number of movies where Wedge Antilles is present: ${filmsWithWedgeAntilles.length}`);
});
