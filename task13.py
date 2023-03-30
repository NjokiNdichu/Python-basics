email=input("Enter your email: ")
password=input("Enter your password: ")
attempts=3
for i in range(1, attempts):
    if (email=="admin@mail.com" and password=="Admin@123"):
        print("Login is successful")
    else:
        print("Invalid username and password")

if attempts>3:
    print("You have been blocked")
