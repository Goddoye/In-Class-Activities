# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 12:05:14 2019

@author: oddoy
"""

# @TODO: Write a function that returns the arithmetic average for a list of numbers


def average(list):
    return (sum(list)/len(list))

# Test your function with the following:
print(average([1, 5, 9]))
print(average(range(11)))
