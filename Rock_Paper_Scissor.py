# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:58:31 2019

@author: oddoy
"""

# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if (computer_choice == "r" and user_choice == "p"):
    print("You chose paper and the computer chose rock.")
    print("You win!")
        
elif (computer_choice == "r" and user_choice == "r"):
    print("You chose rock and the computer chose rock.")
    print("Draw, try again.")

elif (computer_choice == "r" and user_choice == "s"):
    print("You chose scissors and the computer chose rock.")
    print("You lose, try again!")

elif (computer_choice == "p" and user_choice == "s"): 
    print("You chose scissors and the computer chose paper.")
    print("You win!")
    
elif (computer_choice == "p" and user_choice == "p"): 
    print("You chose paper and the computer chose paper.")
    print("Draw, try again.")
    
elif (computer_choice == "p" and user_choice == "r"):
    print("You chose rock and the computer chose paper.")
    print("You lose, try again!")
    
elif (computer_choice == "s" and user_choice == "r"): 
    print("You chose rock and the computer chose scissor.")
    print("You win!")
    
elif (computer_choice == "s" and user_choice == "s"): 
    print("You chose scissor and the computer chose scissor.")
    print("Draw, try again.")
    
elif (computer_choice == "s" and user_choice == "p"):
    print("You chose paper and the computer chose scissor.")
    print("You lose, try again!")
    
else:
    print("I dont understand that.")
    print("Please choose from r: rock, p: paper, s: scissor")