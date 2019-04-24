""" 
Created on March 04, 2019

@author Elijah Hampton
"""

import unittest
from nav.predict import predict
from nav.predict import starTableLookup
from nav.predict import calculateLeapYears
from jinja2.utils import missing

class predictTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
#     -----------------------------------------------------------------------
#     Acceptance Tests
#     200 predict operation
#       Happy path analysis:
#       body: String, Mandatory, (Matches name of one of the navigable stars)
#       date: String, Optional
#        - defaults to "2001-01-01
#        - yyyy: GE 2001 and LE 2100
#        - mm/dd: two digit integers
#        - follows conventional rules for expressing months/days
#       time: String, Optional
#        - defaults to "00:00:00"
#        - follows conventional rules for expressing time
#        - two digit integer
#                
#                          
#       Sad path analysis:
#       date
#        - defaults to "2001-01-01" if missing
#        - Wrong type if integer or float
#        - Should not be more than two generate_integers
#       time
#        - defaults to "00:00:00"
#        - Falls outside of conventional rules for expressing time
#       unspecified dictionary elements - ignored
#         error - if any error occurs "error" key should be added to values
#         

#Happy Path Test
#     def test200_010ShouldReturnWithoutErrorIfBodyIsString(self): - TEST THIS AGAIN
#         testDict = {
#             "body": "Achernar",
#             "date": "2001-01-01",
#             "time": "00:00:00"
#         }
#     
#         expectedValue = 1
#         actualValue = 1
#     
#         self.assertEquals(predict(testDict), expectedValue, actualValue)

#     def test200_020MethodShouldReturnCorrectValuesIfBodyCorrectAndPresent(self):
#         testDict = 1
#         
#         expectedValue = 1
#           
#         self.assertEquals(predict(testDict), expectedValue)
     
#     def test200_030MethodShouldIgnoreExtraKeyAndReturnCorrectValues(self):
#         testDict = {
#                "body": 'Archernar',
#                "date": "2001-01-01",
#                "time": "00:00:00",
#                "extraKey": "extraData"
#            }
#          
#         expectedValue = {
#                "body": 'Archernar',
#                "date": "2001-01-01",
#                "time": "00:00:00",
#            }
#            
#         self.assertEquals(predict(testDict), expectedValue)

#     def test200_040MethodShouldDefaultDateAndTimeIfMissingAndReturnCorrectValues(self):
#         testDict = {
#                 "body": 'Archernar'
#             }
#            
#         expectedValue = {
#                 "body": 'Archernar',
#                 "date": "2001-01-01",
#                 "time": "00:00:00",
#             }
#              
#         self.assertEquals(predict(testDict), expectedValue)


#     def test200_050StarTableLookupShouldReturnCorrectDataForSpecifiedStar(self):
#         filePath = "../starinfo.csv"
#         
#         starName = "Aldebaran"
#         actualResults = {
#             "starName": "Aldebaran",
#             "Sidereal Hour Angle": "290d47.1",
#             "Declination": "16d32.3",
#             "Magnitude": "0.85",
#             "Etymology": "follower of the Pleiades"
#         }
#         
#         self.assertEquals(starTableLookup(filePath, starName), actualResults)


#     def test200_060CalculateLeapYearsShouldReturnCorrectNumber(self):
#         expectedValue = 3
#         actualValue = calculateLeapYears(2001, 2016)
#         
#         self.assertEquals(expectedValue, actualValue)


    def test200_070CalculateGreenwichHourAngleShouldReturnCorrectResult(self):
        testDict = {
            "op": "predict",
            "body": "Aldebaran",
            "date": "2016-01-17",
            "time": "03:15:42"
         }
         
        expectedValue = {
            "op": "predict",
            "body": "Aldebaran",
            "date": "2016-01-17",
            "time": "03:15:42",
            "long": "95d41.6",
            "lat": "16d32.3"
         }
          
        self.assertEquals(predict(testDict), expectedValue)
#Sad Path Test
#     def test201_010ValuesShouldReturnValuesWithErrorIfBodyIsNotString(self):
#         testDict = {
#              "body": 5,
#              "date": "2001-01-01",
#              "time": "00:00:00"
#          }
#          
#         expectedValue = {
#              "body": 5,
#              "date": "2001-01-01",
#              "time": "00:00:00",
#              "error": "Error with parameter types."
#          }
#           
#         self.assertEquals(predict(testDict), expectedValue)

#     def test201_020MethodShouldReturnValuesWithErrorKeyIfYearIsGreater2100(self):
#         testDict = {
#                 "body": 'Archernar',
#                 "date": "2120-01-01",
#                 "time": "00:00:00",
#             }
#            
#         expectedValue = {
#                 "body": 'Archernar',
#                 "date": "2120-01-01",
#                 "time": "00:00:00",
#                 "error": "Incorrect boundary for year."
#             }
#              
#         self.assertEquals(predict(testDict), expectedValue)

