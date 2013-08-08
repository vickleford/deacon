import keyring
import requests
import json

from sys import argv

url = 'https://identity.api.rackspacecloud.com/v2.0/tokens'

def get_auth(pyrax_environment):
    """Return an auth token.
    
    Piggybacks off the pyrax environments you have set up in keyring.
    """

    api_key = keyring.get_password('pyrax', pyrax_environment)
    
    headers = {'Content-Type': 'application/json'}
    payload = {
                'auth': {
                    'RAX-KSKEY:apiKeyCredentials': {
                        'username': pyrax_environment,
                        'apiKey': api_key
                    }
                 }
               }
                  
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    
    return r.json()

# just make one call.
response = get_auth('actionlogs')
    
    
def get_token():
    ''''Return a token.'''
    
    return response['access']['token']['id']
    
    
def get_endpoint():
    '''Return the MaaS endpoint.'''
    
    for endpoints in response['access']['serviceCatalog']:
        if endpoints['name'] == 'cloudMonitoring':
            return endpoints['endpoints'][0]['publicURL']
    
    
token = get_token()
endpoint = get_endpoint()