'use strict';

module.exports = function (settings, trigger) {
  var myEventConfig;
  myEventConfig = turbine.getExtensionSettings().event;/* retrieve my configuration for my event listening */
  window.addEventListener(myEventConfig, function (elem) {
    trigger({ element: elem })/* passing the element that trigger the event*/
  })
};
