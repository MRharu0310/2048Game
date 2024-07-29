import random
import math
import os

def clear_terminal():
    # Windowsの場合
    if os.name == 'nt':
        os.system('cls')
    # Unix系OS（Linux、Macなど）の場合
    else:
        os.system('clear')

BG_WHITE = '\033[47m'#白背景の定義
BLACK = '\033[30m'#黒文字の定義
RESET = '\033[0m'

#それぞれのマスの指数を格納
L = []
for i in range(16):
    L.append(0)

Save = [] #Lの保存用

#空きマスの情報を格納
E = []

score = 0
score_plus = 0
Input = "None"
Count_Move = 0
turn = 0
check = 0
Massage = "None"

#1つの空きマスを2か4にする
def check_space():
    global turn
    E = []
    for i in range(16):
        if L[i] == 0:
            E.append(i)
    if len(E) != 0:
        turn = E[random.randint(0,len(E)-1)]
        L[turn] = random.randint(1,2)

def Move(a,b,c,d):
    global Count_Move, score, score_plus
    if L[b] != 0 and L[a] == 0:
        Count_Move += 1
        L[a] = L[b]
        L[b] = 0
    if L[c] != 0 and L[b] == 0:
        Count_Move += 1
        L[b] = L[c]
        L[c] = 0
        if L[b] != 0 and L[a] == 0:
            L[a] = L[b]
            L[b] = 0
    if L[d] != 0 and L[c] == 0:
        Count_Move += 1
        L[c] = L[d]
        L[d] = 0
        if L[c] != 0 and L[b] == 0:
            L[b] = L[c]
            L[c] = 0
            if L[b] != 0 and L[a] == 0:
                L[a] = L[b]
                L[b] = 0
    #合体させて指数の処理
    if L[a] == L[b] != 0:
        L[a] += 1
        L[b] = 0
        Count_Move += 1
        score += 2**L[a]
        score_plus += 2**L[a]
    if L[b] == L[c] != 0:
        L[b] += 1
        L[c] = 0
        Count_Move += 1
        score += 2**L[b]
        score_plus += 2**L[b]
    if L[c] == L[d] != 0:
        L[c] += 1
        L[d] = 0
        Count_Move += 1
        score += 2**L[c]
        score_plus += 2**L[c]
    #隙間の処理
    if L[b] != 0 and L[a] == 0:
        Count_Move += 1
        L[a] = L[b]
        L[b] = 0
    if L[c] != 0 and L[b] == 0:
        Count_Move += 1
        L[b] = L[c]
        L[c] = 0
        if L[b] != 0 and L[a] == 0:
            L[a] = L[b]
            L[b] = 0
    if L[d] != 0 and L[c] == 0:
        Count_Move += 1
        L[c] = L[d]
        L[d] = 0
        if L[c] != 0 and L[b] == 0:
            L[b] = L[c]
            L[c] = 0
            if L[b] != 0 and L[a] == 0:
                L[a] = L[b]
                L[b] = 0

def count():
    global check , Save, L, score_plus, score, Count_Move
    Save = L.copy()
    check = 0
    Count_Move = 0
    for i in range(4):
        Move(4*i, 4*i+1, 4*i+2, 4*i+3)
    if Count_Move != 0:
        check += 1
    L = Save.copy()
    Count_Move = 0
    for i in range(4):
        Move(4*i+3, 4*i+2, 4*i+1, 4*i)
    if Count_Move != 0:
        check += 1
    L = Save.copy()
    Count_Move = 0
    for i in range(4):
        Move(i, 4+i, 8+i, 12+i)
    if Count_Move != 0:
        check += 1
    L = Save.copy()
    Count_Move = 0
    for i in range(4):
        Move(12+i, 8+i, 4+i, i)
    if Count_Move != 0:
        check += 1
    L = Save.copy()
    Count_Move = 0
    
    if check == 0:
        score -= score_plus
        score_plus = 0
        return 0
    else:
        score -= score_plus
        score_plus = 0
        return 1


def draw():
    global turn
    clear_terminal()
    print("---------------------------------")
    for i in range(4):
        for j in range(4):
            if L[4*i+j] == 0:
                print("|",end="\t")
            elif 4*i+j == turn:
                if math.log(2**L[4*i+j], 10)<= 2:
                    print("|  ", f"{BG_WHITE}{BLACK}{2**L[4*i+j]}{RESET}",end="\t")
                elif math.log(2**L[4*i+j], 10) > 2:
                    print("| ",f"{BG_WHITE}{BLACK}{2**L[4*i+j]}{RESET}",end="\t")
            else:
                if math.log(2**L[4*i+j], 10)<= 2:
                    print("|  ",2**L[4*i+j],end="\t")
                elif 5 > math.log(2**L[4*i+j], 10) > 2:
                    print("| ",2**L[4*i+j],end="\t")
                else:
                    print("|",2**L[4*i+j],end="\t")
        print("|",end="\n")
        print("---------------------------------")
    print("Score: ",score," ( +",score_plus,")")

check_space()
check_space()
draw()
while Massage == "None":
    while 0 in L:
        Input = input()
        if Input == "A" or Input == "a":
            for i in range(4):
                Move(4*i, 4*i+1, 4*i+2, 4*i+3)
        elif Input == "D" or Input == "d":
            for i in range(4):
                Move(4*i+3, 4*i+2, 4*i+1, 4*i)
        elif Input == "W" or Input == "w":
            for i in range(4):
                Move(i, 4+i, 8+i, 12+i)
        elif Input == "S" or Input == "s":
            for i in range(4):
                Move(12+i, 8+i, 4+i, i)
        else:
            print("invalid input")
        
        if Count_Move == 0:
            print("invalid input")
        else:
            check_space()
            draw()
            Count_Move = 0
            score_plus = 0
    if count() == 0:
        print("GAME OVER!")
        break
    while Massage != "Moved":
        Input = input()
        if Input == "A" or Input == "a":
            for i in range(4):
                Move(4*i, 4*i+1, 4*i+2, 4*i+3)
        elif Input == "D" or Input == "d":
            for i in range(4):
                Move(4*i+3, 4*i+2, 4*i+1, 4*i)
        elif Input == "W" or Input == "w":
            for i in range(4):
                Move(i, 4+i, 8+i, 12+i)
        elif Input == "S" or Input == "s":
            for i in range(4):
                Move(12+i, 8+i, 4+i, i)
        else:
            print("invalid input")
        
        if Count_Move== 0:
            print("invalid input")
        else:
            check_space()
            draw()
            Count_Move = 0
            score_plus = 0
            Massage = "Moved"
    Massage = "None"