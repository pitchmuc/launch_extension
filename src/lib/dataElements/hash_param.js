'use strict';

module.exports = function (settings) {
    var globalParam, settingKey, url, split_url, array_url, value;/* Declare the variables because of 'strict' mode */
    globalParam = turbine.getExtensionSettings().dataElements
    settingKey = settings.hashParam;
    url = window.location.href;
    value = '';
    if (url.indexOf(globalParam) != -1) {/* if the parameter exists in the url */
        split_url = url.split(globalParam)[1]
        if (globalParam != '&' && split_url.indexOf('&') != -1) {/*if the parameter is not the amper and the amper is in the url*/
            array_url = split_url.split('&')[1]/* create an array of different key value pairs*/
            array_url.forEach(function (element) {
                if (element.indexOf(settingKey) > -1) {/* if the key is in the url * /
                    value = element.split('=')[1]/* take the 2nd part of the key value pair*/
                }
            });

        } else {/* if the param is the only parameter*/
            if (split_url.indexOf(settingKey) != -1) {/* if the key is in the url*/
                value = split_url.split('=')[1]/* take the 2nd part of the key value pair*/
            }
        }

    }
    return value;
};
