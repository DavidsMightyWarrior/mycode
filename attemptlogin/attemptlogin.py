#!/usr/bin/env python3
# parse keystone.common.wsgi and return number of failed login attempts
loginfail = 0 
keystone_file = open('./attemptlogin/keystone.log','r')
keystone_file_lines=keystone_file.readlines()
for i in range(len(keystone_file_lines)):
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail += 1 # this is the same as loginfail = loginfail + 1
print('The number of failed log in attempts is ' + str(loginfail))
