ls1=list(range(1,20))
print(ls1)
for i in ls1:
    print("i is ",i)

mydata=["Nrb", "Msa", "Ksm", "Eld", "Nkr"]
mydataindexes= list(range(0,len(mydata)))
for i in mydataindexes:
    if mydata[i] == 'Ksm':
        mydata[i]= 'Kisumu'
        break
    else:
        pass
print(mydata)