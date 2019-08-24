# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 10:48:54 2019

@author: oddoy
"""

personal = {"Name": "George Oddoye", 
            "Age":"27",
            "Hobbies": ["Cycling", "Boxing","Working Out","Coding"],
            "Wake up": {"Mon":"9:00 am","Wed":"7:00 am", "Fri":"9:30 am"}
            }

print(f'My name is {personal["Name"]} and my hobbies include {personal["Hobbies"]}. I usually get up on {personal["Wake up"]}')