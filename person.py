import key_schedule, binascii

class Person:
    def __init__(self, name):
        self.name = name
        self.prox_ids = []       
        self.infected = False
        self.traceKey = key_schedule.trace_key()      
        self.dailyTraceKey = None
        self.dayNumber = 1  
        self.diagnosisKeys = [] #A list of personal diagnosis keys. Tuple of (DayNumber, DailyTraceKey). 
        self.contact = [] #A list of contacts with other people. A tuple of (DayNumber, ProxID). 

    def setDailyTraceKey(self, dayNumber):
        self.dayNumber = dayNumber
        self.dailyTraceKey = key_schedule.daily_trace(self.dayNumber, self.traceKey)
        self.diagnosisKeys.append((self.dayNumber, self.dailyTraceKey))
        self.__generateProxIDs()

    def __generateProxIDs(self):
        self.prox_ids.clear()
        for timeInterval in range(0, 144): #each interval is equal to 10 minutes of time.
          prox_id = key_schedule.rolling_prox_id(self.dailyTraceKey, timeInterval)
          self.prox_ids.append(prox_id)

    def setContact(self, prox_id):
        self.contact.append((self.dayNumber, prox_id))

    def getDiagnosisKeys(self):
        return self.diagnosisKeys

    def doContactTracing(self, diagnosisKeys):
        contact_match =[] #Stores a list of possible contacts which occurred with Covid-19 infected individual. A tuple of (DayNumber, TimeInterval, Matching Prox ID).
        for dk in diagnosisKeys:
          for timeInterval in range(0, 144): #each interval is equal to 10 minutes of time.              
            prox_id = key_schedule.rolling_prox_id(dk[1], timeInterval)
            for c in self.contact:        
              if dk[0] == c[0] and prox_id == c[1]: #If day and prox ID matches with contact list.              
                contact_match.append((dk[0], timeInterval, prox_id))
        return contact_match

    def printResults(self):
        print("**********")
        print("< " + self.name + " >")
        print("Trace Key: " + binascii.hexlify(self.traceKey).decode())    
        print("Daily Trace Key: " + binascii.hexlify(self.dailyTraceKey).decode())
        print("Day Number: " + str(self.dayNumber))
        print("**********")        
  
        for i, prox_id in enumerate(self.prox_ids):
          print("Time Interval: " + str(i) + "; Prox ID: " + binascii.hexlify(prox_id).decode())
        
        print("\n")
      