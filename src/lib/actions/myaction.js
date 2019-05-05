'use strict';

module.exports = function (settings, event) {
  var myGlobalSetting; /*we have to declare all of the variables because of strict mode*/
  myGlobalSetting = turbine.getExtensionSettings().action;/*retrieving the global config*/
  if (myGlobalSetting == true || myGlobalSetting == "true") {/*If it is true*/
    console.log('Rule ID : ' + event.$rule.id);
    console.log('Rule Name : ' + event.$rule.name);
  }
  else {
    turbine.logger.info('Rule ID : ' + event.$rule.id);
    turbine.logger.info('Rule Name : ' + event.$rule.name);
  }
};
