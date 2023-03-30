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
taxableincome=gross-nssf1
print("taxable income is:" + str(taxableincome))
if ((float(taxableincome)<=24000)):
                payee= 0
                print(payee)
elif(float(taxableincome)>24000 and float(taxableincome)<=32333):
                payee=((0.1*24000)+((float(taxableincome)-24000)*0.25))-2400
                print(payee)
elif(float(taxableincome)>32333):
                payee=(((float(taxableincome)-32333)*0.3)+(0.1*24000)+(8333*0.25))-2400
                print(payee)
else:
                print("Enter salary amount from 0")