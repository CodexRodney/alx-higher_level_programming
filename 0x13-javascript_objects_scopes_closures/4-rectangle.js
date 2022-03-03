#!/usr/bin/node
module.exports = class Rectangle {
  width;
  height;
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    let x = '';
    for (let i = 0; i < this.width; i++) {
      x += 'X';
    };
    for (let z = 0; z < this.height; z++) {
      console.log(x);
    }
  };
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  };
  double () {
    this.width *= 2;
    this.height *= 2;
  }
};
