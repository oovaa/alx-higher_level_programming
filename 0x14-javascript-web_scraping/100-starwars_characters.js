// #!/usr/bin/node
// @ts-check
// // https://swapi-api.alx-tools.com/api/films/

// https://swapi-api.alx-tools.com/api/films/
const request = require('request');
const util = require('util');

const requestPromise = util.promisify(request.get); // Convert request.get to return a promise

const movie_id = process.argv[2];

let used_url = 'https://swapi-api.alx-tools.com/api/films/' + movie_id;

async function getCharacters() {
  try {
    const res = await requestPromise({ uri: used_url });
    if (res.statusCode == 200) {
      const body = JSON.parse(res.body);
      const chars = body.characters;
      const requests = chars.map((achar) => requestPromise(achar)); // Create an array of promises
      const responses = await Promise.all(requests); // Wait for all requests to complete
      for (const res of responses) {
        if (res.statusCode == 200) {
          const achar_info = JSON.parse(res.body);
          console.log(achar_info.name);
        } else {
          console.log('error code :', res.statusCode);
        }
      }
    } else {
      console.log('error code :', res.statusCode);
    }
  } catch (err) {
    console.log(err);
  }
}

getCharacters();

// const request = require('request');

// const movie_id = process.argv[2];

// let used_url = 'https://swapi-api.alx-tools.com/api/films/' + movie_id;

// request.get(used_url, (err, res, body) => {
//   if (err) {
//     console.log(err);
//     return;
//   } else if (res.statusCode == 200) {
//     body = JSON.parse(body);
//     let chars = body.characters;
//     for (let i = 0; i < chars.length; i++) {
//       const achar = chars[i];
//       request.get(achar, (err, res, body) => {
//         if (err) {
//           console.log(err);
//           return;
//         } else if (res.statusCode == 200) {
//           const achar_info = JSON.parse(body);
//           console.log(achar_info.name);
//         } else console.log('error code :', res.statusCode);
//       });
//     }
//   } else console.log('error code :', res.statusCode);
// });
