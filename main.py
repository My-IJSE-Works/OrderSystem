class MainClass:

    def register(self):
        n = input("Name: ")
        p = input("Password: ")
        print(" ")
        file = open("user_detail.txt","a")
        file.write(n+","+p+"\n")
        print(" ")

    def login(self):
        u = input("Username: ")
        p = input("Password: ")
        success = False
        file = open("user_detail.txt","r")
        for i in file:
            a,b = i.split(",")
            b = b.strip()
            if(a==u and b==p):
                success = True
                break
        file.close()
        if(success):
            print("----------------Login Successful----------------")
        else:
            print("Incorrect username or password")
        
    def home(self):
        print("SELECT YOUR PARTH")
        print("1. Sign UP")
        print("2. Login")
        print("3. Exit")
        print(" ")
        a = input("Enter Number : ")
        print(" ")
        if(a == "1"):
            self.register()
        elif(a == "2"):
            self.login()
        elif(a == "3"):
            exit()
        else:
            print("Choose a valid option")

    def show(self):
        print("SELECT YOUR PARTH")
        print("1. Customer")
        print("2. Admin")
        print("3. Exit")
        print(" ")
        a = input("Enter Number : ")
        print(" ")
        if(a == "1"):
            self.home()
        elif(a == "2"):
            self.login()
        elif(a == "3"):
            exit()
        else:
            print("Choose a valid option")

class_instance = MainClass()
class_instance.show()
class_instance.home()