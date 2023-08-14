#creating a box with hashtag as their default values....
values=["#","#","#","#","#","#","#","#","#"]
userx_turn=1
usery_turn=1


#Error check code...
Error_Check=[] #creating an empty list to store all the entered values

def printbox():
    print(" {} | {} | {} ".format(values[0], values[1], values[2]))
    print("---|---|---")
    print(" {} | {} | {} ".format(values[3], values[4], values[5]))
    print("---|---|---")
    print(" {} | {} | {} ".format(values[6], values[7], values[8]))

printbox()

userx=["O","O","O","O","O","O","O","O","O"]
usery=["X","X","X","X","X","X","X","X","X"]
for game in range(4):
    userx_turn=1
    usery_turn=1
    while(userx_turn!=0):
        userx_in=int(input("user 1 input: "))
        if (userx_in>=0 and userx_in<=8):
            if userx_in not in Error_Check:
                userx_turn=0
                match(userx_in):
                    case 0:
                        values[0]=userx[0]
                    case 1:
                        values[1]=userx[1]
                    case 2:
                        values[2]=userx[2]
                    case 3:
                        values[3]=userx[3]
                    case 4:
                        values[4]=userx[4]
                    case 5:
                        values[5]=userx[5]
                    case 6:
                        values[6]=userx[6]
                    case 7:
                        values[7]=userx[7]
                    case 8:
                        values[8]=userx[8]
        elif(userx_in in Error_Check or userx_in>8):
            print("out of range")
            userx_turn=1
        Error_Check.append(userx_in)
    printbox()
    while(usery_turn!=0):
        usery_in=int(input("user 2 input: "))
        if (usery_in>=0 and usery_in<=8):
            if usery_in not in Error_Check:
                usery_turn=0
                match(usery_in):
                    case 0:
                        values[0]=usery[0]
                    case 1:
                        values[1]=usery[1]
                    case 2:
                        values[2]=usery[2]
                    case 3:
                        values[3]=usery[3]
                    case 4:
                        values[4]=usery[4]
                    case 5:
                        values[5]=usery[5]
                    case 6:
                        values[6]=usery[6]
                    case 7:
                        values[7]=usery[7]
                    case 8:
                        values[8]=usery[8]
        elif(usery_in in Error_Check or usery_in>8):
            print("out of range")
            usery_turn=1
        #if out of range do the same thing again
        Error_Check.append(usery_in)
    printbox()
#last condition
index_check=0
for values_check in values:
    if(values_check=="X" or values_check=="O"):
        index_check+=1
    else:
        break

values[index_check]=userx[index_check]
print("____________________Final____________________")
printbox()

wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
for win in wins:

    if(userx[win[0]]==userx[win[1]]==userx[win[2]]=="X"):
        print("UserX win the Game")
        break
    elif(usery[win[0]]==usery[win[1]]==usery[win[2]]=="O"):
        print("UserY win the Game")
        break
    else:
        print("Nobody won the game")