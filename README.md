# Covid19-ContactTracing-Python

UPDATE: Please note that with the release of v1.1 of the Crypto Specifications (https://covid19-static.cdn-apple.com/applications/covid19/current/static/contact-tracing/pdf/ExposureNotification-CryptographySpecificationv1.1.pdf) this implementation is now outdated. AES has replaced the HMAC function in v1.1. 

An example implementation of the Covid-19 Contact Tracing concept proposed by Apple/Google.

A demo of the code is available at  [https://repl.it/@owenlo/Covid19-ContactTracing-Simulation](https://repl.it/@owenlo/Covid19-ContactTracing-Simulation)

This code is capable of generating all values for an individual (Trace Key, Daily Trace Key and Rolling Proximity IDs) within a 24-hour period.  In the current implementation (see `simulate2()` function), we simulate the keys and activities of two individuals (Bob and Alice) within a 24-hour period for Day Number 1. We assume Alice is infected with Covid-19 and comes into contact with Bob. Alice's Diagnosis Keys are released, Bob acquires them and is able to determine that he came into contact with an infected person without knowing their identity. 

The Trace Key, Daily Trace Key and 24-hour rolling proximity IDs (each interval is equal to 10 mins) are shown below for Bob and Alice.

```
**********
< Bob >
Trace Key: 4c7cdb6fbe601a804e0e5db27566505bacc398a9e6951c8b4949038958f88a78
Daily Trace Key: 1fad8fc09cabb7740eff63c08494da74
Day Number: 1
**********
Time Interval: 0; Prox ID: ce5833ce3237bf5403700ab0aba2b869
Time Interval: 1; Prox ID: 4a3c4c487d14d2918d75eafc2691817b
Time Interval: 2; Prox ID: 801712480318911400f1b49cb976054b
Time Interval: 3; Prox ID: b8e70049b2393b45dc065669776e849d
Time Interval: 4; Prox ID: 05d72ec0c2ad300b004dfadc0ad17493
Time Interval: 5; Prox ID: 61e56cc3a7c73ea109be66fb4f8bda0f
Time Interval: 6; Prox ID: d366341403e840a1cd07bd3ff2d08dfe
Time Interval: 7; Prox ID: 4ff51db483ebe0228320577468826c77
<--- Truncated to save space --->
```
```
**********
< Alice >
Trace Key: 74ffa27dcf229d1a4ba15f48dfcc88eaa2dc2f409743451a940c1c573857f72d
Daily Trace Key: c7df586124ff46f982e0776735a320b2
Day Number: 1
**********
Time Interval: 0; Prox ID: 9673eeba93a385ef2b8efaed690b9fbf
Time Interval: 1; Prox ID: 5b559293c7a694a919ae4aab79fcbbf3
Time Interval: 2; Prox ID: a51e8f967c83cefc743db6e0a2bb759c
Time Interval: 3; Prox ID: 9094510b85970ab105daef522654945d
Time Interval: 4; Prox ID: a72f4721089a8c5c426eb40186e062aa
Time Interval: 5; Prox ID: 8dd247152014ebf9ac24bc9a6f18677f
Time Interval: 6; Prox ID: 6cc75a9865a334d1ec33d72a59502300
Time Interval: 7; Prox ID: d42bc59e2523e822165d0ed2db74c696
<--- Truncated to save space --->
```

We simulate the scenario of Bob and Alice having an encounter at time intervals 5, 6 and 7 during day number 1. Both Bob and Alice will save each others respective proximity IDs during this time period.

```
Simulation of contact between Bob and Alice has occurred (Day Number: 1; Time Interval: 5;)
Simulation of contact between Bob and Alice has occurred (Day Number: 1; Time Interval: 6;)
Simulation of contact between Bob and Alice has occurred (Day Number: 1; Time Interval: 7;)
```

Next, we assume Alice has been diagnosed with Covid-19:

```
Alice is tested positive for Covid-19 and her diagnosis keys are released to Bob via a third party.
```

Finally, Bob is able to perform contact tracing:

```
Bob performs contact tracing to determine when he came into contact with Alice. His results show:
Bob came into contact with a Covid-19 infected individual (Day Number: 1; Time Interval: 5; Matching Prox ID: 8dd247152014ebf9ac24bc9a6f18677f
Bob came into contact with a Covid-19 infected individual (Day Number: 1; Time Interval: 6; Matching Prox ID: 6cc75a9865a334d1ec33d72a59502300
Bob came into contact with a Covid-19 infected individual (Day Number: 1; Time Interval: 7; Matching Prox ID: d42bc59e2523e822165d0ed2db74c696
``` 

Each of the matching proximity IDs can be mapped back to the Prox IDs generated by Alice as shown earlier in this text.

References:

https://medium.com/asecuritysite-when-bob-met-alice/contact-tracing-the-most-amazing-and-scariest-technology-of-the-21st-century-9fb86d7869e5

https://www.apple.com/covid19/contacttracing/

https://covid19-static.cdn-apple.com/applications/covid19/current/static/contact-tracing/pdf/ContactTracing-CryptographySpecification.pdf
