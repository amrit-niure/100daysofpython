l = [67,56,1,2,4,6]
print(l)
l.append(7)
l.sort()
print(l)
l.reverse()
print(l)
print(l.index(2))
print(l.count(2))

# m= l.copy()
# m[0]=0
# print(l)

l.insert(1, 899) # it inserts 899 in index 1 
print(l)

m=[900, 1000, 1100]
k=l+m
# l.extend(m)
print(l)
print(k)