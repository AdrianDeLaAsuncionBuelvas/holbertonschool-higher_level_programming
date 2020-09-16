#!/usr/bin/node
const first = Number(process.argv[2]);
const second = Number(process.argv[3]);
if (isNaN(fisrt) || isNaN(second)) {
    console.log('NaN');
} else {
    console.log(add(first, second));
}

function add (a, b) {
    return a + b;
}
