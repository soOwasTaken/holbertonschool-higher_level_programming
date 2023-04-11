#!/usr/bin/node
const args = process.argv.slice(2);
const nums = args.map(num => parseInt(num));

if (nums.length <= 1) {
  console.log('0');
} else {
  const sortedNums = nums.sort((a, b) => b - a);
  console.log(sortedNums[1]);
}
