import random
import sys
board = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}
available = [i for i in range(1, 10)]
print(available)
winners = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]
player = []
computer = []
list1 = []
list2 = []
win = False
checkp = []
checkc = []
firstmove = True
def display():
    for i in board:
        end = "|"
        if int(i)%3 == 0:
            end = "\n"
        print(board[i], end=end)

def computerchoice():

    for x in computer:
        for y in computer:
            for z in available:
                if x != y and y != z and x != z:
                    checkc.append((x, y, z))
                    checkc.append((x, z, y))
                    checkc.append((z, x, y))
                    checkc.append((z, y, x))
                    checkc.append((y, z, x))
                    checkc.append((y, x, z))
    for x in checkc:
        if x in winners:
            for y in x:
                if y in available:
                    return y
        else:
            for x in player:
                for y in player:
                    for z in available:
                        if x != y and y != z and x != z:
                            checkp.append((x, y, z))
                            checkp.append((x, z, y))
                            checkp.append((z, x, y))
                            checkp.append((z, y, x))
                            checkp.append((y, z, x))
                            checkp.append((y, x, z))
    for x in checkp:
        if x in winners:
            for y in x:
                if y in available:
                    return y
    else:
        return random.choice(available)



while len(available) > 0 and win == False:
    print("the available places are {}".format(available))
    place = input("choose where to put x")
    if int(place) not in available:
        print("the available places are {}".format(available))
        place = input("try again")
    y = int(place)
    board[int(place)] = "x"
    #print(board)
    display()
    player.append(y)
    available.remove(y)
    #print(available)
    for x in player:
        for y in player:
            for z in player:
                if x != y and y != z and x != z:
                    list1.append((x, y, z))
    #print(list1)
    for x in list1:
        if x in winners:
            print("you are a winner")
            win = True
            break
    list1.clear()
    if win == True:
        break
    if len(available) <= 0:
        print("its a tie")
        break
    print("computer's turn")
    place = computerchoice()
    print("computer has chosen {}".format(place))
    y = int(place)
    board[int(place)] = "o"
    #print(board)
    display()
    computer.append(y)
    #print(computer)
    #print(available)
    available.remove(y)
    for x in computer:
        for y in computer:
            for z in computer:
                if x != y and y != z and x != z:
                    list2.append((x, y, z))
    #print(list2)
    for x in list2:
        if x in winners:
            print("sorry computer wins you lost")
            win = True
            break
    list2.clear()
    if win == True:
        break
else:
    print("it is a tie")






