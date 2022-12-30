import time
# from time import gmtime, strftime
t = time.strftime('%T')
print(t)
hour= int(time.strftime('%H'))
print(hour)

if(hour>0 & hour <12):
    print("Good Morning Sir !")
elif(hour>12 & hour <17):
    print("Good Afternoon Sir !")
elif:
    print("Good Night Sir !")
    

# s = strftime("%A, %D %B %Y %H:%M:%S + 1010", gmtime())
# print("Example 1:", s)

# s = strftime("%C")
# print("Example 4:", s)
 

 