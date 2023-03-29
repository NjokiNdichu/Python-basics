marks=float(input("Enter student marks:"))
if marks>0 and marks<100:
    if marks>79:
        print("A")
    if marks>=60 and marks<=79:
        print("B")
    if marks>=50 and marks<=59:
        print("C")
    if marks>=40 and marks<=49:
        print("D")
    if marks<40:
        print("E")
else:
    print("Enter marks within given range")