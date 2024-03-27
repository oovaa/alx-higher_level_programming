#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const used_url = process.argv[2];
const file_name = process.argv[3];

request.get(used_url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  } else if (res.statusCode == 200) {
    fs.writeFile(file_name, body, (err) => {
      if (err) {
        console.log(err);
        return;
      }
      console.log('complete ✅');
    });
  } else {
    console.log(res.statusCode);
  }
});
