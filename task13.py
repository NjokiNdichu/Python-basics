attempts=0
if attempts<3:
    email=input("Enter your email: ")
    password=input("Enter your password: ")
    if (email=="admin@mail.com" and password=="Admin@123"):
            print("Login is successful")
    else:
            print("Invalid username and password")
    attempts+=1
else:
    print("You have been blocked!")