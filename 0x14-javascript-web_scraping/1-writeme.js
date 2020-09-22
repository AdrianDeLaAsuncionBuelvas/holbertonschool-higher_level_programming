#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv[2], 'utf8', process.argv[3], error => {
  if (error) console.log(error);
});
