# with open('file.txt','r') as f:
#     print(type(f))
#     # move to the 10th byte in the file
#     f.seek(10)

#     # read the next 5 bytes 
#     print(f.tell())
#     data = f.read(5)
#     print(data)


with open('sample.txt','w') as f:
    f.write("Hello World")
    f.truncate(5)
    # read the next 5 bytes 
with open("sample.txt",'r') as f:
    print(f.read())