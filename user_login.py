import getpass
username = input("Enter your name:")
password = getpass.getpass("Enter password")

if username == "Alex" and password == "123":
    print ("Welcome ", username)
    
else:
    print ("Wrong username or password!")
    

