from math import sqrt
from math import modf

def convertToCelsius(degree):
    degree = int(degree) - 32
    degree = degree * 5
    degree = degree / 9
    return degree

def tangent(observation):
    x = int(observation.split("d",1)[0])
    y = float(observation.split("d",1)[1])
    
    #calculate tangent
    tangentInDegrees = x + (y/60)
    
    #convert degrees to radians
    tangentInRadians = tangentInDegrees * (3.14/180)
    return tangentInRadians

def adjust(values = None):
    isWrongType = False
    isBoundaryError = False
    
    #check instances
    for x in values:
        if (not(isinstance(values[x], basestring))):
            isWrongType = True
    
    if (isWrongType is True):
        values['error'] = 'error with parm types'
        return values
    
    print('atleast here')
    
    #check boundary values
    for y in values:
        if (y is 'observation'):
            dPattern = "d"
            observationValue = values['observation']
            degreePortionOfAltitude = int(observationValue.split("d",1)[0])
            minutePortionOfAltitude = float(observationValue.split("d",1)[1])
            if (degreePortionOfAltitude < 1 or degreePortionOfAltitude > 90):
                isBoundaryError = True
            
            if (minutePortionOfAltitude < 0.0 or minutePortionOfAltitude > 60.0):
                isBoundaryError = True
                print('boundary error in observation')
        if (y is 'height'):
            heightValueAsInt = int(values['height'])
            if (heightValueAsInt < 0):
                isBoundaryError = True
                print('boundary error in height')
        if (y is 'temperature'):
            temperatureValueAsInt = int(values['temperature'])
            if (temperatureValueAsInt < -20 or temperatureValueAsInt > 120):
                isBoundaryError = True
                print('boundary error in temperature')
        if (y is 'pressure'):
            pressureValueAsInt = int(values['pressure'])
            if (pressureValueAsInt < 100 or pressureValueAsInt > 1100):
                isBoundaryError = True
                print('boundary error in pressure')
        if (y is 'horizon'):
            if (values['horizon'] == 'natural' or values['horizon'] != 'artificial'):
                print('boundary error in horizon')
    
    if (isBoundaryError == True):
        values['error'] = 'parm exceeds boundary limit'
        return values
    
    
    #check and set optional parms if missing
    if (not('height' in values)):
        values['height'] = '0'
    if (not('temperature' in values)):
        values['temperature'] = '72'
    if (not('pressure' in values)):
        values['pressure'] = '1010'
    if (not('horizon' in values)):
        values['horizon'] = 'natural'
    
    #perform adjustment
    dip = 0
    if (values['observation'] is 'natural'):
        dip = (0.97 * sqrt(values['height']))/60
        
    observationX = int(values['observation'].split("d", 1)[0])
    observationY = float(values['observation'].split("d", 1)[1]) / 60
    calcObservation = observationX + observationY
        
    #calculate refraction
    refraction = (-0.00452 * float(values['pressure'])) / (273 + convertToCelsius(values['temperature']))/tangent(values['observation'])
    
    
    preAltitude = calcObservation + dip + refraction
    splitAltitude = modf(preAltitude)
    postAltitudeX = int(splitAltitude[1])
    postAltitudeY = splitAltitude[0] * 60
    
    altitude = str(postAltitudeX) + "d" + str(postAltitudeY)
    values['altitude'] = altitude
    return values