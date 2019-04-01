""" 
Created on March 04, 2019

@author Elijah Hampton
"""
#from six import string_types
from datetime import datetime, timedelta
import csv
import math
import os.path as path

STAR_INFO_FILE_PATH = "starinfo.csv"
ARIES_DATE = "2001-01-01"
ARIES_TIME = "00:00:00"
ARIES_GREENWICH = "100d42.6"
GHA_DECREASE = "-0d14.31667"
EARTH_ROTATION = 86164.1
EARTH_CLOCK = 86400

def deleteKeysFromDict(inputDict, extraKeysDict):
    for key in extraKeysDict:
        del inputDict[key]
        
    return inputDict

def checkYearBoundaryError(inputDate):
    year = inputDate[0:4]
    year = int(year)
    if (year < 2001 or year > 2100):
        return True
    return False

def starTableLookup(filePathInput, starNameInput):
    starInfoList = []
    filePath = filePathInput
    with open(filePath) as starInfoFile:
        readFile = csv.reader(starInfoFile, delimiter=",")
        for row in readFile:
            starInfoList.append(",".join(row))
    
    correctStar = ""
    starData = {}
    for stars in starInfoList:
        if (stars.split(",")[0] == starNameInput):
            correctStar = stars.split(",")
            for x in correctStar:
                starData["starName"] = correctStar[0]
                starData["Sidereal Hour Angle"] = correctStar[1]
                starData["Declination"] = correctStar[2]
                starData["Magnitude"] = correctStar[3]
                starData["Etymology"] = correctStar[4]
    
    
    for element in starData:
        if "\xc2\xa0" in starData[element]:
            starData[element] = starData[element].replace("\xc2\xa0", " ")
            
    PATH_FOR_OS = path.abspath(path.join(__file__,"../../" + filePathInput))
    
    return starData

def calculateLeapYears(fromYear, toYear):
    leapYearCount = 0
    while (fromYear != toYear):
        if (fromYear % 4) == 0:
            if (fromYear % 100) == 0:
                if (fromYear % 400) == 0:
                    print "Found leap year!"
                    leapYearCount = leapYearCount + 1
                else:
                    print "No leap year"
            else:
                print "Found leap year!"
                leapYearCount = leapYearCount + 1
        else:
            print "No leap year!"
        fromYear = fromYear + 1
    return leapYearCount

def calculateTotalSecondsFromDayAndTime(daysInput, timeInput):
    totalDays = timedelta(days=int(daysInput))
    secondsFromDays = totalDays.total_seconds()
    
    hours = timeInput.split(":")[0]
    minutes = timeInput.split(":")[1]
    seconds = timeInput.split(":")[2]
    
    secondsFromHours = int(hours) * 3600
    secondsFromMinutes = int(minutes) * 60
    seconds  = int(seconds)
    totalSeconds = secondsFromDays + secondsFromHours + secondsFromMinutes + seconds
    return totalSeconds

