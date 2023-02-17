# a = int(input("Enter any value between 5 and 9"))
# if(a<5 and a>9):
#     raise ValueError("Value should be between 5 and 9") #in python we can raise custom errors by using the raise keyword


# defining custom errors 
a =input("Enter any numeric value:")
try:
    if(int(a)>5 and int(a)<9):
        raise ValueError("The number is either lesser than 5 or bigger than 9")
except:
    if a!='quit':
        raise ValueError("You entered a string other than quit.")