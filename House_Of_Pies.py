print("Welcome to the House of Pies! Here are our pies: ")

pies = ["(1) Pecan", "(2) Apple Crisp", "(3) Bean", "(4) Banoffee",  "(5) Black Bun", "(6) Blueberry", "(7) Buko", "(8) Burek",  "(9) Tamale", "(10) Steak"]

print(pies)

order_up= input("Would you like a pie? Yes or No: ")

order_list = []

while order_up == "Yes":
    user_pie= ((int(input("Which pie would you like us to start making? Enter the number of the pie: ")))-1)
    order_list.append(pies[user_pie])
    pie_order= str(pies[user_pie])
    print("Great! We'll have that " + pie_order + " right out for you.")
    next_order= input("Would you like another pie? Sure or Nah: ")
	
    if next_order == "Sure":
        next_pie = ((int(input("Which pie would you like us to start making? Enter the number of the pie: ")))-1)
        order_list.append(pies[next_pie])
        pie_order1= str(pies[next_pie])
        print("Great! We'll have that "+ pie_order1 +" right out for you.")
        next_order= input("Would you like another pie? Sure or Nah: ")
    elif next_order == "Nah":
        print("Thank you for your shopping with us. Your order is: ")
        print (order_list)
        break
    else: 
        print("I dont know what you enter.")