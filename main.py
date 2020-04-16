#!/usr/bin/env python
# Example implementation of the Contact Tracing Crypto Specification as defined by Apple/Google:
# https://www.apple.com/covid19/contacttracing/
#
# This implementation is based on code originally written by Prof. Bill Buchanan. See following article for more details:
# https://medium.com/asecuritysite-when-bob-met-alice/contact-tracing-the-most-amazing-and-scariest-technology-of-the-21st-century-9fb86d7869e5

import key_schedule
import binascii
import person

def generateProxIds(daily_trace_key):
  """Generate all prox IDs for a 24 hour period based on Daily Trace Key"""
  prox_ids = []
  
  for timeInterval in range(0, 144): #each interval is equal to 10 minutes of time.
    prox_ids.append(key_schedule.rolling_prox_id(daily_trace_key, timeInterval))

  return prox_ids

def simulate():
  """ Simulate the Rolling Prox ID for a 24-hour window of Day Number 1. """
  
  dayNumber = 1

  trace_key = key_schedule.trace_key() # Begin contact tracing and generate a Trace Key
  daily_trace_key = key_schedule.daily_trace(1, trace_key) # Generate a rolling 24-hour Daily Tracing Key

  print("**********")
  print("Trace Key: " + binascii.hexlify(trace_key).decode())    
  print("Daily Trace Key: " + binascii.hexlify(daily_trace_key).decode())
  print("Day Number: " + str(dayNumber))
  print("**********")
  
  for i, prox_id in enumerate(generateProxIds(daily_trace_key)):
    print("Time Interval: " + str(i) + "; Prox ID: " + binascii.hexlify(prox_id).decode())

def simulate2():
  dayNumber = 1 #We only simulate 1 day in this scenario

  # Create actors Bob and Alice. In this scenario, we assume Alice is infected with Covid-19.
  bob = person.Person("Bob")
  alice = person.Person("Alice")

  # Both Bob and Alice set their daily trace keys for a specified day.
  # The proximity IDs for their 24-hour of daily activity is automatially set 
  # when this function is called.
  bob.setDailyTraceKey(dayNumber)
  alice.setDailyTraceKey(dayNumber)

  # Uncomment below functions to print all keys produced by Alice and Bob in this simulation
  bob.printResults()  
  alice.printResults() 

  # We simulate Alice coming into contact with Bob at time interval 5 to 7 on Day Number 1
  # Both Alice and Bob store each others respective prox IDs observed during these time intervals.

  for i in range(5, 8):
    alice.setContact(bob.prox_ids[i])
    bob.setContact(alice.prox_ids[i])
    print("Simulation of contact between Bob and Alice has occurred (Day Number: %d; Time Interval: %d;)" % (dayNumber, i))

  print("\nAlice is tested positive for Covid-19 and her diagnosis keys are released to Bob via a third party.")
  aliceDiagnosisKeys = alice.getDiagnosisKeys()

  print("\nBob performs contact tracing to determine when he came into contact with Alice. His results show:")
  bobContactTracingResult = bob.doContactTracing(aliceDiagnosisKeys)  

  for t in bobContactTracingResult:
    print("Bob came into contact with a Covid-19 infected individual (Day Number: %d; Time Interval: %d; Matching Prox ID: %s" % (t[0], t[1], binascii.hexlify(t[2]).decode()))    

if __name__ == "__main__":
  #simulate()
  simulate2()
