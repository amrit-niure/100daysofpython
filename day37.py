def func1():
    try:
        l=[3,4,5]
        i = int(input("Enter the index:")
        print(l[i]))
        return 1
    except:
        print("SOme error occoured")
        return 0
    finally:
        print("I am always executed.")

x= func1()
print(x)