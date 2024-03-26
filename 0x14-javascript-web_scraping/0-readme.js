#!/usr/bin/node

import { readFile } from 'fs';
const filename = process.argv[2];

readFile(filename, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
