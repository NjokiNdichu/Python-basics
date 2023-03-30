
basic=float(input("Enter your basic salary: "))
benefits=float(input("Enter your benefits: "))
gross=basic+benefits
if (gross<18000):
    nssf1=0.06*gross
    print(nssf1)
else:
    nssf1=1080
    print(nssf1)
nssf2=nssf1*2
print(nssf2)