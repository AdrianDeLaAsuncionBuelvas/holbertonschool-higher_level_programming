#!/usr/bin/node

let i, j;
let newstr = '';

if (process.argv.length <= 2) {
  console.log('Missing size');
} else {
  for (i = 0; i < process.argv[2]; i++) {
    newstr += 'X';
  }
  for (j = 0; j < process.argv[2]; j++) {
    console.log(newstr);
  }
}
