#!/usr/bin/env python3

## Create a dictionary
switch = {'hostname': 'sw1', 'ip': '10.0.1.1', 'version':'1.2', 'vendor':'cisco'}

## display parts of the dictionary
print( switch['hostname'] )
print( switch['ip'] )

## request a 'fake' key
print( "First test -get()" )
print( switch('lynx') )

print( "Second test -.get()" )
print( switch.get('lynx', "THE KEY IS IN ANOTHER CASTLE!") )

print( "Third test - .get()" )
print( switch.get('version') )
