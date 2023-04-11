#!/usr/bin/node
const c_is_fun = 'C is fun';
const arg = process.argv[2];
const int = parseInt(arg);
if (isNaN(int)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < int; i++) {
    console.log(c_is_fun);
  }
}
