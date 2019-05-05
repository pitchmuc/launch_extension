'use strict';

module.exports = function (settings) {
  var mysettings, value; /* declare the variables */
  mysettings = settings.sessionStorage || "";/* retrieve value set in the module configuration */
  value = window.sessionStorage.getItem(mysettings);
  value == null ? value = '' : value = value;/* make sure that we return a string*/
  return value; /*returning the value*/
};
