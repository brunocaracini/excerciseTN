from flask.app import Flask
from data import Data
from classes import Shipment

class Controller:
    ''' Class that manage the logic of the application'''
    
    shipments = []

    @classmethod
    def get_shipments(cls,val=False,test_mode=False):
        '''
        Manage the logic of the API.
        Returns the shipments options avialable sorted by cost and estimated days.
        '''
        try:
            #Check if there are pre-set values for shipments
            if val == False:
                #If there are not, call the initial values method to make the request.
                cls.set_shipments_initial_val()
            else:
                #If there are, call the initial values to assign this values to class variable.
                cls.set_shipments_initial_val(val)
            
            #Check if there are options available. If there are not, the list will be empty.     
            if len(cls.shipments) == 0:
                #If list is empty, return the empty list.
                return cls.shipments
            else:
                #If it is not, call the order method, to order the shipments.
                cls.order_shipments()
                
                #Check if we are in test mode to define what the method will return
                if test_mode:
                    #If we are in test mode, return list of options names, to compare results during Unit Testting execution.
                    return [x.name for x in cls.shipments]
                else:
                    #If not, call the method to re-convert the data into a Json to be returned as API response.
                    return cls.map_class_into_json()
        except Exception as e:
            raise e

    @classmethod
    def set_shipments_initial_val(cls,val=False):
        """Sets the initial value of class variable shipments. If there are pre-set values, the method assign them to class variable, 
           if there are not, it makes the request to obtain the data.
        """

        #Check if there are pre-set values
        if val == False:
            #If there are not, make the request and call the method to map the json objects into Python Shipment class.
            Data.set_url('https://shipping-options-api.herokuapp.com/v1/shipping_options')
            Data.make_request()
            cls.shipments = cls.parse_into_ship_class(Data.response)
        else:
            #If there are, assign them to class variable that contains shipments
            cls.shipments = val

    @classmethod
    def parse_into_ship_class(cls, shipments):
        """Maps the json response of the API into Shipment Python Class"""
        try:
            shipments = shipments['shipping_options']
            #Check if there are options available.
            if len(shipments) > 0:
                #If there are, it converts the data into Shipments Python class.
                return [Shipment(x['name'],x['type'],x['cost'],x['estimated_days']) for x in shipments]
            else:
                #If there are not, it returns an empty list.
                return []
        except Exception as e:
            raise e

    @classmethod
    def order_shipments(cls):
        """ Orders the shipments based on cost and estimated days """
        cls.shipments = sorted(cls.shipments, key = lambda x: (x.cost, x.estimated_days))
    
    @classmethod
    def map_class_into_json(cls):
        """Maps the Python API classes into a Dictionary"""
        return [{'name':x.name,'type':x.type,'cost':x.cost,'estimated_days':x.estimated_days} for x in cls.shipments]


