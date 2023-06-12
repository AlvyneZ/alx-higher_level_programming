#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const list = process.argv.sort();
  console.log(list.reverse()[1]);
}
