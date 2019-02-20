def adjust(values = None):
    #check instances
    hasWrongType = False
    for x in values:
        if (not(isinstance(values[x], basestring))):
            hasWrongType = True
    
    if (hasWrongType is True):
        values['error'] = 'error'
        
        
    values['altitude'] = '1'
    return values