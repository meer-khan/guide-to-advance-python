import datetime
import time
'''
datetime is a module in python, that provides us with 6 classes, which has multiple useful functions.
We dont need to install this module seperately, it comes with the default installation of python. 

Classes given by datetime module are given below:
1- date
2- time
3- datetime
4- timedelta
5- tzinfo
6- timezone

every class has many functions and we will explore all of them InshAllah

'''

# Date class
def getDate():
    date = datetime.date(1997,10,10)
    print("date is: ", date)
    print("Type of date is: ",type(date))

    # Uncommenting my_date = date(1996, 12, 39)
    # will raise an ValueError as it is
    # outside range
    
    # uncommenting my_date = date('1996', 12, 11)
    # will raise a TypeError as a string is
    # passed instead of integer



def getTime():

    time = datetime.time(hour = 11,minute = 34, second = 56, microsecond=11)
    print("Hours: " , time.hour)
    print("Minutes: ", time.minute)
    print("Seconds: ", time.second)
    print("Microseconds: ", time.microsecond)


def convertingTimeObjectIntoString():
    time = datetime.time(hour = 11,minute = 34, second = 56, microsecond=11)
    print("Hours: " , time.hour)
    print("Minutes: ", time.minute)
    print("Seconds: ", time.second)
    print("Microseconds: ", time.microsecond)
    print(type(time.hour))
    print(type(time))
    timeInStr = time.isoformat()
    # Seconds will be caluclated upto 6 decimal digits (Microseonds) 
    print("Time in String object is: ", timeInStr, " Type of this time is: ", type(timeInStr))


def convetingStringTimeObjectintoTimeClassObject():
    time = datetime.time(hour = 11,minute = 34, second = 56, microsecond=11)
    print("Hours: " , time.hour)
    print("Minutes: ", time.minute)
    print("Seconds: ", time.second)
    print("Microseconds: ", time.microsecond)
    print(type(time.hour))
    print(type(time))
    timeInStr = time.isoformat()
    # Seconds will be caluclated upto 6 decimal digits (Microseonds) 
    print("Time in String object is: ", timeInStr, " Type of this time is: ", type(timeInStr))

    timeObjectConversion = datetime.time.fromisoformat(timeInStr)
    print(type(timeObjectConversion))
# getDate()
# getTime()

def replaceFunc():
    time = datetime.time(hour = 11)
    replacement = time.replace(hour=5)
    print(replacement)

def strfTimeConversion():
    time = datetime.time(hour= 11, minute = 34)
    replacement = time.strftime("%H/%M")
    print(replacement)

def datetimeFunc():
    a = datetime.datetime(1999, 12, 12)
    print(a)
    # Initializing constructor
    # with time parameters as well
    a = datetime.datetime(1999, 12, 12, 12, 12, 12, 342380)
    print(a)

def getDateTimeChunks():
    a = datetime.datetime(1999, 1, 12, 12, 12, 12)
    print("year =", a.year)
    print("month =", a.month)
    print("hour =", a.hour)
    print("minute =", a.minute)
    print("timestamp =", datetime.datetime.timestamp(a))


def currentDateTime():
    currentDateAndTime = datetime.datetime.now()
    print(currentDateAndTime)


def getTodaysDate():
    todaysDate = datetime.date.today()
    print(todaysDate)


def getTodaysDateandSplitIntoChunks():
    todaysDate = datetime.date.today()
    print(todaysDate.year)
    print(todaysDate.month)
    print(todaysDate.day)


def convertingDateIntoString():
    date = datetime.date.today()
    # dateIntoString = date.isoformat()
    # OR we can write below line too
    dateIntoString = datetime.date.isoformat(date)
    print(dateIntoString)
    print(type(dateIntoString))

def astimeZone():
    d1 = datetime.datetime.now()
 
    # Calling the astimezone() function without
    # any timezone parameter
    d2 = d1.astimezone()

    # Printing the local current date, time and
    # timezone
    print(format(d2))

def dateTimeCombineFunction():
    d = datetime.date.today()
    t = datetime.datetime.now().time()
    print(datetime.datetime.combine(d,t))
    print(d,t)

def ctimeOfDateTime():
    Todays_time = time.time()
  
# Printing today's time
    print(Todays_time)
  
    # Calling the fromtimestamp() function
    # to get date from the current time
    date_From_CurrentTime = datetime.date.fromtimestamp(Todays_time);
    
    # Printing the current date
    print("Date for Timestamp used is: %s"%date_From_CurrentTime);
    
    # Calling the ctime() function over the above date
    print("Today's date: %s"%date_From_CurrentTime.ctime());


def convertingDateIntoString():
    date = datetime.date.today()
    print(datetime.date.isoformat(date))
convertingDateIntoString()

