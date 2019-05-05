'use strict';
var getTracker, myPromise, sharedMod;/* because of strict mode, we have to declare the variable */
getTracker = turbine.getSharedModule('adobe-analytics', 'get-tracker') /* get the shared module from Adobe Analytics */
if (typeof getTracker != 'undefined') { /* if shared module doesn't exist, it return undefined */
    getTracker().then(function (tracker) { /** here the module is a promise (see docu) */
        turbine.logger.info('tracker has been set');
        turbine.logger.info(tracker);
    })
}
turbine.logger.info('Out of the sharedExtension');/** in order to inform that our shared module script has ran */
myPromise = require('@adobe/reactor-promise'); /* creating my shared Module function by calling the promise wrapper */
sharedMod = new myPromise(function (resolve, reject) {
    resolve('mySharedModule')
});
module.exports = { 'ags862': sharedMod };/* exporting the module, exposing it */
