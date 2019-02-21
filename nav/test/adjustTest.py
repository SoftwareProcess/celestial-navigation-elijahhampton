import unittest
import nav.adjust as nav
from jinja2.utils import missing

class adjustTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
     # -----------------------------------------------------------------------
    # ---- Acceptance Tests
    # 100 adjust operation
    #   Happy path analysis:
    #        observation: mandatory, string
    #            form: xdy.y
    #            x - integer, GE 0, LT 90
    #            d - character 'd'
    #            y.y - float, GE 0.0, LT 60.0
    #
    #        height - string (of numeric value), GE 0, optional, defaults to 0
    #        temperature - string (of integer), GE 0, optional, defaults to 0
    #        pressure - string (of integer), GE -20, LE 120, optional, defaults to 72
    #        horizon - strings, optional, defaults to natural
    #
    #           
    #                     
    #   Sad path analysis:
    #        height - defaults to 0 if missing
    #        temperature - defaults to 0 if missing
    #        pressure - defaults to 0 if missing
    #        horizing - defaults to "natural" if missing
    #        other - ignore
    #        wrong type - default to value
    #################################################################################################
    # Happy Path Test
    # def test100_010ShouldReturnDictWithKeyAltitudeIfCorrectParmTypes(self):
    #    preDict = {
    #        "observation": "13d51.6",
    #        "height": "33",
    #        "temperature": "72",
    #        "pressure": "1010",
    #        "horizon": "natural"
    #        }
    #    
    #    postDict = {
    #        "altitude": "1",
    #        "observation": "13d51.6",
    #        "height" : "33",
    #        "temperature": "72",
    #        "pressure": "1010",
    #        "horizon": "natural"
    #    }
    #    
    #    self.assertEquals(nav.adjust(preDict), postDict)
    
    #def test100_020ShouldReturnDictWithKeyAltitudeIfCorrectParmBoundaries(self):
    #    preDict = {
    #        "observation": "13d51.6",
    #        "height": "33",
    #        "temperature": "72",
    #        "pressure": "1010",
    #        "horizon": "natural"
    #        }
    #    
    #    postDict = {
    #        "altitude": "1",
    #        "observation": "13d51.6",
    #        "height" : "33",
    #        "temperature": "72",
    #        "pressure": "1010",
    #        "horizon": "natural"
    #    }
    #    
    #    self.assertEquals(nav.adjust(preDict), postDict)
    
    #def test100_030ShouldSetValuesOfOptionalParmIfMissing(self):
    #    preDict = {
    #        "observation": "13d51.6"
    #        }
    #    
    #    postDict = {
    #        "altitude": "1",
    #        "observation": "13d51.6",
    #        "height" : "0",
    #        "temperature": "72",
    #        "pressure": "1010",
    #       "horizon": "natural"
    #    }
    #    
    #    self.assertEquals(nav.adjust(preDict), postDict)
    
#     def test110_010ShouldConvertCelsius(self):
#         valueInFahrenheight = 100.00
#         self.assertAlmostEqual(int(nav.convertToCelsius(valueInFahrenheight)), 37)
    
    def test120_010ShouldReturnCorrectTangentInDegrees(self):
        testObservation = "13d51.6"
        actualResult = nav.tangent("13d51.6")
        expectedresult = .2419
        self.assertAlmostEqual(actualResult, expectedresult, 5)
        pass
      
    #def test100_040ShouldReturnValuesWithCorrectAdjustment(self):
    #    preDict = {
    #        "observation": "30d1.5",
    #        "height": "19.0",
    #        "temperature": "85",
    #        "pressure": "1000",
    #        "horizon": "artificial"
    #        }
    #    
    #    postDict = {
    #        "altitude": "29d59.9",
#   #        "observation": "30d1.5",
#             "height": "19.0",
#             "temperature": "85",
#             "pressure": "1000",
#             "horizon": "artificial"
#             }
#         
#         self.assertEquals(nav.adjust(preDict), postDict)
#         pass
    
    ###################################################################################################
    # Sad Path Test
    #def test000_010ShouldReturnDictWithKeyErrorIfWrongParmType(self):
    #    preDict = {
    #        "observation": 5,
    #        "height": "33",
    #        "temperature": "72",
    #        "pressure": "1010",
    #        "horizon": "natural"
    #        }
    #    
    #    postDict = {
    #        "error": "error with parm types",
    #        "observation": 5,
    #        "height" : "33",
    #        "temperature": "72",
    #        "pressure": "1010",
    #        "horizon": "natural"
    #    }
    # 
    #     self.assertEquals(nav.adjust(preDict), postDict)
    
    #def test000_020ShouldReturnDictWithKeyErrorIfBoundaryExceedsSpecifications(self):
    #    preDict = {
    #        "observation": "13d51.6",
    #        "height": "-5",
    #        "temperature": "72",
    #        "pressure": "1010",
    #        "horizon": "natural"
    #        }
    #    
    #    postDict = {
    #        "error": "parm exceeds boundary limit",
    #        "observation": "13d51.6",
    #        "height" : "-5",
    #        "temperature": "72",
    #        "pressure": "1010",
    #        "horizon": "natural"
    #    }
    #    
    #    self.assertEquals(nav.adjust(preDict), postDict)