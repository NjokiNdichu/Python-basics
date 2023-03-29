num=input("Enter your phone number: ")
if (num[0]=="0" and num[1]=="7"):
    num="+254" + num[1:]
    print(num)
elif (num[0]=="0" and num[1]=="1"):
    num="+254" + num[1:]
    print(num)
elif (num[0]=="7"):
    num="+254" + num
    print(num)
elif (num[0]=="2" and num[1]=="5" and num[2]=="4"):
    num="+" + num
    print(num)
else:
    print("false")
   


