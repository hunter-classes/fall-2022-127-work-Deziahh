timeNowString = input("What time is it now? (In Hours)")
hoursToWaitString = input ("How many hours do you want to wait for the alarn to go off?")

timeNowInt = int(timeNowString)
hoursToWaitInt = int(hoursToWaitString)

hours = timeNowInt + hoursToWaitInt

timeOfDay = hours % 24
print(timeOfDay)
