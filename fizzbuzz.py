#!/usr/bin/env python3
import os

def fizzbuz(n):
    tableau=[]
    for i in range(0, n):
        if i % 5 == 0 and i % 3 ==0:
            tableau.append('fizzbuzz')
        elif i % 5 == 0:
            tableau.append('fizz')
        elif i % 3 == 0:
            tableau.append('buzz')
        else:
            tableau.append(i)
    return tableau

fizzbuz(100)





fi = fizzbuz(100)
print(fi)
