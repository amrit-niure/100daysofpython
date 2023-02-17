import time
questions = [
    ["what color is banana?",'white','orange','yellow','red',3],
    ["what color is orange?",'white','orange','yellow','red',2],
    ["what color is apple?",'white','orange','yellow','red',4],
    ["what color is mirror?",'no color','orange','yellow','red',1],
    ["what color is garden?",'white','green','yellow','red',2],
    ["what color is banana?",'white','orange','yellow','red',3],
    ["what color is orange?",'white','orange','yellow','red',2],
    ["what color is apple?",'white','orange','yellow','red',4],
    ["what color is mirror?",'no color','orange','yellow','red',1],
    ["what color is garden?",'white','green','yellow','red',2],
]

levels = [1000,2000,3000,5000, 10000,20000,40000,80000,160000,320000,640000,1250000,2500000,500000,10000000]
money=0 
for i in range(0,len(questions)):
    
    print(f'\nQuestion for Rs. {levels[i]} ')
    # time.sleep(1)
    print(f'\n{questions[i][0]}')
    print(f'a. {questions[i][1]}\t\tb. {questions[i][2]} ')
    print(f'c. {questions[i][3]}\t\td. {questions[i][4]} ')
    reply = input("Enter you option: ")
    if (reply=="a"):
        reply=1
    elif (reply=="b"):
        reply=2
    elif (reply=="c"):
        reply=3
    elif (reply=="d"):
        reply=4

    if(reply==questions[i][-1]):
        print(f'\nCorrect answer, you have won Rs. {levels[i]}')
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==4):
            money=10000000

    else:
        print("\nWrong Answer.")
        break

print(f'\nYour take away money is : {money}')

