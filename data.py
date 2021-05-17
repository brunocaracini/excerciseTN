import requests
import json

class Data:
    ''' 
    Class that manage the connections with the API to obtain the data.
    '''
    url = None
    response = None

    @classmethod
    def make_request(cls):
        r = requests.get(cls.url)
        r = json.loads(r.text)
        cls.response = r
    
    @classmethod
    def set_url(cls,url):
        cls.url = url

if __name__ == '__main__':
    Data.set_url('https://shipping-options-api.herokuapp.com/v1/shipping_options')
    Data.make_request()
    print(Data.response)