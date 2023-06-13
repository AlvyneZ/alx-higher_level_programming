#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let num = 0;
  list.forEach((item) => {
    if (item === searchElement) {
      num += 1;
    }
  });
  return num;
};
