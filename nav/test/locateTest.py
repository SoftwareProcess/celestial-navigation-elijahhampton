""" 
Created on March 04, 2019

@author Elijah Hampton
"""

from nav.locate import locate
import unittest
from urllib import urlencode
import httplib
import json
from jinja2.utils import missing

class locateTest(unittest.TestCase):

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
    
#     ----------------------------------------------------------------------

#         self.setParm('assumedLat', '-53d38.4')
#         self.setParm('assumedLong', '350d35.3')
#         self.setParm('corrections', '[[100,1d0.0]]')
#         self.setParm('op', 'locate')

# Happy Path Test


# Sad Path Test
    def test200_010ShouldReturnWithErrorKeyIfXOfAssumedLatIsLTNegNinety(self):
        self.setParm('assumedLat', '-91d38.4')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('corrections', '[[100,1d0.0]]')
        self.setParm('op', 'locate')
          
        tempResultDict = {'op': 'locate',
                          'assumedLat': '-91d38.4',
                          'assumedLong': '350d35.3',
                          'corrections': '[[100,1d0.0]]',
                          'error': 'assumedLat parm outside correct boundary.'}
         
        self.assertEqual(locate(self.inputDictionary), tempResultDict)
        
    def test200_010ShouldReturnWithErrorKeyIfXOfAssumedLatIsGTNinety(self):
        self.setParm('assumedLat', '91d38.4')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('corrections', '[[100,1d0.0]]')
        self.setParm('op', 'locate')
          
        tempResultDict = {'op': 'locate',
                          'assumedLat': '91d38.4',
                          'assumedLong': '350d35.3',
                          'corrections': '[[100,1d0.0]]',
                          'error': 'assumedLat parm outside correct boundary.'}
         
        self.assertEqual(locate(self.inputDictionary), tempResultDict)
        
    def test200_010ShouldReturnWithErrorKeyIfYOfAssumedLatIsLTZero(self):
        self.setParm('assumedLat', '-53d-5.1')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('corrections', '[[100,1d0.0]]')
        self.setParm('op', 'locate')
          
        tempResultDict = {'op': 'locate',
                          'assumedLat': '-53d-5.1',
                          'assumedLong': '350d35.3',
                          'corrections': '[[100,1d0.0]]',
                          'error': 'assumedLat parm outside correct boundary.'}
         
        self.assertEqual(locate(self.inputDictionary), tempResultDict)
        
    def test200_010ShouldReturnWithErrorKeyIfYOfAssumedLatIsGT59(self):
        self.setParm('assumedLat', '-53d361.1')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('corrections', '[[100,1d0.0]]')
        self.setParm('op', 'locate')
          
        tempResultDict = {'op': 'locate',
                          'assumedLat': '-53d361.1',
                          'assumedLong': '350d35.3',
                          'corrections': '[[100,1d0.0]]',
                          'error': 'assumedLat parm outside correct boundary.'}
         
        self.assertEqual(locate(self.inputDictionary), tempResultDict)
        
    def test200_010ShouldReturnWithErrorKeyIfXOfAssumedLatIsNotInteger(self):
        self.setParm('assumedLat', '-53.2d0.0')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('corrections', '[[100,1d0.0]]')
        self.setParm('op', 'locate')
          
        tempResultDict = {'op': 'locate',
                          'assumedLat': '-53.2d0.0',
                          'assumedLong': '350d35.3',
                          'corrections': '[[100,1d0.0]]',
                          'error': 'Found parm with wrong type (correct: integer).'}
         
        self.assertEqual(locate(self.inputDictionary), tempResultDict)
        