import adjust

def handleDuplicateParm(values):
    dupCounter = 0
    newParmList = []
    operationsList = []
    
    for x in values:
        operationsList.append(x)
        
    for y in operationsList:
        for z in operationsList[:z-1]:
            if ( y is z ):
                continue
            
        for z in operationsList[z: ]:
            if ( y is z ):
                continue
            
        newParmList.add(y)       
    return newParmList;
    
def dispatch(values=None):

    #Validate parm
    if(values == None):
        return {'error': 'parameter is missing'}
    if(not(isinstance(values,dict))):
        return {'error': 'parameter is not a dictionary'}
    if (not('op' in values)):
        values['error'] = 'no op  is specified'
        return values
    
    #Check parm
    

    #Perform designated function
    if(values['op'] == 'adjust'):
        result = adjust.adjust(values)
        return result    
    elif(values['op'] == 'predict'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'correct'):
        return values    #This calculation is stubbed out
    elif(values['op'] == 'locate'):
        return values    #This calculation is stubbed out
    else:
        values['error'] = 'op is not a legal operation'
        return values