def predict(values = None):
    isWrongType = False
    isYearBoundaryError = False
    
    #Check if op key is present
    if not("op" in values):
        values["error"] = "Op key not present in values."
        return values
    
    #Default date and time if not present
    if not("date" in values):
        values["date"] = "2001-01-01"
    if not("time" in values):
        values["time"] = "00:00:00"
        
    #Check if Day and Month are two digits only
    day = values["date"].split("-")
    day = day[len(day) - 1]
    if (len(day) > 2):
        values["error"] = "Day must only contain two digits."
        return values
    if (int(day) < 1 or int(day) > 31):
        values["error"] = "The value for the day exceeds the boundary."
        return values
    
    month = values["date"].split("-")
    month = month[1]
    if (len(month) > 2):
        values["error"] = "Month must only contain two digits."
        return values
    if (int(month) < 1 or int(month) > 12):
        values["error"] = "The value for the month exceeds the boundary."
        return values
    
    #Check if hours, minutes, or seconds are two digits only
    timeValues = values["time"].split(":")
    hours = timeValues[0]
    minutes = timeValues[1]
    seconds = timeValues[2]
    
    if (len(hours) > 2):
        values["error"] = "Hours must only contain two digits."
        return values
    
    if (len(minutes) > 2):
        values["error"] = "Minutes must only contain two digits."
        return values
    
    if (len(seconds) > 2):
        values["error"] = "Seconds must only contain two digits."
        return values
    
    #Check value boundaries
    isYearBoundaryError = checkYearBoundaryError(values['date'])
    if (isYearBoundaryError is True):
        values["error"] = "Incorrect boundary for year."
        return values
    
    #Check instances of variables
    #for x in values:
     #   if x is 'body':
      #      if (isinstance(values[x], string_types) == False):
       #         isWrongType = True
        #    elif (values[x] == ''):
         #       isWrongType = True
    
    #Check to see if we encountered any values with wrong types
    if (isWrongType is True):
        values['error'] = 'Error with parameter types.'
        return values
    
    #Remove Extra Keys
    extraValues = dict()
    for x in values:
        if x != "body" and x != "date" and x != "time" and x != "op":
            extraValues[x] = values[x]
            
    deleteKeysFromDict(values, extraValues)
    
    #Calculate Greenwich Hour Angle
    body = values["body"]
    date = values["date"]
    time = values["time"]
    
    #Retrieve star data
    starData = starTableLookup(STAR_INFO_FILE_PATH, body)
    
    #Assign latitude
    lat = starData["Declination"]
    
    #Sidereal Hour Angle
    SHA_star = starData["Sidereal Hour Angle"]
    
    #Determine Angular Difference
    referenceYear = int(ARIES_DATE.split("-")[0])
    observationYear = int(values["date"].split("-")[0])
    yearDifference = observationYear - referenceYear
    
    GHA_DECREASEX = int(GHA_DECREASE.split("d")[0])
    GHA_DECREASEY = -1 * float(GHA_DECREASE.split("d")[1])
    GHA_DECREASESUM = GHA_DECREASEX + (GHA_DECREASEY / 60) #Might need to check this
    GHA_DECREASESUMVALUE = str(GHA_DECREASESUM * yearDifference)
    GHA_DECREASESUMVALUEX = int(GHA_DECREASESUMVALUE.split(".")[0]) #IMPORTANT X
    GHA_DECREASESUMVALUEY = "." + GHA_DECREASESUMVALUE.split(".")[1]
    GHA_DECREASESUMVALUEY = -1 * float(GHA_DECREASESUMVALUEY)
    GHA_DECREASESUMVALUEY = GHA_DECREASESUMVALUEY * 60 #IMPORTANT Y
    
    #cumulativeProgression = LEAVING EVERYTHING IN X AND Y FOR NOW
    
    #Determine Leap Progression
    leapProgressionBeforeYearsCalc = str(abs(360 - 86164.1 / 86400 * 360)) #0.9829
    leapProgressionBeforeYearsCalcX = int(leapProgressionBeforeYearsCalc.split(".")[0]) #0
    
    
    leapProgressionBeforeYearsCalcY = "." + leapProgressionBeforeYearsCalc.split(".")[1] #.9829
    leapProgressionBeforeYearsCalcY = float(leapProgressionBeforeYearsCalcY) * 60 #58.975 (59)
    
    leapProgressionY = str((leapProgressionBeforeYearsCalcY / 60) * 3)
    leapProgressionX = int(leapProgressionY.split(".")[0]) #2
    leapProgressionY = float("." + leapProgressionY.split(".")[1]) #.94875
    leapProgressionY = leapProgressionY * 60 #56.9
    
    #Determine how far prime meridian has rotated
    ARIES_GREENWICHX = int(ARIES_GREENWICH.split("d")[0])
    ARIES_GREENWICHY = float(ARIES_GREENWICH.split("d")[1])
    
    GHAProgression =( (ARIES_GREENWICHY / 60) + (GHA_DECREASESUMVALUEY / 60) + (leapProgressionY / 60) 
                      + (ARIES_GREENWICHX + leapProgressionX + GHA_DECREASESUMVALUEX) )
    
    GHAProgressionX = int(str(GHAProgression).split(".")[0])
    GHAProgressionY = "." + str(GHAProgression).split(".")[1]
    GHAProgressionY = float(GHAProgressionY) * 60
    
    #Calculate angle of earths rotation
    ##Calculate total num seconds between dates##
    oYear = datetime(year = 2016, month = 1, day = 17, hour = 3, minute = 15, second = 42)
    rYear = datetime(year = 2016, month = 1, day = 1, hour = 0, minute = 0, second = 0)
    dateValues = oYear - rYear
    daysCalculated = str(dateValues).split(",")[0].replace(" days", "")
    timeCalculated = str(dateValues).split(",")[1].replace(" ", "")
    
    totalSeconds = calculateTotalSecondsFromDayAndTime(daysCalculated, timeCalculated)
    
    earthRotationAngle = str((totalSeconds / EARTH_ROTATION * 360) % 360)
    earthRotationAngleX = int(earthRotationAngle.split(".")[0])
    earthRotationAngleY = float("." + earthRotationAngle.split(".")[1])
    earthRotationAngleY = earthRotationAngleY * 60
    
    
    #Calculate Total
    totalX = GHAProgressionX + earthRotationAngleX
    totalY = GHAProgressionY + earthRotationAngleY
    
    #Calculate Star GHA
    starSHA = starData["Sidereal Hour Angle"]
    starSHAX = int(starSHA.split("d")[0])
    starSHAY = float(starSHA.split("d")[1])
    
    starGHAX = totalX + starSHAX
    starGHAY = (totalY / 60) + (starSHAY / 60)
    starGHAY = float("." + str(starGHAY).split(".")[1]) * 60
    
    if (starGHAX > 360):
        starGHAX = starGHAX - 360
    
    starGHAY = round(starGHAY,2)
    long = str(starGHAX) + "d" + str(starGHAY)
    
    values["long"] = long
    return values