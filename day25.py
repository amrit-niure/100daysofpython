countries = ("Nepal","Argentina","Australia","Japan","Canada")
temp = list(countries)
temp.append("Portugal")
temp.pop(4)
temp[2]="USA"
countries=tuple(temp)
print(countries)

tup1=("Nepal","India")
tup2=("USA","Canada")
cont=tup1+tup2
print(cont)



# tuple methods
tuple1 = (1,2,3,3,4,4,5,6,7,8,6,7,8)
res = tuple1.count(7)
res = tuple1.index(7)
res= len(tuple1)
print("Count of 7 is ",res)