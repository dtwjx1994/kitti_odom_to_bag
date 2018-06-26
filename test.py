#!/usr/bin/python 
from datetime import datetime
print("Hello, World")

a='2011-09-26 13:02:25.964389445'
b='2.012365465456'
dt = datetime.strptime(a[:-4], '%Y-%m-%d %H:%M:%S.%f')

c=float(datetime.strftime(dt, "%s.%f"))
print(dt)
print(c)
