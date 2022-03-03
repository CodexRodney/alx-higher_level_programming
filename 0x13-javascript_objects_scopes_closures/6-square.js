#!/usr/bin/node
module.exports = class Square extends require('./5-square.js') {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let shapechar = '';
      for (let i = 0; i < this.width; i++) {
        shapechar += String(c);
      }
      for (let z = 0; z < this.height; z++) {
        console.log(shapechar);
      }
    }
  }
};
