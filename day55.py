    #      S W G     COMPUTER
    #      0 1 2
    # S 0  D W L
    # W 1  W D W
    # G 2  W L D 
list = [[0,1,2],[0,1,2]]
for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j], end=' ')
    print()