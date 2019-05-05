'use strict';

module.exports = function (settings) {
  var localKey, value;/* Declare the variables because of 'strict' mode */
  localKey = settings.localStorage || "";/*retrieve the key to look for*/
  value = window.localStorage.getItem(localKey);
  value == null ? value = '' : value = value;/* make sure that we return a string*/
  return value;
};
