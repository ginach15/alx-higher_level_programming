#!/usr/bin/node
// defines a function which adds 2 integers and script prints the sum

function add (a, b) { return a + b; }

const firstInt = parseInt(process.argv[2]);
const secondInt = parseInt(process.argv[3]);

console.log(add(firstInt, secondInt));
