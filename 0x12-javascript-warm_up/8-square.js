#!/usr/bin/node
// prints a square
const sqSize = parseInt(process.argv[2]);
if (isNaN(sqSize)) {
  console.log('Missing size');
} else { for (let i = 0; i < sqSize; i++) { console.log('X'.repeat(sqSize)); } }
