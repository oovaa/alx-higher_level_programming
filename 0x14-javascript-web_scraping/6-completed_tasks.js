#!/usr/bin/node

// @ts-check

const request = require('request');

const used_url = process.argv[2];

request.get(used_url, (err, res, body) => {
  if (err) {
    console.log(err);
    return;
  } else if (res.statusCode == 200) {
    const data_list = JSON.parse(body);
    console.log(data_list);
    let users_tasks = {};
    for (let i = 0; i < data_list.length; i++) {
      const element = data_list[i];
      const key = element.userId;
      if (element.completed == true) {
        if (!users_tasks[key]) users_tasks[key] = 0;
        users_tasks[key] = users_tasks[key] + 1;
      }
    }
    console.log(users_tasks);
  } else console.log('error code :', res.statusCode);
});
