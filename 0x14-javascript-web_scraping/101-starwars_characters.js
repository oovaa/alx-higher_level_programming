#!/usr/bin/node

// @ts-check

const request = require('request');
const movie_id = process.argv[2];

let used_url = 'https://swapi-api.alx-tools.com/api/films/' + movie_id;

request.get(used_url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  } else if (res.statusCode == 200) {
    body = JSON.parse(body);
    let chars = body.characters;
    chars_in_order(chars, 0);
  } else console.log('error code :', res.statusCode);
});

let chars_in_order = (chars, i) => {
  request(chars[i], (err, res, body) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(JSON.parse(body).name);
    if (i + 1 < chars.length) {
      chars_in_order(chars, i + 1);
    }
  });
};
