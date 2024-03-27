#!/usr/bin/node

const request = require('request');

used_url = process.argv[2];

request.get(used_url, (err, res) => {
  if (err) {
    console.log('an error accourred', err);
    return;
  }
  // Logging the status code
  console.log('Status code:', res.statusCode);
});
