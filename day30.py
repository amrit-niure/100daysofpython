# def facto(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*facto(n-1)
# print(facto(4))




# def fibo(n):
#     if n<0:
#         print("Incorrect Output")
#     elif n==0:
#         return 0
#     elif n==1 or n==2:
#         return 1
#     else:
#         return fibo(n-1)+fibo(n-2)

# print(fibo(3))
def fibo(n):
    a=0
    b=1

    if n<0:
        print("Incorrect Output")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(1,n):
            c=a+b
            a=b
            b=c
        return b
print(fibo(9))