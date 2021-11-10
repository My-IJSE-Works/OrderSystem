import getpass
class Users:
    def __init__(self):
        self.name = 'User'
        self.cus = self.Customer()

    def show(self):
        print("SELECT YOUR PARTH")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        print(" ")
        a = input("Enter Number : ")
        print(" ")
        if(a == "1"):
            d1 = outer.cus
            print()
            d1.home()
        elif(a == "2"):
            d2 = outer.ad
            print()
            d2.display()
        elif(a == "3"):
            exit()
        else:
            print("Choose a valid option")

    class Customer:
        def __init__(self):
            self.name = 'Parth'
            self.reg = self.Register()
        
        def home(self):
            print("SELECT YOUR PARTH")
            print("1. Sign UP")
            print("2. Login")
            print("3. Exit")
            print(" ")
            a = input("Enter Number : ")
            print(" ")
            if(a == "1"):
                d3 = outer.cus.reg
                print()
                d3.register()
            elif(a == "3"):
                exit()
            else:
                print("Choose a valid option")

        class Register:

            def register(self):
                n = input("Name: ")
                p = getpass.getpass("Password: ")
                print(" ")
                file = open("db/user_detail.txt","a")
                file.write(n+" , "+p+"\n")
                print(" ")

outer = Users()
outer.show()


out = outer.cus
out.home()

  
gfg2 = outer.cus.reg
gfg2.register()