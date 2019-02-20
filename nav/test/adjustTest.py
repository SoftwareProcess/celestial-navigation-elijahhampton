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
    # Happy Path Analysis
    def test100_010ShouldReturnDictWithKeyAltitudeIfCorrectParmTypes(self):
        preDict = {
            "observation": "13d51.6",
            "height": "33",
            "temperature": "72",
            "pressure": "1010",
            "horizon": "natural"
            }
        
        postDict = {
            "altitude": "1",
            "observation": "13d51.6",
            "height" : "33",
            "temperature": "72",
            "pressure": "1010",
            "horizon": "natural"
        }
        
        self.assertEquals(nav.adjust(preDict), postDict)
        