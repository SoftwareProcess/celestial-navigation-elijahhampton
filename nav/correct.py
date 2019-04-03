""" 
Created on April 1, 2019

@author Elijah Hampton
"""

def correct(values = None):
    #Check if lat key is present
    if not("lat" in values):
        values["error"] = "lat parm not present in input dict."
        return values
    
    #Check if long key is present
    if not("long" in values):
        values["error"] = "long parm not present in input dict."
        return values
    
    #Check if lat is in appropriate bounds
    if (values['lat'] == '90d0.0'):
        values['error'] = 'invalid lat'
        return values
    
    tempLongValue = values['long']
    tempLongValueX = int(values['long'].split('d')[0])
    tempLongValueY = float(values['long'].split('d')[1])
    
    if (tempLongValueX < 0 or tempLongValueX > 360):
        values['error'] = 'long parm outside correct boundary.'
        return values
    
    tempAltitudeValue = values['altitude']
    tempAltitudeValueX = int(tempAltitudeValue.split('d')[0])
    tempAltitudeValueY = float(tempAltitudeValue.split('d')[1])
    print tempAltitudeValue
    print tempAltitudeValueX
    
    if (tempAltitudeValueX < 0 or tempAltitudeValueX > 360):
        values['error'] = 'altitude parm outside correct boundary.'
        return values
    
    
    return values