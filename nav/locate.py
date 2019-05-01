import math


def locate(values=None):
    
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
        values['error'] = 'assumedLat parm outside correct boundary.'
        
    if (float(values['assumedLat'].split('d')[1]) < 0 or float(values['assumedLat'].split('d')[1]) > 59):
        values['error'] = 'assumedLat parm outside correct boundary.'
    
    if (int(values['assumedLong'].split('d')[0]) < 0 or int(values['assumedLong'].split('d')[0]) > 360):
        values['error'] = 'assumedLong parm outside correct boundary.'
        
    if (float(values['assumedLong'].split('d')[1]) < 0 or float(values['assumedLong'].split('d')[1]) > 59):
        values['error'] = 'assumedLong parm outside correct boundary.'
        
    # Calculate the present position as the vector sum of the corrrections for each sighting
    corrections = values['corrections']
    corrections = corrections[1:len(corrections) - 1]
    corrections = corrections.split(',')
    
    nsCorrection = 0
    ewCorrection = 0
    precision = 0
    
    assumedLat = values['assumedLat']
    assumedLong = values['assumedLong']
    
    distanceArr = getCorrectedDistances(corrections)
    azimuthArr = getCorrectedAzimuths(corrections)
    
    nsCorrection = math.degrees(calculateNsCorrection(distanceArr, azimuthArr))
    ewCorrection = math.degrees(calculateEwCorrection(distanceArr, azimuthArr))
    
    assumedLongX = int(assumedLong.split('d')[0])
    assumedLongY = float(assumedLong.split('d')[1])
    calcAssumedLong = assumedLongX = (assumedLongY / 60)
    
    assumedLatX = int(assumedLat.split('d')[0])
    assumedLatY = float(assumedLat.split('d')[1])
    calcAssumedLat = assumedLatX + (assumedLatY / 60)
    
    presentLat = int(calcAssumedLat + (nsCorrection / 60))
    presentLatEx = round((presentLat) * 60, 1)
    presentLong = int(calcAssumedLong + (ewCorrection / 60))
    presentLongEx = round((presentLong) * 60, 1)
    
    precision = calculationPrecision(distanceArr, azimuthArr, nsCorrection, ewCorrection)
    accuracy = "NA"
    
    
    values['presentLat'] = str(presentLat) + 'd' + str(presentLatEx)
    values['presentLong'] = str(presentLong) + 'd' + str(presentLongEx)
    values['precision'] = precision
    values['accuracy'] = 'NA'
    

    return values


def getCorrectedDistances(corrections):
    i=0
    tempArr=[]
    for distance in corrections:
        if (i % 2 == 0):
            tempArr.append(int(distance[1:]))
        i += 1
    return tempArr
    
def getCorrectedAzimuths(corrections):
    j=0
    tempArr=[]
    for azimuth in corrections:
        if (j % 2 != 0):
            tempArr.append(azimuth[:len(azimuth) - 1])
        j += 1
    return tempArr


def calculateNsCorrection(distanceValues, azimuthValues):
    i=0
    tempSum=0
    while (i < len(distanceValues)):
        correctedAzimuthX=int(azimuthValues[i].split('d')[0])
        correctedAzimuthY=float(azimuthValues[i].split('d')[1]) / 60
        correctedAzimuthSum=math.radians(correctedAzimuthX + correctedAzimuthY)
        tempSum += (distanceValues[i] + math.cos((correctedAzimuthSum)))
        i += 1
        
    tempSum /= len(distanceValues)
    tempSum=round(tempSum, 2)
    return tempSum 


def calculateEwCorrection(distanceValues, azimuthValues):
    i=0
    tempSum=0
    while (i < len(distanceValues)):
        correctedAzimuthX=int(azimuthValues[i].split('d')[0])
        correctedAzimuthY=float(azimuthValues[i].split('d')[1]) / 60
        correctedAzimuthSum=math.radians(correctedAzimuthX + correctedAzimuthY)
        tempSum += (distanceValues[i] + math.sin((correctedAzimuthSum)))
        i += 1
    
    tempSum /= len(distanceValues)
    tempSum=round(tempSum, 2)
    return tempSum

    
def calculationPrecision(distanceValues, azimuthValues, nsCorrection, ewCorrection):
   temp = 0
   temp = precisionFunction(distanceValues, azimuthValues, nsCorrection, ewCorrection)
   temp /= len(distanceValues)
   temp = int(round(temp))
   return temp
        
def precisionFunction(distanceValues, azimuthValues, nsCorrection, ewCorrection):
    i = 0
    tempSum = 0
    while (i < len(distanceValues)):
        correctedAzimuthX=int(azimuthValues[i].split('d')[0])
        correctedAzimuthY=float(azimuthValues[i].split('d')[1]) / 60
        correctedAzimuthSum=math.radians(correctedAzimuthX + correctedAzimuthY)
        func = math.sqrt(math.pow(distanceValues[i] * math.cos(correctedAzimuthSum) - nsCorrection),2 )
        + math.pow((distanceValues[i] + math.sin(correctedAzimuthSum)) - ewCorrection)
        tempSum += func
        i += 1
    return tempSum