#!/usr/bin/env python3

mydiction={"10.0.0.1": "Gateway"}

for x in mydiction.keys():
  print("The IP address " + x + " is mapped to " + mydiction[x])
