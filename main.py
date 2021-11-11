print("\n" * 1)                  

import datetime                    
import os                          

list_foods = []                  
                
list_item_price = [0] * 100        
                                  
navigator_symbol = "/" 
if os.name == "nt":
    navigator_symbol = "\\" 

def def_default():
    global list_foods, list_item_price                   
def_default() 

def def_main():
   while True:
        print("*" * 28 + "FOOD ORDERING SYSTEM" + "*" * 24 + "\n") 
        print("*" * 31 + "MAIN MENU" + "*" * 32 + "\n"     
              "\t(C) CUSTOMER\n"                              
              "\t(A) ADMIN\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper()    
        if (len(input_1) == 1):                                           
            if (input_1 == 'C'):                                          
                print("\n" * 1)                                        
                c_user()                                          
                break                                                     
            elif (input_1 == 'A'):                                        
                print("\n" * 1)                                        
                c_user()                                             
                break                                                                                                         
            elif (input_1 == 'E'):                                        
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n")           
                break                                                     
            else:                                                                                 
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + ").Something Went Wrong ,Try again!")     
        else:                                                                                     
            print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

def c_user():                                                                               
    while True:                                             
        print("*" * 31 + "LOGIN AND SING UP PAGE" + "*" * 31 + "\n"    
              "\t(S) SING UP\n"
              "\t(L) LOGIN\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Wish: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == 'S'):  
                print("\n" * 1)
                c_register()
                break
            elif (input_1 == 'L'):
                print("\n" * 1)
                c_login() 
                break
            elif (input_1 == 'E'):
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!") 
        else:
            print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

def c_register():
    n = input("Name: ")
    p = input("Password: ")
    success = True
    print(" ")
    file = open('files'+navigator_symbol+'customers', 'a')
    file.write(n+" - "+p+"\n")
    print(" ")
    if(success):
        print("-" * 20 + " Hey " + n + "-" * 20)
        print(" ")
        order()
    else:
        print("Something Went Wrong ,Try again!")
    

def c_login():
    u = input("Username: ")
    p = input("Password: ")
    success = False
    file = open('files'+navigator_symbol+'customers', 'r')
    for i in file:
        a,b = i.split(" - ")
        b = b.strip()
        if(a==u and b==p):
            success = True
            break
    file.close()
    if(success):
        print("-" * 20 + "Login Successful" + "-" * 20)
        print()
        order()
    else:
        print("Incorrect username or password")


def order():
   while True:
        print("*" * 31 + "ORDER MENU" + "*" * 32 + "\n"     
              "\t(O) ORDER\n"                              
              "\t(L) Item List\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Operation: ")).upper()    
        if (len(input_1) == 1):                                           
            if (input_1 == 'O'):                                          
                print("\n" * 1)                                        
                def_order_menu()                                          
                break                                                     
            elif (input_1 == 'L'):                                        
                print("\n" * 1)                                        
                def_view()                                              
                break                                                    
            elif (input_1 == 'E'):                                        
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n")           
                break                                                     
            else:                                                                                 
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + ").Something Went Wrong ,Try again!")     
        else:                                                                                     
            print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!") 

def def_order_menu():                                                                               
    while True:                                             
        print("*" * 31 + "ORDER PAGE" + "*" * 31 + "\n"    
              "\t(F) FOODS AND DRINKS\n"
              "\t(M) MAIN MENU\n"
              "\t(E) EXIT\n" +
              "_" * 72)

        input_1 = str(input("Please Select Your Wish: ")).upper() 
        if len(input_1) == 1:
            if (input_1 == 'F'):  
                print("\n" * 1)
                def_food_drink_order()
                break
            elif (input_1 == 'M'):
                print("\n" * 1)
                def_main() 
                break
            elif (input_1 == 'E'):
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n")
                break
            else:
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!") 
        else:
            print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

def def_full_file_reader():                                                                        
    file_foods = open('files'+navigator_symbol+'list_foods', 'r') 
    for i in file_foods: 
        list_foods.append(str(i.strip())) 
    file_foods.close()



    i = 0
    while i <= (len(list_foods) - 1): 
        if 'Rs' in list_foods[i]:
            list_foods[i] = str(list_foods[i][:list_foods[i].index('Rs') - 1]) + ' ' * (20 - (list_foods[i].index('Rs') - 1)) + str(list_foods[i][list_foods[i].index('Rs'):])
        i += 1

def_full_file_reader()
def def_file_sorter(): 
    global list_foods, list_drinks
    list_foods = sorted(list_foods)
    

    i = 0
    while i < len(list_foods):
        list_item_price[i] = float(list_foods[i][int(list_foods[i].index("Rs") + 2):]) 
        i += 1

   
def_file_sorter()
def def_food_drink_order():
    while True:
            print("*" * 16 + "ORDER FOODS" + "*" * 16)
            print("-" * 40)
            print(" |NO| |FOOD NAME|         |PRICE|")
            print("-" * 40)

            i = 0
            while i < len(list_foods):
                var_space = 1
                if i <= 8:                      
                    var_space = 2

                if i < len(list_foods):
                    food = " (" + str(i + 1) + ")" + " " * var_space + str(list_foods[i]) + "  || " 
                else:
                    food = " " * 36
                
                print(food)
                i += 1

            print("\n (M) MAIN MENU                   (P) PAYMENT                   (E) EXIT\n" + "_" * 72)


            input_1 = input("Please Select Your Wish: ").upper() 
            if (input_1 == 'M'):
                print("\n" * 1)
                exit 
                break
            if (input_1 == 'E'):
                print("*" * 32 + "THANK YOU COME AGAIN" + "*" * 31 + "\n") 
                break
            if (input_1 == 'P'):
                print("\n" * 1)
                exit 
                break
            try:        
                int(input_1)
                if ((int(input_1) <= len(list_foods) and int(input_1) > 0)):
                     try:
                        print("\n" + "_" * 72 + "\n" + str(list_foods[int(input_1) - 1])) 
                     except:
                        pass
            except:
                print("\n" * 1 + "ERROR: Invalid Input (" + str(input_1) + "). Something Went Wrong ,Try again!")

def_main() 