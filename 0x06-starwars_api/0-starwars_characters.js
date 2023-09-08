#!/usr/bin/node

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
const request = require('request');
let characters = [];

request(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const movie = JSON.parse(body);
    characters = movie.characters;
    getName(0);
  }
});

function getName (index) {
  if (index === characters.length) {
    return;
  }

  request(characters[index], (err, response, body) => {
    if (!err && response.statusCode === 200) {
      const character = JSON.parse(body);
      console.log(character.name);
      getName(++index);
    }
  });
}
