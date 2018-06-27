import requests
from bs4 import BeautifulSoup
import namesilo.errors as nserrors

class NameSiloAPI(object):

    LIVE_BASE_URL = 'https://www.namesilo.com/api/'
    SANDBOX_BASE_URL = 'http://sandbox.namesilo.com/api/'

    NAMESILO_OPERATIONS = {
        'add_account_funds': 'addAccountFunds',
        'add_auto_renew': 'addAutoRenewal',
        'add_contact': 'contactAdd',
        'add_dns_record': 'dnsAddRecord',
        'add_email_forward': 'configureEmailForward',
        'add_portfolio': 'portfolioAdd',
        'add_privacy': 'addPrivacy',
        'add_registered_nameserver': 'addRegisteredNameServer',
        'associate_contact': 'contactDomainAssociate',
        'associate_portfolio': 'portfolioDomainAssociate',
        'change_nameservers': 'changeNameServers',
        'check_register_availability': 'checkRegisterAvailability',
        'check_transfer_availability': 'checkTransferAvailability',
        'check_transfer_status': 'checkTransferStatus',
        'delete_dns_record': 'dnsDeleteRecord',
        'delete_portfolio': 'portfolioDelete',
        'delete_registered_nameserver': 'deleteRegisteredNameServer',
        'forward_domain': 'domainForward',
        'get_account_balance': 'getAccountBalance',
        'get_auth_code': 'retrieveAuthCode',
        'get_domain_info': 'getDomainInfo',
        'list_contacts': 'contactList',
        'list_dns_records': 'dnsListRecords',
        'list_domains': 'listDomains',
        'list_email_forwards': 'listEmailForwards',
        'list_portfolios': 'portfolioList',
        'list_registered_nameservers': 'listRegisteredNameServers',
        'lock_domain': 'domainLock',
        'register_domain': 'registerDomain',
        'renew_domain': 'renewDomain',
        'remove_auto_renewal': 'removeAutoRenewal',
        'remove_email_forward': 'deleteEmailForward',
        'remove_privacy': 'removePrivacy',
        'transfer_domain': 'ransferDomain',
        'unlock_domain': 'domainUnlock',
        'update_contact': 'contactUpdate',
        'update_dns_record': 'dnsUpdateRecord',
        'update_portfolio': 'portfoliopdate',
        'update_registered_nameserver': 'modifyRegisteredNameServer'
    }

    def __init__(self, apiKey=None, live=True):
        self.apiKey = apiKey
        self.baseUri = self.LIVE_BASE_URL if live else self.SANDBOX_BASE_URL

        if self.apiKey is None:
            raise ValueError('No Api Key present')

        self.params = {
            'version': 1,
            'type': 'xml',
            'key': self.apiKey
        }
    
    def request(self, operation, **kwargs):
        operation = self.NAMESILO_OPERATIONS.get(operation, operation)
        data = self.params

        if not kwargs:
            raise ValueError('No arguments provided.')
        
        for key, value in kwargs.items():
            data[key] = value
        
        result = requests.get(self.baseUri + operation, params=data)
        soup = BeautifulSoup(result.content, 'lxml-xml')
        self.handle_error(soup)

        return soup

    def handle_error(self, soup):
        code = soup.namesilo.reply.code
        print(code.string)
        if code.string in nserrors.NAMESILO_ERRORS:
            error = nserrors.NAMESILO_ERRORS[code.string]
            detail = soup.namesilo.reply.detail
            raise error(detail.string)

    def checkRegisterAvailability(self, *domains):
        data = self.params
        query = ""

        if not domains:
            raise ValueError('No domains provided to lookup')
        
        for domain in domains:
            if domains.index(domain) != len(domains) - 1: # Checking for last element here
                query += domain + ","
            else:
                query += domain
        
        data['domains'] = query
        print(data) # Debug

        result = requests.get(self.baseUri + "checkRegisterAvailability", params=data)
        soup = BeautifulSoup(result.content, 'lxml-xml')
        self.handle_error(soup)

        return soup
    
    


        
        

    

