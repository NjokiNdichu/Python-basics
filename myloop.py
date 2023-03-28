ls1=list(range(1,20))
print(ls1)
for i in ls1:
    print("i is ",i)

mydata=["Nrb", "Msa", "Ksm", "Eld", "Nkr"]
for i in list(range(0,len(mydata))):
    if mydata[i] == 'Ksm':
        mydata[i]= 'Kisumu'
    else:
        pass
print(mydata)