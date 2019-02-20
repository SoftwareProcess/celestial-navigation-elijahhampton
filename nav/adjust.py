from math import sqrt

def convertToCelsius(degree):
    degree = degree - 32
    degree = degree * 5
    degree = degree / 9
    return float(degree)

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
            if (degreePortionOfAltitude < 0 or degreePortionOfAltitude > 90):
                isBoundaryError = True
            
            if (minutePortionOfAltitude < 0.0 or minutePortionOfAltitude > 60.0):
                isBoundaryError = True
        print('about to see height')
        if (y is 'height'):
            heightValueAsInt = int(values['height'])
            if (heightValueAsInt < 0):
                isBoundaryError = True
        print('done with height')
        if (y is 'temperature'):
            temperatureValueAsInt = int(values['temperature'])
            if (temperatureValueAsInt < -20 or temperatureValueAsInt > 120):
                isBoundaryError = True
        if (y is 'pressure'):
            pressureValueAsInt = int(values['pressure'])
            if (pressureValueAsInt < 100 or pressureValueAsInt > 1100):
                isBoundaryError = True
        if (y is 'horizon'):
            if (values['horizon'] != 'natural' or values['horizon'] != 'artificial' or values['horizon'] != ''):
                isBoundaryError = True
    
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
        
    values['altitude'] = '1'
    return values