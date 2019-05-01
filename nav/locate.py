import math

def locate(values = None):
    
    try:
        tempValues = values
        for key in tempValues:
            if (key == 'assumedLat' or key == 'assumedLong'):
                        int(tempValues[key].split('d')[0])
    except ValueError:
        values['error'] = 'Found parm with wrong type (correct: integer).'
        return values
    
    try:
        tempValues = values
        for key in tempValues:
            if (key == 'assumedLat' or key == 'assumedLong'):
                        float(tempValues[key].split('d')[1])
    except ValueError:
        values['error'] = 'Found parm with y.y portion as incorrect type. (correct: float).'
        return values
    
    if (int(values['assumedLat'].split('d')[0]) < -90 or int(values['assumedLat'].split('d')[0]) > 90):
        values['error']= 'assumedLat parm outside correct boundary.'
        
    if (float(values['assumedLat'].split('d')[1]) < 0 or float(values['assumedLat'].split('d')[1]) > 59):
        values['error']= 'assumedLat parm outside correct boundary.'
    
    if (int(values['assumedLong'].split('d')[0]) < 0 or int(values['assumedLong'].split('d')[0]) > 360):
        values['error']= 'assumedLong parm outside correct boundary.'
        
    if (float(values['assumedLong'].split('d')[1]) < 0 or float(values['assumedLong'].split('d')[1]) > 59):
        values['error']= 'assumedLong parm outside correct boundary.'
        
    #Calculate the present position as the vector sum of the corrrections for each sighting
    corrections = values['corrections']
    corrections = corrections[1:len(corrections) - 1]
    corrections = corrections.split(',')
    
    nsCorrection = 0
    ewCorrection = 0
    
    return values

def getCorrectedDistances(corrections):
    i = 0
    tempArr = []
    for distance in corrections:
        if (i % 2 == 0):
            tempArr.append(int(i[1:]))
        i += 1
    
def getCorrectedAzimuths(corrections):
    j = 0
    tempArr = []
    for azimuth in corrections:
        if (j % 2 != 0):
            tempArr.append(azimuth[:len(azimuth)-1])
        j += 1

def calculateNsCorrection(distanceValues, azimuthValues):
    i = 0
    tempSum = 0
    while (i < len(distanceValues)):
        correctedAzimuthX = int(azimuthValues[i].split('d')[0])
        correctedAzimuthY = float(azimuthValues[i].split('d')[1]) / 60
        correctedAzimuthSum = math.radians(correctedAzimuthX + correctedAzimuthY)
        tempSum += (distanceValues[i] + math.cos((correctedAzimuthSum)))
        i += 1
        
    tempSum /= len(distanceValues)
    tempSum = round(tempSum, 2)
    return tempSum 

def calculateEwCorrection(distanceValues, azimuthValues):
    i = 0
    tempSum = 0
    while (i < len(distanceValues)):
        corr
        