def adjust(values = None):
    #check instances
    for x in values:
        if (not(isinstance(values[x], basestring))):
            values['error'] = 'error'
        
        values['altitude'] = '1'
    return values