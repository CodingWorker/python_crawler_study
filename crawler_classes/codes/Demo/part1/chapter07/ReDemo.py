#-*- coding:utf-8 -*-
import re

str = 'hello world'
pattern = r'(?P<demo>hello)(abc)*'
regx = re.compile(pattern)
result1 = regx.match(str)
result2 = re.match(regx,str)
print result1
print result2

if result1:
    print result1.group()
    print result1.lastindex  #1
    print result1.lastgroup  #demo
if result2:
    print result2.re.pattern
    print result1.lastindex  #1
    print result1.lastgroup  #demo

print result1.groups().__len__()  #1
print result1.groups()[0]         #hello
print result1.groups()[1]
print result1.groups('aaa')[1]
print result2.groupdict('aabb')
print result1.group("demo")