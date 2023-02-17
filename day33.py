dic = {
    "Harry":"Human Being",
    "Spoon":"Object"
}

print(dic["Harry"])

info ={'name':'Karan', 'age':19 , 'eligible': True }
print(info)
#print(info['name2'])  # it thorws and error if the key is not in the dictionary
print(info.get('name2')) # it does not thorws and error if the key is not in the dictionary
print(info.keys())
for key in info.keys():
    print(f"The vaalue corresponding to the key {key} is {info[key]}")

print(info.items())
for key, value in info.items():
    print(f"The vaalue corresponding to the key {key} is {value}")
