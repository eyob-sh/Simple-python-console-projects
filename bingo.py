import random


class bingo:

    def __init__(self):
        list = [i for i in range(1, 26)]
        self.board = {}
        for x in range(1, 26):
            y = random.choice(list)
            list.remove(y)
            self.board[x] = y


computer = bingo()
board2 = computer.board
print(computer.board)
player = bingo()
board1 = player.board
print(player.board)
leftnum = [i for i in range(1, 26)]
win = False
winner = [(1, 2, 3, 4, 5), (6, 7, 8, 9, 10), (11, 12, 13, 14, 15), (16, 17, 18, 19, 20), (21, 22, 23, 24, 25)]
countcomp = [0 for i in range(1, 13)]
countplayer = [0 for i in range(1, 13)]


def display(board):
    for x in board:
        end = '|'
        if x % 5 == 0:
            end = '\n'
        print(board[x], end=end)


def change_to_zero(num):
    for x in board1:
        if board1[x] == num:
            board1[x] = 0
            break
    for x in board2:
        if board2[x] == num:
            board2[x] = 0
            break


def counter(board, count):
    for x in range(1, 6):
        if board[x] == 0:
            board[x] = 'o'
            count[0] += 1
            count[x + 4] += 1
            if x == 1:
                count[10] += 1
            if x == 5:
                count[11] += 1
    for x in range(6, 11):
        if board[x] == 0:
            board[x] = 'o'
            count[1] += 1
            count[x - 1] += 1
            if x == 7:
                count[10] += 1
            if x == 9:
                count[11] += 1
    for x in range(11, 16):
        if board[x] == 0:
            board[x] = 'o'
            count[2] += 1
            count[x - 6] += 1
            if x == 13:
                count[10] += 1
                count[11] += 1
    for x in range(16, 21):
        if board[x] == 0:
            board[x] = 'o'
            count[3] += 1
            count[x - 11] += 1
            if x == 19:
                count[10] += 1
            if x == 17:
                count[11] += 1
    for x in range(21, 26):
        if board[x] == 0:
            board[x] = 'o'
            count[4] += 1
            count[x - 16] += 1
            if x == 25:
                count[10] += 1
            if x == 21:
                count[11] += 1


def computer_choice():
    biggest = countcomp[0]
    level = 0
    for x in countcomp:
        if countcomp[x] < 5:
            biggest = countcomp[x]
            level = x
            break
    for x in countcomp:
        if biggest < countcomp[x] < 5:
            biggest = countcomp[x]
            level = x
    if level == 0:
        for x in range(1, 6):
            if board2[x] != 0 and board2[x] != 'o':
                return board2[x]
    if level == 1:
        for x in range(6, 11):
            if board2[x] != 0 and board2[x] != 'o':
                return board2[x]

    if level == 2:
        for x in range(11, 16):
            if board2[x] != 0 and board2[x] != 'o':
                return board2[x]

    if level == 3:
        for x in range(16, 21):
            if board2[x] != 0 and board2[x] != 'o':
                return board2[x]

    if level == 4:
        for x in range(21, 26):
            if board2[x] != 0 and board2[x] != 'o':
                return board2[x]

    if level == 5:
        for x in range(1, 22, 5):
            if board2[x] != 0 and board2[x] != 'o':
                return board2[x]

    if level == 6:
        for x in range(2, 23, 5):
            if board2[x] != 0 and board2[x] != 'o':
                return board2[x]
    if level == 7:
        for x in range(3, 24, 5):
            if board2[x] != 0 and board2[x] != 'o':
                return board2[x]
    if level == 8:
        for x in range(4, 25, 5):
            if board2[x] != 0 and board2[x] != 'o':
                return board2[x]
    if level == 9:
        for x in range(5, 26, 5):
            if board2[x] != 0 and board2[x] != 'o':
                return board2[x]
    if level == 10:
        for x in range(1, 26, 6):
            if board2[x] != 0 and board2[x] != 'o':
                return board2[x]
    if level == 11:
        for x in range(5, 22, 6):
            if board2[x] != 0 and board2[x] != 'o':
                return board2[x]


def check_win(list):
    if list.count(5) >= 5:
        return True


while not win:
    display(board1)
    print()
    display(board2)
    print(leftnum)
    num1 = int(input("enter the number you want to remove"))  # another function to check
    if num1 < 0 or num1 > 25 or num1 not in leftnum:
        num1 = input("try again the numbers you can enter are {}".format(leftnum))
    leftnum.remove(num1)
    change_to_zero(num1)
    counter(board1, countplayer)
    counter(board2, countcomp)
    if check_win(countplayer):
        print("you win")
        break
    if check_win(countcomp):
        print("sorry computer wins")
        break
    num2 = int(computer_choice())
    leftnum.remove(num2)
    change_to_zero(num2)
    counter(board2, countcomp)
    counter(board1, countplayer)
    if check_win(countcomp):
        print("you win")
        break
    if check_win(countplayer):
        print("you win")
        break
