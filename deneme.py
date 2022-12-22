printf("Hello World")﻿
def azalt(a):
    if len(a) < 1:
       return a
    else:
         print(a)
         return azalt(a[1:])
print(azalt('Hello World'))         
