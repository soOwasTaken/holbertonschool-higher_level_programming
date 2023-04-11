#!/usr/bin/node
const arg = process.argv[2];
const int = parseInt(arg);
if (isNaN(int)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${int}`);
}
