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
from jinja2.utils import missing


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
    def test200_000CorrectShouldReturnCorrectAzimuthandDistanceValues(self):
        self.setParm('op', 'correct')
        self.setParm('lat', '16d32.3')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('assumedLong', '350d35.3')
        
        tempResultDict = {'op': 'correct',
                          'lat': '16d32.3',
                          'long': '95d41.6',
                          'altitude': '13d42.3',
                          'assumedLat': '53d38.4',
                          'assumedLong': '350d35.3',
                          'correctedAzimuth': '262d55.6',
                          'correctedDistance': '104'}
        
        self.assertEqual(correct(self.inputDictionary),tempResultDict)
        
    def test200_001CorrectedDistanceAndCorrectedAzimuthShouldBeAddedToDictionaryAfterReturning(self):
        self.setParm('op', 'correct')
        self.setParm('lat', '16d32.3')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('assumedLong', '350d35.3')
        
        resultDict = correct(self.inputDictionary)
        
        doesContainKey = False
        
        if ('correctedAzimuth' in resultDict):
            doesContainKey = True
        
        if ('correctedDistance' in resultDict):
            doesContainKey = True
        
        self.assertEqual(doesContainKey, True)
        
    def test200_002CorrectedDistanceAndCorrectAzimuthShouldBeOverwrittenIfAlreadyInDictionary(self):
        self.setParm('op', 'correct')
        self.setParm('lat', '16d32.3')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('correctedDistance', '1')
        self.setParm('correctedAzimuth', '1')
        
        resultDict = correct(self.inputDictionary)
        
        tempResultDict = {'op': 'correct',
                          'lat': '16d32.3',
                          'long': '95d41.6',
                          'altitude': '13d42.3',
                          'assumedLat': '53d38.4',
                          'assumedLong': '350d35.3',
                          'correctedAzimuth': '262d55.6',
                          'correctedDistance': '104'}
        
        self.assertEqual(resultDict, tempResultDict)
         
