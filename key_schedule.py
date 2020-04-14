import os

from cryptography.hazmat.primitives import hashes, hmac
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.backends import default_backend

def trace_key():
  """The Tracing Key is generated when contact tracing is enabled on the device and is securely stored on the device."""
  tk = os.urandom(32) #Generate a 32-byte tracing key.
  return tk

def daily_trace(dayNumber, traceKey):
  """A Daily Tracing Key is generated for every 24-hour window where the protocol is advertising."""
  
  hkdf = HKDF(algorithm=hashes.SHA256(), #Setup HKDF
              length=16, 
              salt=None, 
              info=str.encode("CT-DTK" + str(dayNumber)),
              backend=default_backend()) 
  
  dtk_i = hkdf.derive(traceKey)
  return dtk_i

def rolling_prox_id(dailyTraceKey, timeIntervalNum):
  """The Rolling Proximity Identifiers are privacy-preserving identifiers that are sent in Bluetooth Advertisements."""
  h = hmac.HMAC(dailyTraceKey, hashes.SHA256(), backend=default_backend())  
  h.update(str.encode("CT-RPI" + str(timeIntervalNum)))
 
  return  h.finalize()[:16]

