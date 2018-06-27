import requests
from bs4 import BeautifulSoup

class NameSiloAPI(object):

    def __init__(self, apiKey=None):
        self.apiKey = apiKey
        self.baseUri = "https://www.namesilo.com/api/"

        if self.apiKey is None:
            raise ValueError('No Api Key present')

        self.params = {
            'version': 1,
            'type': 'xml',
            'key': self.apiKey
        }
    
    def checkRegisterAvailability(self, *domains):
        query = ""

        if not domains:
            raise ValueError('No domains provided to lookup')
        
        for domain in domains:
            if domains.index(domain) != len(domains) - 1: # Checking for last element here
                query += domain + ","
            else:
                query += domain
        
        self.params['domains'] = query
        print(self.params) # Debug

        result = requests.get(self.baseUri + "checkRegisterAvailability", params=self.params)
        soup = BeautifulSoup(result.content, 'lxml-xml')

        return soup
    
    


        
        

    

