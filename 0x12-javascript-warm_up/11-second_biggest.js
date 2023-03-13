#!/usr/bin/node
// prints the second biggest integer in list of arguments
let args = process.argv.slice(2);
if (args.length <= 1) {
  console.log('0');
} else {
  let intArr = args.map(s => parseInt(s));
  let sortedArr = intArr.sort((a, b) => a - b);
  let setValues = new Set(sortedArr);
  let sortedValues = Array.from(setValues);
  console.log(sortedValues[sortedValues.length - 2]);
}