#     def test201_030MethodShouldReturnValuesWithErrorKeyIfYearIsLess2001(self):
#         testDict = {
#                 "body": 'Archernar',
#                 "date": "2001-01-01",
#                 "time": "00:00:00",
#             }
#            
#         expectedValue = {
#                 "body": 'Archernar',
#                 "date": "2001-01-01",
#                 "time": "00:00:00",
#                 "error": "Incorrect boundary for year."
#             }
#              
#         self.assertEquals(predict(testDict), expectedValue)

#     def test201_040MethodShouldReturnWithErrorKeyIfDayIsNotTwoDigits(self):
#         testDict = {
#             "body": 'Archernar',
#             "date": "2001-01-012",
#             "time": "00:00:00",
#             }
#              
#         expectedValue = {
#             "body": 'Archernar',
#             "date": "2001-01-012",
#             "time": "00:00:00",
#             "error": "Day must only contain two digits."
#             }
#          
#         self.assertEqual(predict(testDict), expectedValue)

#     def test201_040MethodShouldReturnWithErrorKeyIfMonthIsNotTwoDigits(self):
#         testDict = {
#             "body": 'Archernar',
#             "date": "2001-012-01",
#             "time": "00:00:00",
#             }
#              
#         expectedValue = {
#             "body": 'Archernar',
#             "date": "2001-012-01",
#             "time": "00:00:00",
#             "error": "Month must only contain two digits."
#             }
#          
#         self.assertEqual(predict(testDict), expectedValue)

#     def test201_060MethodShouldReturnErrorKeyIfHoursIsGreaterThanTwoDigits(self):
#         testDict = {
#             "body": 'Archernar',
#             "date": "2001-01-01",
#             "time": "000:00:00",
#             }
#               
#         expectedValue = {
#             "body": 'Archernar',
#             "date": "2001-01-01",
#             "time": "000:00:00",
#             "error": "Hours must only contain two digits."
#             }
#           
#         self.assertEqual(predict(testDict), expectedValue)

#     def test201_070MethodShouldReturnErrorKeyIfMinutesIsGreaterThanTwoDigits(self):
#         testDict = {
#             "body": 'Archernar',
#             "date": "2001-01-01",
#             "time": "00:000:00",
#             }
#               
#         expectedValue = {
#             "body": 'Archernar',
#             "date": "2001-01-01",
#             "time": "00:000:00",
#             "error": "Minutes must only contain two digits."
#             }
#           
#         self.assertEqual(predict(testDict), expectedValue)

#     def test201_080MethodShouldReturnErrorKeyIfSecondsIsGreaterThanTwoDigits(self):
#         testDict = {
#             "body": 'Archernar',
#             "date": "2001-01-01",
#             "time": "00:00:000",
#         }
#                
#         expectedValue = {
#         "body": 'Archernar',
#         "date": "2001-01-01",
#         "time": "00:00:000",
#         "error": "Seconds must only contain two digits."
#         }
#            
#         self.assertEqual(predict(testDict), expectedValue)

#     def test201_090MethodShouldReturnValuesWithErrorKeyIfDayOutsideOfBoundary(self):
#         testDict = {
#             "body": 'Archernar',
#             "date": "2001-01-32",
#             "time": "00:00:00",
#             }
#                
#         expectedValue = {
#             "body": 'Archernar',
#             "date": "2001-01-32",
#             "time": "00:00:00",
#             "error": "The value for the day exceeds the boundary."
#             }
#            
#         self.assertEqual(predict(testDict), expectedValue)

#     def test201_100MethodShouldReturnValuesWithErrorKeyIfMonthOutsideOfBoundary(self):
#         testDict = {
#             "body": 'Archernar',
#             "date": "2001-13-01",
#             "time": "00:00:00",
#             }
#                 
#         expectedValue = {
#             "body": 'Archernar',
#             "date": "2001-13-01",
#             "time": "00:00:00",
#             "error": "The value for the month exceeds the boundary."
#             }
#             
#         self.assertEqual(predict(testDict), expectedValue)

#     def test201_110MethodShouldReturnValuesWithErrorKeyIfOpNotPresent(self):
#         testDict = {
#             "body": 'Archernar',
#             "date": "2001-13-01",
#             "time": "00:00:00",
#             }
#                 
#         expectedValue = {
#             "body": 'Archernar',
#             "date": "2001-13-01",
#             "time": "00:00:00",
#             "error": "Op key not present in values."
#             }
#             
#         self.assertEqual(predict(testDict), expectedValue)

