basic=float(input("Enter your basic salary: "))
benefits=float(input("Enter your benefits: "))
gross=basic+benefits
if (gross>0 and gross<=5999):
                nhif=150
elif(gross>=6000 and gross <=7999):
                nhif=300
                print(nhif)
elif(gross>=8000 and gross<=11999):
                nhif=400
                print(nhif)
elif(gross>=12000 and gross<=14999):
                nhif=500
                print(nhif)
elif(gross>=15000 and gross<=19999):
                nhif=600
                print(nhif)
elif(gross>=20000 and gross<=24999):
                nhif=750
                print(nhif)
elif(gross>=25000 and gross<=29999):
                nhif=850
                print(nhif)
elif(gross>=30000 and gross<=34999):
                nhif=900
                print(nhif)
elif(gross>=35000 and gross<=39999):
                nhif=950
                print(nhif)
elif(gross>=40000 and gross<=44999):
                nhif=1000
                print(nhif)
elif(gross>=45000 and gross<=49999):
                nhif=1100
                print(nhif)
elif(gross>=50000 and gross<=59999):
                nhif=1200
                print(nhif)
elif(gross>=60000 and gross<=69999):
                nhif=1300
                print(nhif)
elif(gross>=70000 and gross<=79999):
                nhif=1400
                print(nhif)
elif(gross>=80000 and gross<=89999):
                nhif=1500
                print(nhif)
elif(gross>=90000 and gross<=99999):
                nhif=1600
                print(nhif)
elif(gross>=100000):
                nhif=1700
                print(nhif)
else:
                print("Enter an amount")


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

net_salary= gross- (nhif + nssf1 + payee)
print("Your net salary is:" + str(net_salary))
