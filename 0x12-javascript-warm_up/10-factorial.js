#!/usr/bin/node
// computes and prints a factorial
function factorial (n) { if (n === 1) { return (1); } else { return (n * factorial(n - 1)); } }

const i = parseInt(process.argv[2]);
if (isNaN(i)) { console.log(factorial(1)); } else { console.log(factorial(i)); }
