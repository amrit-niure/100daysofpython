# def average(a,b):
#     print("The average is ",(a+b)/2)
# average(4,6)


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum +i
    print("Average is : ",sum/len(numbers))

average(5,6)