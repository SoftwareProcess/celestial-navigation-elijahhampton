""" 
Created on March 04, 2019

@author Elijah Hampton
"""

import unittest
from nav import locate
from jinja2.utils import missing

class locateTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
#     ----------------------------------------------------------------------

#         self.setParm('assumedLat', '-53d38.4')
#         self.setParm('assumedLong', '350d35.3')
#         self.setParm('corrections', '[[100,1d0.0]]')
#         self.setParm('op', 'locate')

# Happy Path Test


# Sad Path Test
def test200_010ShouldReturnWithErrorKeyIfXOfAssumedLatIsGTNegNinety(self):
        self.setParm('assumedLat', '-91d38.4')
        self.setParm('assumedLong', '350d35.3')
        self.setParm('corrections', '[[100,1d0.0]]')
        self.setParm('op', 'locate')
          
        tempResultDict = {'op': 'locate',
                          'assumedLat': '-53d38.4',
                          'assumedLong': '350d35.3',
                          'error': 'assumedLat parm outside correct boundary.'}
         
        self.assertEqual(locate(self.inputDictionary), tempResultDict)