mynum=float(input("Enter number to test:"))
if (mynum>=0 and mynum<=100):
 if mynum>70:
    print("High")
 elif mynum<70 and mynum>40:
    print("Medium")
 else:
    print("Low")
else:
    print("Enter number between 0 and 100")