import random
'''
1 for snake
-1 for water
0 for gun
'''
computer=random.choice([-1,0,1])
youstr=input("enter your choice: ")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}

#by now we have two numbers(variables),you and computer

you=youdict[youstr]

print(f"You chose {reversedict[you]}\nComputer chose {reversedict[computer]}")

if(you==computer):
    print("tie")

else:
    if(you==1 and computer==-1):
        print("you win")

    elif(you==0 and computer==-1):
         print("you lose")

    elif(you==-1 and computer==1):
        print("you lose")

    elif(you==0 and computer==1):
        print("you win")

    elif(you==-1 and computer==0):
        print("you win")

    elif(you==1 and computer==0):
        print("you win")

    else:
        print("something is wrong")

    