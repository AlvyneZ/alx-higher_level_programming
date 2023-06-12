#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
}
let str = '';
for (let i = 0; i < process.argv[2]; i++) {
  str = str + 'X';
}
for (let i = 0; i < process.argv[2]; i++) {
  console.log(str);
}
