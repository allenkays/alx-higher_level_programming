#!/usr/bin/node
function factorialize (num) {
  if (num === 0 || isNaN(num)) {
    return 1;
  } else {
    return (num * factorialize(num - 1));
  }
}
const result = factorialize(parseInt(process.argv[2]));
console.log(result);
