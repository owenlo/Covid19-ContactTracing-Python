#!/usr/bin/env python
# Example implementation of the Contact Tracing Crypto Specification as defined by Apple/Google:
# https://www.apple.com/covid19/contacttracing/
#
# This implementation is based on code originally written by Prof. Bill Buchanan. See following article for more details:
# https://medium.com/asecuritysite-when-bob-met-alice/contact-tracing-the-most-amazing-and-scariest-technology-of-the-21st-century-9fb86d7869e5

import key_schedule
import binascii

def generateProxIds(daily_trace_key):
  """Generate all prox IDs for a 24 hour period based on Daily Trace Key"""
  prox_ids = []
  
  for timeInterval in range(0, 144): #each interval is equal to 10 minutes of time.
    prox_ids.append(key_schedule.rolling_prox_id(daily_trace_key, timeInterval))

  return prox_ids

if __name__ == "__main__":
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

