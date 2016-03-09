#!/usr/bin/python2

from subprocess import Popen, PIPE, STDOUT

p = Popen(['./addone'], stdout=PIPE, stdin=PIPE, stderr=PIPE)

num = raw_input("Enter a number:")

output = p.communicate(input=str(num))[0]

print(num +  " + 1 = " + output)
