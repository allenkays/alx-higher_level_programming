#!/usr/bin/node
function add (a, b) {
  return (parseInt(a) + parseInt(b));
}
const myVar = (add(process.argv[2], process.argv[3]));
console.log(myVar);
