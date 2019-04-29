def locate(values = None):
    if (int(values['assumedLat'].split('d')[0]) < -90 or int(values['assumedLat'].split('d')[0]) > 90):
        values['error']= 'assumedLat parm outside correct boundary.'
        
    if (float(values['assumedLat'].split('d')[1]) < 0):
        values['error']= 'assumedLat parm outside correct boundary.'
        
    
    return values