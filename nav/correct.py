""" 
Created on April 1, 2019

@author Elijah Hampton
"""

def correct(values = None):
    #Check if lat is in appropriate bounds
    if (values['lat'] == '90d0.0'):
        values['error'] = 'invalid lat'
        return values
    
    #Check if lat key is present
    if not("lat" in values):
        values["error"] = "lat parm not present in input dict."
        return values
    
    return values