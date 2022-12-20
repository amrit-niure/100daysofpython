marks = [3,5,6,"Amrit"]
print(marks)
print(marks[-3])#negative index
print(marks[len(marks)-3]) # positive index
print(marks[1:]) # starting from index one it will go all the way to ending
print(marks[1:4])# 4 is not included 

print(type(marks))


if 7 in marks:
    print("Yes")
else:
    print("No")

if "am" in marks:
    print("yes")
else:
    print("No")