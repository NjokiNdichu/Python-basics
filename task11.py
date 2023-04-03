from datetime import date
today=date.today()
print(today)
today=str(today)
year_today=today[0:4]
print (year_today)
date_born=(input("Enter date of birth(yyyy-mm-dd): "))
date_born=str(date_born)
year_born=date_born[0:4]
print(year_born)
year_diff=float(year_today)-float(year_born)
print (year_diff)
month_today=today[5:7]
print(month_today)
month_born=date_born[5:7]
print(month_born)
month_diff=float(month_today)-float(month_born)
print(month_diff)
