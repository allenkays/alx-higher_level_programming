#!/usr/bin/node

const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];

let movieCharacters = [];
const characterNames = {};
request({ url: url, json: true }, (err, response) => {
  if (err) {
    console.error(err);
  } else {
    movieCharacters = response.body.characters;
    for (const index of movieCharacters) {
      request(index, { json: true }, (err, response) => {
        if (err) {
          console.log(err);
        }
        getName(index, response.body.name);
      });
    }
  }
});

function getName (url, name) {
  characterNames[url] = name;
  if (Object.entries(characterNames).length === movieCharacters.length) {
    for (const idx of movieCharacters) {
      console.log(characterNames[idx]);
    }
  }
}
