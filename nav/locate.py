def locate(values = None):
    
    try:
        tempValues = values
        for key in tempValues:
            if (key == 'assumedLat'):
                        int(tempValues[key].split('d')[0])
    except ValueError:
        values['error'] = 'Found parm with wrong type (correct: integer).'
        return values
    
    try:
        tempValues = values
        for key in tempValues:
            if (key == 'assumedLat'):
                        float(tempValues[key].split('d')[1])
    except ValueError:
        values['error'] = 'Found parm with y.y portion as incorrect type. (correct: float).'
        return values
    
    if (int(values['assumedLat'].split('d')[0]) < -90 or int(values['assumedLat'].split('d')[0]) > 90):
        values['error']= 'assumedLat parm outside correct boundary.'
        
    if (float(values['assumedLat'].split('d')[1]) < 0 or float(values['assumedLat'].split('d')[1]) > 59):
        values['error']= 'assumedLat parm outside correct boundary.'
    
    if (float(values['assumedLong'].split('d')[0]) < 0 or float(values['assumedLong'].split('d')[0]) > 360):
        values['error']= 'assumedLong parm outside correct boundary.'
    
    return values