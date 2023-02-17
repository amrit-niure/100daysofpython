#write a python program to translate a meaasge into sceret code language. use the rules below  to translate normal english into secret code language

#coding
# if the word contains atleast 3 characters, remove the first letter and append it at the end now append three random characters at the starting and the end 
# else sumply reverse the string 

# decoding
# if the word contains less than 3 characters, reverse it 
# else remove 3 random characters form start and end. Now remove the last letter form the end and append it to the start
# --------------------------coded by Amrit Niure--------------------------------
import random
import string
enc = input("Enter the message:")
# ---------------------------------------- ENCODING -------------------------------------
x= enc.split(" ")
message=''
for i in x:
    length=len(i)
    if length>=3:
        j=i[0:1]
        i=i[1:]
        rejoin=i+j
        S=3
        ran = ''.join(random.choices(string.ascii_lowercase, k = S))  
        halfletter=ran+rejoin
        ran = ''.join(random.choices(string.ascii_lowercase, k = S))  
        fullletter=halfletter + ran
        message = message+fullletter+" "
    elif(length<3):
        rev = i[::-1]
        message= message+rev+" "
print(f"This is encrypted message:\n{message}")
# -------------------------------------- DECODING ----------------------------------------
dec = message.split(" ")
decoded_msg=''
for k in dec:
    length2=len(k)
    if(length2<3):
        rev2 = k[::-1]
        decoded_msg= decoded_msg+rev2+" "
    else:
        l=k[3:]
        m=l[:-3]
        f_letter=m[-1]
        l_letter=m[:-1]
        final_letter=f_letter+l_letter
        decoded_msg= decoded_msg+final_letter+" "
print(f"This is decrypted message:\n{decoded_msg}")

