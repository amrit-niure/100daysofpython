# create a program capable of displaying questions to the user like KBC 
# use list data type to stor the questions and their correct answers
# display the final amount the person is taking home agter playing the game

print("\n---------------------------------- Welcome to KBC -----------------------------------")
qst=[
    "What is the Date of Birth of Amrit Niure?",
    "Where was the right hand incident happened in Amrits life?",
    "What is fastest programming language? ",
    "In which language this program is coded?"
]
ans=[
    "6 april",
    "uncles house",
    "c",
    "python"
]
prize_won=0
j=0
def options(){
    
}
for i in qst:
 
    print(i)
    options()
    gans=input("Answer:")
    if(gans==ans[j]):
        prize_won=1000+prize_won*j
        j+=1
    else:
        break
    print("You won",prize_won)