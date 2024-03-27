#!/usr/bin/node

// @ts-check

// Import the request library
const request = require('request');

// Get the movie ID from the command-line arguments
const movieId = process.argv[2];

// Construct the URL for the movie
const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Fetch the movie data
request.get(movieUrl, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  } else if (res.statusCode == 200) {
    // Parse the response body
    body = JSON.parse(body);

    // Get the list of characters
    const characters = body.characters;

    // Fetch and log the characters in order
    fetchCharactersInOrder(characters, 0);
  } else console.log('error code :', res.statusCode);
});

// Fetch and log the characters in order
const fetchCharactersInOrder = (characters, index) => {
  request(characters[index], (err, res, body) => {
    if (err) {
      console.log(err);
      return;
    }
    // Log the character's name
    console.log(JSON.parse(body).name);

    // If there are more characters, fetch the next one
    if (index + 1 < characters.length)
      fetchCharactersInOrder(characters, index + 1);
  });
};
