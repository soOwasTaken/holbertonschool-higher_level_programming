#!/usr/bin/node

exports.converter = function (base) {
  return function (myConverter) {
    return myConverter.toString(base);
  };
};
