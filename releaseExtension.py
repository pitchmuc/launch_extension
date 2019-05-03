# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 14:18:30 2019

@author: piccini
"""

import time as _time
import json as _json
## Non standard libraries
import requests as _requests
import jwt as _jwt
from pathlib import Path
import zipfile

### Set up default values
_org_id, _api_key, _tech_id, _pathToKey, _secret = "","","","","",
_TokenEndpoint = "https://ims-na1.adobelogin.com/ims/exchange/jwt"
_orga_admin ={'_org_admin','_deployment_admin','_support_admin'}
_cwd = Path.as_posix(Path.cwd())
_date_limit = 0
_token = ''
_packageID = ''

def createConfigFile(verbose=False):
    """
    This function will create a 'config_admin.json' file where you can store your access data. 
    """
    json_data = {
        'org_id': '<orgID>',
        'api_key': "<APIkey>",
        'tech_id': "<something>@techacct.adobe.com",
        'secret': "<YourSecret>",
        'pathToKey': '<path/to/your/privatekey.key>',
        'packageID' : '<YourExtensionID>'
    }
    with open('config_admin.json', 'w') as cf:
        cf.write(_json.dumps(json_data, indent=4))
    if verbose:
        print(' file created at this location : '+_cwd + '/config_admin.json')


def importConfigFile(file):
    """
    This function will read the 'config_admin.json' to retrieve the information to be used by this module. 
    """
    global _org_id
    global _api_key
    global _tech_id
    global _pathToKey
    global _secret
    global _packageID
    global _endpoint
    with open(file, 'r') as file:
        f = _json.load(file)
        _org_id = f['org_id']
        _api_key = f['api_key']
        _tech_id = f['tech_id']
        _secret = f['secret']
        _pathToKey = f['pathToKey']
        _packageID = f['packageID']
        _endpoint = _endpoint + _packageID

#### Launch API Endpoint
_endpoint = 'https://reactor.adobe.io/extension_packages/' #+PackageID

    
def retrievingToken(verbose=False):
    """ Retrieve the token by using the information provided by the user during the import importConfigFile function. 
    
    Argument : 
        verbose : OPTIONAL : Default False. If set to True, print information.
    """
    with open(_pathToKey, 'r') as f:
        private_key_unencrypted = f.read()
        header_jwt = {'cache-control':'no-cache','content-type':'application/x-www-form-urlencoded'}
    jwtPayload = {
        "exp": round(24*60*60+ int(_time.time())),###Expiration set to 24 hours
        "iss": _org_id, ###org_id
        "sub": _tech_id,###technical_account_id
        "https://ims-na1.adobelogin.com/s/ent_user_sdk": True,
        "https://ims-na1.adobelogin.com/s/ent_analytics_bulk_ingest_sdk": True,
        "https://ims-na1.adobelogin.com/s/ent_reactor_admin_sdk":True,
        "aud": "https://ims-na1.adobelogin.com/c/"+_api_key
    }
    encoded_jwt = _jwt.encode(jwtPayload, private_key_unencrypted , algorithm='RS256')##working algorithm
    payload = {
            "client_id":_api_key,
            "client_secret":_secret,
            "jwt_token" : encoded_jwt.decode("utf-8")
            }
    response = _requests.post(_TokenEndpoint, headers=header_jwt, data=payload)
    json_response = response.json()
    token = json_response['access_token']
    expire = json_response['expires_in']
    global _date_limit ## getting the scope right
    _date_limit= _time.time()+ expire/1000 -500 ## end of time for the token
    with open('token.txt','w') as f: ##save the token
        f.write(token)
    if verbose == True:
        print('token valid till : ' + _time.ctime(_time.time()+ expire/1000))
        print('token has been saved here : ' + Path.as_posix(Path.cwd()))
    return token


def releaseExtension():
    """ It will release the extension privately. To be used only once """
    token = retrievingToken()
    header = {'accept':'application/vnd.api+json;revision=1',
              'content-type':'application/vnd.api+json',
              'Authorization':'Bearer '+token,
              'cache-control': 'no-cache',
              'x-api-key': 'Activation-DTM'
              }
    data = {
        "data": {
            "id": _packageID,
            "type": "extension_packages",
            "meta": {
                "action": "release_private"
            }
        }
    }
    res = _requests.patch(_endpoint,headers=header,json=data)
    return res 


importConfigFile('config_multi_services.json')
res = releaseExtension()
print(res.text)