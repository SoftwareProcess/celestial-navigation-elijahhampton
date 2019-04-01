""" 
Created on April 1, 2019

@author Elijah Hampton
"""

def correct(values = None):
    if (values['lat'] == '90d0.0'):
        values['error'] = 'invalid lat'
        return values
    
    return values