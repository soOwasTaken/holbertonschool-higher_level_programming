#!/usr/bin/node
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
let x = 0;
function add (a, b) {
  return a + b;
}
if (isNaN(b)) {
  console.log('NaN');
} else {
  x = add(a, b);
  console.log(x);
}
