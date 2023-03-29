speed=float(input("Enter speed of car:"))
if speed<70:
    print("Ok")
else:
    demerits=(speed-70)/5
    demerits=str(demerits)
    print("Points:" + demerits)
    if float(demerits)>12:
        print("license suspended")