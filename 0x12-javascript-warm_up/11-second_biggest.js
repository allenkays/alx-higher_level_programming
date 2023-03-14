#!/usr/bin/node
const myVar = [];
for (let i = 2; i < process.argv.length; i++) {
  myVar.push(parseInt(process.argv[i]));
}
const myVar2 = myVar.sort();
console.log(myVar2[myVar2.length - 2]);