#Sad Path Test
    def test200_010ShouldReturnAppropriateErrorIfLatParmIsLTNeg90OrGT90(self):
        self.setParm('op', 'correct')
        self.setParm('lat', '-300d0.0')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('assumedLong', '350d35.3')
          
        tempResultDict = {'op': 'correct',
                          'lat': '-300d0.0',
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
         
    def test200_010ShouldReturnAppropriateErrorIfLongParmMissing(self):
        self.setParm('op', 'correct')
        self.setParm('lat', '16d32.3')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('assumedLong', '350d35.3')
          
        tempResultDict = {'op': 'correct',
                          'lat': '16d32.3',
                          'altitude': '13d42.3',
                          'assumedLat': '53d38.4',
                          'assumedLong': '350d35.3',
                          'error': 'long parm not present in input dict.'}
          
        self.assertEqual(correct(self.inputDictionary),tempResultDict)
     
    def test200_010ShouldReturnWithErrorKeyIfLongParmXIfLT0OrGT360(self):
        self.setParm('op', 'correct')
        self.setParm('lat', '16d32.3')
        self.setParm('long', '370d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('assumedLong', '350d35.3')
          
        tempResultDict = {'op': 'correct',
                          'lat': '16d32.3',
                          'long': '370d41.6',
                          'altitude': '13d42.3',
                          'assumedLat': '53d38.4',
                          'assumedLong': '350d35.3',
                          'error': 'long parm outside correct boundary.'}
          
        self.assertEqual(correct(self.inputDictionary), tempResultDict)
         
    def test200_010ShouldReturnWithErrorKeyIfXOfAltitudeParmIsGT90OrLT0(self):
        self.setParm('lat', '16d32.3')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '400d42.3')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('op', 'correct')
          
        tempResultDict = {'op': 'correct',
                          'lat': '16d32.3',
                          'long': '95d41.6',
                          'altitude': '400d42.3',
                          'assumedLat': '53d38.4',
                          'assumedLong': '350d35.3',
                          'error': 'altitude parm outside correct boundary.'}
         
        self.assertEqual(correct(self.inputDictionary), tempResultDict)
         
    def test200_010ShouldReturnWithErrorKeyIfAltitudeIsNotPresent(self):
        self.setParm('lat', '16d32.3')
        self.setParm('long', '95d41.6')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('op', 'correct')
          
        tempResultDict = {'op': 'correct',
                          'lat': '16d32.3',
                          'long': '95d41.6',
                          'assumedLat': '53d38.4',
                          'assumedLong': '350d35.3',
                          'error': 'altitude parm not present.'}
         
        self.assertEqual(correct(self.inputDictionary), tempResultDict)
         
    def test200_010ShouldReturnWithErrorKeyIfXOfAssumedLatIsLTNegNinetyOrGTNinety(self):
        self.setParm('lat', '16d32.3')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '-200d38.4')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('op', 'correct')
          
        tempResultDict = {'op': 'correct',
                          'lat': '16d32.3',
                          'long': '95d41.6',
                          'altitude': '13d42.3',
                          'assumedLat': '-200d38.4',
                          'assumedLong': '350d35.3',
                          'error': 'assumedLat parm outside correct boundary.'}
         
        self.assertEqual(correct(self.inputDictionary), tempResultDict)
         
    def test200_010ShouldReturnWithErrorKeyIfAssumedLatParmNotPresent(self):
        self.setParm('lat', '16d32.3')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('op', 'correct')
          
        tempResultDict = {'op': 'correct',
                          'lat': '16d32.3',
                          'long': '95d41.6',
                          'altitude': '13d42.3',
                          'assumedLong': '350d35.3',
                          'error': 'assumedLat parm not present.'}
         
        self.assertEqual(correct(self.inputDictionary), tempResultDict)
         
    def test200_010ShouldReturnWithErrorKeyIfXOfAssumedLongParmIsLTZeroOrGT360(self):
        self.setParm('lat', '16d32.3')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('assumedLong', '500d35.3')
        self.setParm('op', 'correct')
          
        tempResultDict = {'op': 'correct',
                          'lat': '16d32.3',
                          'long': '95d41.6',
                          'altitude': '13d42.3',
                          'assumedLat': '53d38.4',
                          'assumedLong': '500d35.3',
                          'error': 'assumedLong parm outside correct boundary.'}
         
        self.assertEqual(correct(self.inputDictionary), tempResultDict)
         
    def test200_010ShouldReturnWithErrorKeyIfAssumedLongParmNotPresent(self):
        self.setParm('lat', '16d32.3')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('op', 'correct')
          
        tempResultDict = {'op': 'correct',
                          'lat': '16d32.3',
                          'long': '95d41.6',
                          'altitude': '13d42.3',
                          'assumedLat': '53d38.4',
                          'error': 'assumedLong parm not present.'}
         
        self.assertEqual(correct(self.inputDictionary), tempResultDict)
         
    def test200_010ShouldReturnWithErrorKeyIfXPortionOfLatLongAltitudeAssumedLatOrAssumedLongAreNonIntegers(self):
        self.setParm('lat', '16ad32.3')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('op', 'correct')
          
        tempResultDict = {'op': 'correct',
                          'lat': '16ad32.3',
                          'long': '95d41.6',
                          'altitude': '13d42.3',
                          'assumedLat': '53d38.4',
                          'assumedLong': '350d35.3',
                          'error': 'Found parm with wrong type (correct: integer).'}
         
        self.assertEqual(correct(self.inputDictionary), tempResultDict)
         
    def test200_010ShouldReturnWithErrorKeyIfYPortionOfLatLongAltitudeAssumedLatOrAssumedLongIsInCorrectBoundary(self):
        self.setParm('lat', '16d32.3')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('assumedLong', '350d70.3')
        self.setParm('op', 'correct')
          
        tempResultDict = {'op': 'correct',
                          'lat': '16d32.3',
                          'long': '95d41.6',
                          'altitude': '13d42.3',
                          'assumedLat': '53d38.4',
                          'assumedLong': '350d70.3',
                          'error': 'Found Parm with y portion outside of correct boundary.'}
         
        self.assertEqual(correct(self.inputDictionary), tempResultDict)
         
    def test200_010ShouldReturnWithErrorKeyIfYPortionOfLatLongAltitudeAssumedLatOrAssumedLongIsAFloatingPointValue(self):
        self.setParm('lat', '16d32.3')
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('assumedLong', '350d35.3a')
        self.setParm('op', 'correct')
          
        tempResultDict = {'op': 'correct',
                          'lat': '16d32.3',
                          'long': '95d41.6',
                          'altitude': '13d42.3',
                          'assumedLat': '53d38.4',
                          'assumedLong': '350d35.3a',
                          'error': 'Found parm with y.y portion as incorrect type. (correct: float)'}
         
        self.assertEqual(correct(self.inputDictionary), tempResultDict)
        
    def test200_010ShouldReturnAppropriateErrorIfResultDictContainsANonString(self):
        self.setParm('lat', 16d32.3)
        self.setParm('long', '95d41.6')
        self.setParm('altitude', '13d42.3')
        self.setParm('assumedLat', '53d38.4')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('op', 'correct')
        
        tempResultDict = {'op': 'correct',
                          'lat': 
        16d32.3,
                          'long': '95d41.6',
                          'altitude': '13d42.3',
                          'assumedLat': '53d38.4',
                          'assumedLong': '350d35.3',
                          'error': 'Result dict contains non string key or value.'}
        
        self.assertEqual(correct(self.inputDictionary), tempResultDict)