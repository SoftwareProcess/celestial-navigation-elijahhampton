def locate(values = None):
    if (values['assumedLat'] > -90):
        values['error']= 'assumedLat parm outside correct boundary.'
    return values