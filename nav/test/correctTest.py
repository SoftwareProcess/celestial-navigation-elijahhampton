""" 
Created on April 1, 2019

@author Elijah Hampton
- self.setParm on all
- result = self.microservice() get result from micro
- resultDictionary = self.string2dict(result) turn result to dict
- self.assertEqual(func(self.inputDict), resultDict) test results
"""

import unittest
import httplib
from urllib import urlencode
import json
from nav.correct import correct
#from jinja2.utils import missing


class corrrectTest(unittest.TestCase):

    def setUp(self):
        self.inputDictionary = {}
        self.errorKey = "error"
        self.solutionKey = "probability"
        self.BX_PATH = '/nav?'
        self.BX_PORT = 5000
        self.BX_URL = 'localhost'

    def tearDown(self):
        self.inputDictionary = {}
        
    def setParm(self, key, value):
        self.inputDictionary[key] = value
    
    def microservice(self):
        try:
            theParm = urlencode(self.inputDictionary)
            theConnection = httplib.HTTPConnection(self.BX_URL, self.BX_PORT)
            theConnection.request("GET", self.BX_PATH + theParm)
            theStringResponse = theConnection.getresponse().read()
            return theStringResponse
        except Exception as e:
            return "error encountered during transaction"
        
    def string2dict(self, httpResponse):
        '''Convert JSON string to dictionary'''
        result = {}
        try:
            jsonString = httpResponse.replace("'", "\"")
            unicodeDictionary = json.loads(jsonString)
            for element in unicodeDictionary:
                if(isinstance(unicodeDictionary[element],unicode)):
                    result[str(element)] = str(unicodeDictionary[element])
                else:
                    result[str(element)] = unicodeDictionary[element]
        except Exception as e:
            result['diagnostic'] = str(e)
        return result
#     -----------------------------------------------------------------------
#     Acceptance Tests
                
#                          
#       Sad path analysis:      

#Happy Path Test

         
#Sad Path Test
    def test200_010LatParmShouldBeGreaterThan90d0(self):
        self.setParm('op', 'correct')
        self.setParm('lat', '90d0.0')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('assumedLong', '350d35.3')
         
        tempResultDict = {'op': 'correct',
                          'lat': '90d0.0',
                          'long': '95d41.6',
                          'altitude': '13d42.3',
                          'assumedLat': '53d38.4',
                          'assumedLong': '350d35.3',
                          'error': 'invalid lat'}
         
        self.assertEqual(correct(self.inputDictionary),tempResultDict)
    
    def test200_020ShouldReturnAppropriateErrorIfLatParmIsNotPresent(self):
        self.setParm('op', 'correct')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('assumedLong', '350d35.3')
        
        tempResultDict = {'op': 'correct',
                          'long': '95d41.6',
                          'altitude': '13d42.3',
                          'assumedLat': '53d38.4',
                          'assumedLong': '350d35.3',
                          'error': 'lat parm not present in input dict.'}
        
        self.assertEqual(correct(self.inputDictionary), tempResultDict);