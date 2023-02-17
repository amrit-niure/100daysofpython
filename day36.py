a = input ("Enter the number:")
print(f"Multiplication table of {a} is :")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
# except Exception as e:
#     print(e)
except ValueError:
    print("Number entered is not an integer.")

except IndexError:
    print("Index error")
    
# except:
#     print("Invalid Input")

print("Some lines of code")
print("End of program")