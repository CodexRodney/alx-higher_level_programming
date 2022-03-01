#!/usr/bin/node
let squareFormat = '';
const sizeSquare = parseInt(process.argv[2]);
if (isNaN(sizeSquare) === true) {
  console.log('Missing size');
}
for (let i = 0; i < sizeSquare; i++) {
  squareFormat += 'X';
}
for (let z = 0; z < sizeSquare; z++) {
  console.log(squareFormat);
}
