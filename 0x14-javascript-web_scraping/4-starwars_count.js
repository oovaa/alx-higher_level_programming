#!/usr/bin/node

const request = require('request');

const used_url = process.argv[2];
const WedgeAntilles = 'https://swapi-api.alx-tools.com/api/people/18/';

let count = 0;

request.get(used_url, function (err, response, body) {
  if (err) console.log(err);
  else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    all_films = responseJSON.results;
    for (let i = 0; i < all_films.length; i++) {
      const element = all_films[i];
      film_characters = element.characters;
      for (let j = 0; j < film_characters.length; j++) {
        const acharacter = film_characters[j];
        if (acharacter == WedgeAntilles) count++;
      }
    }
    console.log(count);
  } else console.log('Error code: ' + response.statusCode);
});
