from functools import reduce
# MAP
# def cube(x):
#     return x*x*x
# print(cube(2))
# l = [1,3,4,6,7]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))
# # newl = list(map(cube,l))
# newl = list(map(lambda x: x*x*x ,l))
# print(newl)
# #
# # FILTER
# def fil_fun(a):
#     return a>4
# # newnewl = list(filter(fil_fun, l))
# newnewl = list(filter(lambda a: a>2, l))
# print(newnewl)


num = [1,2,4,6,7]

def mysum(x,y):
    return x+y
sum = reduce (mysum,num)

print(sum)
