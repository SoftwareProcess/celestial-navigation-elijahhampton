from __future__ import division
from math import sin, cos, asin, acos, radians

""" 
Created on April 1, 2019

@author Elijah Hampton
"""

def radiansToDegrees(numInRadians):
    numInDegrees = (numInRadians * 180) / 3.14
    return numInDegrees

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
    
    #Calculate local hour angle
    localhourAngleX = int(values['long'].split('d')[0]) + int(values['assumedLong'].split('d')[0])
    localHourAngleY = float(values['long'].split('d')[1]) + float(values['assumedLong'].split('d')[1])
    
    #Calculate intermmediate distance
    intermmediateDistance = ( ((sin(int(values['lat'].split('d')[0])) + sin(float(values['lat'].split('d')[1]))) * ((sin(int(values['assumedLat'].split('d')[0])) + sin(float(values['assumedLat'].split('d')[1]))) 
                               + ((cos(int(values['lat'].split('d')[0])) + cos(float(values['lat'].split('d')[1]))) * ((cos(int(values['assumedLat'].split('d')[0])) + cos(float(values['assumedLat'].split('d')[1]))) 
                                    * (cos(localhourAngleX) + cos(localHourAngleY) ))))))
    
    #Calculate correctedAltitude
    preCorrectedAltitude = str(radiansToDegrees(asin(intermmediateDistance))) #Should have 15.41256
    correctedAltitudeX = int(preCorrectedAltitude.split('.')[0])
    correctedAltitudeY = float(preCorrectedAltitude.split('.')[1]) * 60
    
    #Calculate distance in arc minutes and round to nearest 0.1 arc minute
    #calculate
    correctedDistanceX = int(values['altitude'].split('d')[0]) - correctedAltitudeX
    correctedDistanceY = float(values['altitude'].split('d')[1]) - correctedAltitudeY
    correctedDistance = (correctedDistanceY / 60) + correctedDistanceX
    correctedDistance = correctedDistance * 60
    
    #Round to nearest arc minute 1
    round(correctedDistance)
    
    #Determine compass direction in which to make the distance adjustment
    print(   sin(radians(int(values['lat'].split('d')[0]) + (float(values['lat'].split('d')[1]) / 60))    )    )
    print(sin(radians(int(values['assumedLat'].split('d')[0])) + (float(values['assumedLat'].split('d')[1]) / 60))))
    print(intermmediateDistance)
    print(cos(int(values['assumedLat'].split('d')[0])) + cos(float(values['assumedLat'].split('d')[1])))
    print(cos(correctedDistance))
    
    
    preCorrectedAzimuth =  str( radiansToDegrees( acos(
        (sin(int(values['lat'].split('d')[0])) + sin(float(values['lat'].split('d')[1]))) - (  (sin(int(values['assumedLat'].split('d')[0])) + sin(float(values['assumedLat'].split('d')[1]))) * intermmediateDistance)
            // (  (cos(int(values['assumedLat'].split('d')[0])) + cos(float(values['assumedLat'].split('d')[1]))) * cos(correctedDistance))))) #Should be 82.9490446
    
    
    correctedAzimuthX = int(preCorrectedAzimuth.split('.')[0])
    correctedAzimuthY = float(preCorrectedAzimuth.split('.')[1]) * 60
    
    
    if (correctedDistance < 0):
        correctedDistance = abs(correctedDistance)
        correctedAzimuthX = (correctedAzimuthX + 180) % 360
        
    #Convert correctedAzimuth and correctedDistance to strings
    correctedAzimuth = str(correctedAzimuthX) + 'd' + str(correctedAzimuthY)
    correctedDistance = str(correctedDistance)
    
    #Add values to dictionary
    values['correctedAzimuth'] = correctedAzimuth
    values['correctedDistance'] = correctedDistance
    
    return values