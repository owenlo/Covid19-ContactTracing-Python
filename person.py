import key_schedule, binascii

class Person:
    def __init__(self, name):
        self.name = name
        self.prox_ids = []       
        self.infected = False
        self.traceKey =  key_schedule.trace_key()
        self.dailyTraceKey = None
        self.dayNumber = 1

    def setDailyTraceKey(self, dayNumber):
        self.dayNumber = dayNumber
        dailyTraceKey = key_schedule.daily_trace(self.dayNumber, self.traceKey)
        self.dailyTraceKey = dailyTraceKey

    def generateProxID(self, timeInterval):
        prox_id = key_schedule.rolling_prox_id(self.dailyTraceKey, timeInterval)
        self.prox_ids.append((self.dayNumber, prox_id))

    def setInfected(self, state = False):
        self.infected = state

    def printResults(self):
        print("**********")
        print("< " + self.name + " >")
        print("Trace Key: " + binascii.hexlify(self.traceKey).decode())    
        print("Daily Trace Key: " + binascii.hexlify(self.dailyTraceKey).decode())
        print("Day Number: " + str(self.dayNumber))
        print("**********")
  
        for i, prox_id in enumerate(self.prox_ids):
          print("Time Interval: " + str(i) + "; Prox ID: " + binascii.hexlify(prox_id[1]).decode())
      