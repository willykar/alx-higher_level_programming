#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const uniqVal = [...new Set(vals)];
const newDict = {};
for (const i in uniqVal) {
  const list = [];
  for (const j in totalist) {
    if (totalist[j][i] === uniqVal[j]) {
      list.unshift(totalist[j][0]);
    }
  }
  newDict[uniqVal[i]] = list;
}
console.log(newDict);
