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
    
    #Check if altitude key is present
    if not("altitude" in values):
        values["error"] = "altitude parm not present."
        return values;
    
    #Check if assumed lat key is present
    if not("assumedLat" in values):
        values["error"] = "assumedLat parm not present."
        return values;
    
    #Check if assumed long key is present
    if not("assumedLong" in values):
        values['error'] = "assumedLong parm not present."
        return values
    
    #Check if x portion of lat, long, altitude, assumedLat, and assumedLong are integers
    try:
        tempValues = values
        for key in tempValues:
            if (key == 'lat' or key == 'long' 
                or key =='altitude' or key =='assumedLat' 
                    or key == 'assumedLong'):
                        int(tempValues[key].split('d')[0])
    except ValueError:
        values['error'] = 'Found parm with wrong type (correct: integer).'
        return values
    
     #Check if x xportion of lat, long, altitude, assumedLat, and assumedLong are floats
    try:
        tempValues = values
        for key in tempValues:
            if (key == 'lat' or key == 'long' 
                or key =='altitude' or key =='assumedLat' 
                    or key == 'assumedLong'):
                        float(tempValues[key].split('d')[1])
    except ValueError:
        values['error'] = 'Found parm with y.y portion as incorrect type. (correct: float)'
        return values
    
    #Check if lat is in appropriate bounds
    if (values['lat'] == '90d0.0'):
        values['error'] = 'invalid lat'
        return values
    
    tempLongValue = values['long']
    tempLongValueX = int(values['long'].split('d')[0])
    tempLongValueY = float(values['long'].split('d')[1])
    
    #Check x value of long
    if (tempLongValueX < 0 or tempLongValueX > 360):
        values['error'] = 'long parm outside correct boundary.'
        return values
    
    tempAltitudeValue = values['altitude']
    tempAltitudeValueX = int(tempAltitudeValue.split('d')[0])
    tempAltitudeValueY = float(tempAltitudeValue.split('d')[1])
    
    #Check X value of altitude
    if (tempAltitudeValueX < 0 or tempAltitudeValueX > 90):
        values['error'] = 'altitude parm outside correct boundary.'
        return values
    
    tempAssumedLatX = int(values['assumedLat'].split('d')[0])
    tempAssumedLatY = float(values['assumedLat'].split('d')[1])
    
    #Check x value of assumedLat
    if (tempAssumedLatX < -90 or tempAssumedLatX > 90):
        values['error'] = 'assumedLat parm outside correct boundary.'
        return values
    
    tempAssumedLongX = int(values['assumedLong'].split('d')[0])
    tempAssumedLongY = float(values['assumedLong'].split('d')[1])
    
    #Check x value of assumedLong
    if (tempAssumedLongX < 0 or tempAssumedLongX > 360):
        values['error'] = 'assumedLong parm outside correct boundary.'
        return values
    
    #Check if y.y portion of lat, long, altitude, assumedLat, and assumedLong are within correct bounds
    yBoundaryError = False
    for key in values:
        if (key == 'lat' or key == 'long' 
                or key =='altitude' or key =='assumedLat' 
                    or key == 'assumedLong'):
                        if (float(values[key].split('d')[1]) < 0 or float(values[key].split('d')[1]) > 59):
                            yBoundaryError = True
                                
    if (yBoundaryError == True):
        values['error'] = 'Found Parm with y portion outside of correct boundary.'
        return values
    
    return values