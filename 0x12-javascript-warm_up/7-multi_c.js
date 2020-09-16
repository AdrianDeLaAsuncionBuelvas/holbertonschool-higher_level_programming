#!/usr/bin/node

let i;
if (process.argv.length <= 2) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < process.argv[2]; i++) {
    if (i < 0) {
      break;
    } else {
      console.log('C is fun');
    }
  }
}
