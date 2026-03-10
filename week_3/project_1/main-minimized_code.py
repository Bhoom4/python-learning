'''snake,water,gun game!!!'''

import random  #module
computer=random.choice([-1,0,1])
istr=input("enter your choice: ")
idict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}

i=idict[istr]
print(f"you choose {reversedict[i]}\ncomputer choose {reversedict[computer]}")

if(computer==i):
    print("its a draw!!")

'''else:
    if(computer==-1 and i==0):      # [computer-i] =(-1-0==-1)
        print("you loose")
    elif(computer==1 and i==-1):     #        =(1-(-1)==2)
        print("you lost")
    elif(computer==0 and i==1):       #     =(0-1==-1)
        print("you lost")
    elif(computer==1 and i==0):       #     =(1-0==1)
        print("you win")
    elif(computer==0 and i==-1):      #     =(0-(-1)==1)
        print("you win")
    elif(computer==-1 and i==1):      #    =(-1-(1)==-2)
        print("you win")
    else:
        print("somthing went wrong")'''

if((computer-i)==-2 or (computer-i)==1):    # in the basis of above calculated sol
    print("you win!!")
else:
    print("you losse!!")

