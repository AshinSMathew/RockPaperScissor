import random

def rockpaper():
    print(' ')
    print('*********************************************************************************************************************************************************\n')
    p=input(" LET'S PLAY A GAME OF ROCK PAPER SCISSOR (PRESS ENTER TO START THE GAME)")
    y=int(input('HOW MANY ROUNDS '))
    if y<1:
        print('ENTER A VALID NUMBER')
    #k=input("YOUR TURN")
    s=['rock','paper','scissor']
    myscore=0
    uscore=0
    w=random.randint(0,2)
    o=0
   #print('MINE IS ',s[w],'\n')
    while y>=1:
        print(' ')
        print('''OPTIONS
\t1] ROCK
\t2] PAPER
\t3] SCISSOR''')
        k=int(input("YOUR TURN (type option number) "))
        if k>=4:
            print('ENTER A VALID INPUT')
            continue
        print('MINE IS ',s[w])
        print('YOURS IS ',s[k-1],'\n')
        if s[k-1]==s[w]:
            print("IT'S A 'TIE ROUND'")
            o+=1
            print('PLAYING THE ROUND ',o, 'AGAIN')
            y+=1
            o-=1
        if s[k-1]=='rock' and s[w]=='paper':
            myscore+=1
            print('"I WON" THE ROUND')
            o+=1
            print('ROUND ',o,'OVER\n')
        if s[k-1]=='rock' and s[w]=='scissor':
            uscore+=1
            print('"YOU WON" THE ROUND')
            o+=1
            print('ROUND ',o,'OVER\n')
        if s[k-1]=='paper' and s[w]=='rock':
            uscore+=1
            print('"YOU WON" THE ROUND')
            o+=1
            print('ROUND ',o,'OVER\n')
        if s[k-1]=='paper' and s[w]=='scissor':
            myscore+=1
            print('"I WON" THE ROUND')
            o+=1
            print('ROUND ',o,'OVER\n')
        if s[k-1]=='scissor' and s[w]=='paper':
            uscore+=1
            print('"YOU WON" THE ROUND')
            o+=1
            print('ROUND ',o,'OVER\n')
        if s[k-1]=='scissor' and s[w]=='rock':
            myscore+=1
            print('"I WON" THE ROUND')
            o+=1
            print('ROUND ',o,'OVER\n')
        #o+=1
        y-=1
        #print('ROUND ',o,'OVER\n')
        
    if myscore>uscore:
        print('SCOREBOARD IS ',myscore,'-',uscore)
        print('HAHAHA..... I WON THE MATCH\n')
    elif uscore>myscore:
        print('SCOREBOARD IS ',myscore,'-',uscore)
        print('CONGRATS YOU WON THE MATCH\n')
    else:
        print('SCOREBOARD IS ',myscore,'-',uscore)
        print("IT'S A TIE MATCH\n")
    w2=input('PRESS ENTER TO CONTINUE')
    print('_________________________________________________________________________________________________________________________________________________________\n')
rockpaper()
