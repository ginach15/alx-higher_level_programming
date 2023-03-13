#!/usr/bin/node
// prints "My number: <first argument converted in integer>" if first argument could be converted to an integer
const args = process.argv;
const number = parseInt(args[2]);
if (isNaN(number)) {
  console.log('Not a number');
} else { console.log('My number: ' + number); }
