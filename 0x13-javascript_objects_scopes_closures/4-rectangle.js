#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || !w || !h) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

    rotate () {
	const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width *= 4;
    this.heigth *= 4;
  }
}

module.exports = Rectangle;
