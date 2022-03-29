class ClockTime:
    def __init__(self):
        currHour = 0
        currMin = 0 
        currSec = 0
        hourInput = int(input("Enter hour: "))
        minInput = int(input("Enter minute: "))
        secInput = int(input("Enter second: "))
        self.setHour(hourInput)
        self.setMinute(minInput)
        self.setSeconds(secInput)
        self.setTime(hourInput, minInput, secInput)
        self.showTime()

    def setHour(self, newHour):
        self.currHour = newHour % 24
        return

    def setMinute(self, newMin):
        self.currMin = newMin % 60
        return

    def setSeconds(self, newSec):
        self.currSec = newSec % 60
        return

    def setTime(self, newHour, newMin, newSec):
        self.setHour(newHour)
        self.setMinute(newMin)
        self.setSeconds(newSec)
        return

    def showTime(self):
        print("Current time: " + str(self.currHour) + ":"+ str(self.currMin) + ":" + str(self.currSec))
        return 0

clock = ClockTime()