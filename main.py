print("                      ##### ABC Pastry Shop #####")
print("=================================================================")
print(" ")
print("------------------------- W E L C O M E ! -----------------------")
print(" ")


food = ["Fish Cutlet", "Chicken Cutlet", "Fish Bun", "Fish Roti", "Patties", "Fish Rolls", "Pan Rolls", "Burger", "Sausages Bun"]
prices = [25.00,30.00,45.00,20.00,50.00,55.00,50.00,45.00]

myorderFood = []
myorderCost = []


d = [ [1,"Fish Cutlet", 25.00],
     [2,"Chicken Cutlet", 30.00],
     [3,"Fish Roti", 45.00],
     [4,"Patties", 20.00],
     [5,"Fish Rolls", 50.00],
     [6,"Pan Rolls", 55.00],
     [7,"Burger", 50.00],
     [8,"Sausages Bun", 45.00]
    ]

h = ["Item Number","Food Name","Price (Rs.)"]

print(tabulate(d, h, tablefmt="grid"))

print(" ")

order = input("Can I take your order ?(yes/no) : ")
if order == "no":
    exit()
else:
    print("Thank you")
print(" ")

nextOrder = True

while nextOrder == True:
    foodOrder = input("Please enter item number: ")
    print(" ")
    if foodOrder == "1":
        myorderFood.append(food[0])
        myorderCost.append(prices[0])

    elif foodOrder == "2":
        myorderFood.append(food[1])
        myorderCost.append(prices[1])

    elif foodOrder == "3":
        myorderFood.append(food[2])
        myorderCost.append(prices[2])

    elif foodOrder == "4":
        myorderFood.append(food[3])
        myorderCost.append(prices[3])

    elif foodOrder == "5":
        myorderFood.append(food[4])
        myorderCost.append(prices[4])

    elif foodOrder == "6":
        myorderFood.append(food[5])
        myorderCost.append(prices[5])

    elif foodOrder == "7":
        myorderFood.append(food[6])
        myorderCost.append(prices[6])

    elif foodOrder == "8":
        myorderFood.append(food[7])
        myorderCost.append(prices[7])

    else:
        print ("Not on Menu")
        print(" ")
    finished = input("Have you finished ordering ?(yes/no) : ")
    if finished == "no":
        nextOrder = True
    else:
        nextOrder = False

print(" ")    
print (myorderFood)
print(" ")
print(myorderCost)
print(" ")














