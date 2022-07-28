#!/usr/bin/node
const request = require('request');
const id = Number(process.argv[2]);

function printExactList (array, idx) {
  if (idx === array.length) {
    return;
  }
  request(array[idx], function (error, response, body) {
    if (error) {
      return;
    }
    console.log(JSON.parse(body).name);
    printExactList(array, idx + 1);
  });
}

request(`https://swapi-api.hbtn.io/api/films/${id}`, function (error, response, body) {
  if (error) {
    return;
  }
  const characters = JSON.parse(body).characters;
  printExactList(characters, 0);
});
