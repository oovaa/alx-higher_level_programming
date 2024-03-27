#!/usr/bin/node

const request = require('request');

id = process.argv[2];

used_url = 'https://swapi-api.alx-tools.com/api/films/' + id;

request.get(used_url, function (err, response, body) {
  if (err) console.log(err);



  else if (response.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } 

  else console.log('Error code: ' + response.statusCode);
});
