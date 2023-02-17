# def double(x):
#     return x*2

# double = lambda x : x*2
cube = lambda y: y*y*y
# avg = lambda x,y,z: (x+y+z)/3
# print(double(5))
# print(cube(5))
# print(avg(5,3,2))

def appl(fx, value):
    return 6 + fx(value)

func_func = appl(cube,10)
print(func_func)

func_func = appl(lambda y: y*y*y,10)
print(func_func)