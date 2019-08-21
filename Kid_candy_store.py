# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []

for candy in candyList:
    print("[" + str(candyList.index(candy)) + "]" + candy)

while allowance >= 1 : 
    user_candy= int((input("What is your favorite candy? Enter the number found in the brackets above here: ")))
    candyCart.append(candyList[user_candy])
    allowance = allowance - 1
    
print("Given your allowance of 5 candies your favorite candies are " + str(candyCart))
    
    

