from os import system as s
from random import randrange as rand
from time import sleep

selected = []


satr1 = ["-", "-", "-"]
satr2 = ["-", "-", "-"]
satr3 = ["-", "-", "-"]
dor = 0

def chap_bazi():
    s("cls")
    text_satr1 = ""
    text_satr2 = ""
    text_satr3 = ""
    for i in range(0, 3):
        text_satr1 = text_satr1 + " " + (satr1[i])
        text_satr2 = text_satr2 + " " + (satr2[i])
        text_satr3 = text_satr3 + " " + (satr3[i])
    print(text_satr1)
    print(text_satr2)
    print(text_satr3)

def man():
    if dor == 9:
        s("cls")
        print("bazi mosavi shod")
        exit() 
    else:   
        select_me = True
        while select_me:
            me_satr = rand(0, 3)
            me_soton = rand(0, 3)
            if (me_satr, me_soton) in selected:
                ""
            else:
                selected.append((me_satr, me_soton))
                select_me = False
                if me_satr == 0:
                    satr1[me_soton] = "O"
                elif me_satr == 1:
                    satr2[me_soton] = "O"
                elif me_satr == 2:
                    satr3[me_soton] = "O"

def user():
    if dor == 9:
        s("cls")
        print("bazi mosavi shod")
        exit()
    else:
        select_user = True
        while select_user:
            user_input = input("satr o soton entekhabi khod ra vared konid(satr  soton) ==>")
            user_satr = int(user_input[0]) - 1
            user_soton = int(user_input[-1]) - 1
            if (user_satr, user_soton) in selected:
                print("in satr va soton ghablan entekhab shode ast!...\ndobareh talash konid\n")
            else:
                selected.append((user_satr, user_soton))
                select_user = False
                if user_satr == 0:
                    satr1[user_soton] = "X"
                elif user_satr == 1:
                    satr2[user_soton] = "X"
                elif user_satr == 2:
                    satr3[user_soton] = "X"
      
def check(name):
    win = False
    if dor <= 9:  
        if satr1[0] == satr1[1] == satr1[2] == name or satr2[0] == satr2[1] == satr2[2] == name or satr3[0] == satr3[1] == satr3[2] == name:
            print(f"bazikon {name} barande shod...")
            exit()
        elif satr1[0] == satr2[0] == satr3[0] == name or satr1[1] == satr2[1] == satr3[1] == name or satr1[2] == satr2[2] == satr3[2] == name:
            print(f"bazikon {name} barande shod...")
            exit()
        elif satr1[0] == satr2[1] == satr3[2] == name or satr1[2] == satr2[1] == satr3[0] == name:
            print(f"bazikon {name} barande shod...")
            exit()
    if dor == 9:
        s("cls")
        print("bazi mosavi shod")
        exit()
        
    
chap_bazi()
sleep(1)
play = True
while play:
    if dor != 9:
        man()
        chap_bazi()
        check("O")
        dor += 1
        sleep(1)
        user()
        chap_bazi()
        check("X")
        dor += 1
        sleep(1)
