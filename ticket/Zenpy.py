# Zenpy accepts an API token
creds = {
    'email' : 'nikhilmp448@gmail.com',
    'token' : 'U5clw0A2eOmJUKFLbfiaDxEoffE22MTTWx39b9Am',
    'subdomain': 'sample5751'
}


# Or a password
creds = {
    'email' : 'nikhilmp448@gmail.com',
    'password' : 'nikhil@2020',
    'subdomain': 'sample5751'
}

# Import the Zenpy Class
from zenpy import Zenpy
import requests

# Default
zenpy_client = Zenpy(**creds)

# Alternatively you can provide your own requests.Session object
zenpy_client = Zenpy(**creds, session=requests.Session())

# If you are providing your own HTTPAdapter object, Zenpy provides defaults via the
# Zenpy.http_adapter_kwargs() method. You can choose to use these defaults like so:
# session = requests.Session()
# session.mount('https://sample5751.zendesk.com/', MyAdapter(**Zenpy.http_adapter_kwargs()))
# zenpy_client = Zenpy(**creds, session=requests.Session())


