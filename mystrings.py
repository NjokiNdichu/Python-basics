first_name_one = "JOHN"
first_name_two = "    JOHN    "
#lower
first_name_one=first_name_one.lower()
print(first_name_one)
#strip
first_name_one= first_name_two.strip()
print(first_name_two)
#Both strip and lower
first_name_two=first_name_two.strip().lower()
print(first_name_two)
#count
count_o=first_name_one.lower().count('o')
print(count_o)
#index
print(first_name_one[1:3])
#type-used to know the type of data you're working with
print(type(first_name_one))
#split
mystring= "This is a list of items;item1;item2;item3"
my_split_string=mystring.split(";")
print(my_split_string)
#concatenate-joining or adding strings

