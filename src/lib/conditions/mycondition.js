'use strict';

module.exports = function (settings) {
  var myGlobalSetting, myCondition; /* Declare the variables because of 'strict' mode */
  myGlobalSetting = turbine.getExtensionSettings().condition; /* retrieve the localStorage key */
  myCondition = settings.value; /* retrieve the value to compare */

  if (window.localStorage.getItem(myGlobalSetting) == myCondition) {
    return true
  }
  else {
    turbine.logger.info('The condition is "' + myCondition + '" and the localStorage is "' + window.localStorage.getItem(myGlobalSetting) + '"')
    return false
  }
};
