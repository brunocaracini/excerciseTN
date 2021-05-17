import pytest
import unittest
from classes import Shipment
from controller import Controller


class TestShipments(unittest.TestCase):
    """ Class that contains the methods to run the Unit Tests """

    def test_same_shipping_cost_same_delivery_date(self):
        
        #Arrange
        shipment1 = Shipment('Option_1','Delivery',10,2)
        shipment2 = Shipment('Option_2','Delivery',10,2)
        shipments = [shipment1,shipment2]
        esperado = [shipment1.name,shipment2.name]

        #Act
        result = Controller.get_shipments(shipments,True)
        
        #Assert
        assert(result == esperado)
    
    def test_same_shipping_cost_different_delivery_date(self):
        
        #Arrange
        shipment1 = Shipment('Option_1','Delivery',10,4)
        shipment2 = Shipment('Option_2','Delivery',10,2)
        shipments = [shipment1,shipment2]
        esperado = [shipment2.name,shipment1.name]

        #Act
        result = Controller.get_shipments(shipments,True)
        
        #Assert
        assert(result == esperado)

    def test_different_shipping_cost_same_delivery_date(self):
        
        #Arrange
        shipment1 = Shipment('Option_1','Delivery',10,4)
        shipment2 = Shipment('Option_2','Delivery',9,4)
        shipments = [shipment1,shipment2]
        esperado = [shipment2.name,shipment1.name]

        #Act
        result = Controller.get_shipments(shipments,True)
        
        #Assert
        assert(result == esperado)
    
    def test_different_shipping_cost_different_delivery_date(self):
        
        #Arrange
        shipment1 = Shipment('Option_1','Delivery',10,2)
        shipment2 = Shipment('Option_2','Delivery',9,4)
        shipment3 = Shipment('Option_2','Delivery',9,2)
        shipments = [shipment1,shipment2,shipment3]
        esperado = [shipment3.name,shipment2.name,shipment1.name]
        
        #Act
        result = Controller.get_shipments(shipments,True)
        
        #Assert
        assert(result == esperado)
    
    def test_no_options(self):
        
        #Arrange
        shipments = []
        esperado = []
        
        #Act
        result = Controller.get_shipments(shipments,True)
        
        #Assert
        assert(result == esperado)

    def test_error_and_exceptions_handling(self):
        
        #Arrange
        shipments = 'This is going to fail'
        
        #Act
        with self.assertRaises(Exception) as e:
             result = Controller.get_shipments(shipments,True)
        
        #Assert
        assert(e)