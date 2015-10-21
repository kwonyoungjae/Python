import random
def intro():
    print('#############################')
    print(' 야구 게임 설명')
    print("""1. 야구게임은 플레이어와 컴퓨터와 대결하여 점수가 큰쪽이 이기는 게임입니다.
(단, 점수가 같으면 비깁니다.) 야구와 룰이 비슷하니 야구룰을 참고하면 좋습니다.

2. 플레이어가 먼저 공격을 하게 됩니다. 이때 플레이어는 타자가 되어 플레이합니다.

3. 타자일때 게임존 밑에있는 1~25 사이의 숫자중 하나를 입력하세요. 만약 올바르게 입력
하셨다면 그 숫자가 있는 줄은 다 치게 됩니다. 예를 들면 13을 입력하셨다면
11,12,13,14,15 의 숫자를 다 치신겁니다. 이때 컴퓨터가 투수를 맡게 되는데요. 컴퓨터는
직구, 커브 ,포크볼을 던집니다. 확률은 비밀~,게임하면서 알아맞혀보세요.

4. 투수일때는 게임존 밑에있는 1~25 사이의 숫자중 하나를 입력하세요. 그후 직구,커브,포크볼
세 구질중에 하나를 골라 던지면 됩니다. 이때 컴퓨터는 타자를 맡게됩니다. 컴퓨터(타자)는
1~25 중의 하나의 숫자를 선택합니다.

5.점수는 주자가 홈에서 1~3루를 돌아 다시 홈으로 들어오면 점수를 1점 획득하게됩니다.

6. 3out이 되면 공격과  수비를 바꾸게됩니다.

7. 스트라이크는 7,8,9,12,13,14,17,18,19 이고 나머지는 볼입니다.

8. 타자일때 스트라이크 구역으로 날아오는 공을 맞추면 볼인 구역으로 날아오는 공보다 안타나
홈런을 맞출 확률이 높습니다. 또한 공을 정확히 맞추시면 안타나 홈런이 나올 확률이 더 높습니다. 정확히 맞춰보세요.

9.투수일때 직구는 그대로 공이  들어가고, 커브는 던진공이 1,6,11,16 일때는 숫자를 9 더해서 5,10,15,20 일때는 숫자를
1 더해서 , 2,3,4, 일때는 6을 더하거나 4를 더해서, 21,22,23,24,25일때는 숫자를 5빼서 공이 들어옵니다. 포크볼일때는
던진공이 21부터 25까지의 숫자면 공이 그대로 들어가고 16부터 20까지의 숫자면 5 더해서
나머지 숫자는 10 더해서 들어갑니다.

10. 난이도는 (상 중 하) 가 있습니다.

11. 타자가 공을 쳤을때 나오는 텍스트가 중복됩니다. 여러개 나와도 하나만 나온것과 의미가 같습니다.
############게임 설명을 읽어 주셔서 감사합니다.############# """)
def hnh():
    a = input("치시겠습니까?(y or n):")
    while True:
        if a == 'y' or a == 'n':
            break
        else:
            a = input("치시겠습니까?(y or n):")
    return a
def pform():
    form = input("1.직구,2.커브,3.포크볼 :")
    if form == '1' or form == '2' or form == '3':
        return form
    else :
        return pform()
def pitcher_(a,b):
    """a는 던진곳, b는 구질"""
    gzone =[  ['0','0','0','0','0'],
                    ["1" ,"2","3","4",'5'],
                    ["6","7","8","9","10"],
                    ["11","12","13","14","15"],
                    ["16","17","18","19","20"],
                    ["21","22","23","24","25"],
                      ['0','0','0','0','0']]
    thu = (7,8,9,12,13,14,17,18,19)
    thu1 = (1,6,11,16)
    thu2 = (5,10,15,20)
    thu3 = (2,3,4)
    
    pit = random.randint(1,100)
    throw = str(a)
    form = b
    if form == '1' :
        return int(throw)
    elif form == '2':
        if int(throw) in thu:
            if 1<=pit<=50:
                return int(throw) +6
            else:
                return int(throw) -6
        elif int(throw) in thu1:
            return int(throw) + 9
        elif int(throw) in thu2:
            return int(throw) + 1
        elif int(throw) in thu3:
            if 1<=pit<=50:
                return int(throw) +6
            else:
                return int(throw) +4
        else:
            return int(throw) - 5
      
    else:
        if throw in gzone[1] or throw in gzone[2] or throw in gzone[3]:
            return int(throw) + 10
        elif throw in gzone[4]:
            return int(throw) + 5
        else:
            return int(throw)
def cform():
    pit = random.randint(1,100)
    if 1<=pit<=20:
        return '1'
    elif 21<=pit<=60:
        return '2'
    else:
        return '3'
def pitcher() :
    """투수 어디 던질지"""
    throw = input("어느곳으로 공을 던지시겠습니까?:")
    while True :
        if throw.isdigit() :
            if 1<=int(throw) <=25 :
                return throw
            else :
                throw = input("어느곳으로 공을 던지시겠습니까?:")
        else :
            throw = input("어느곳으로 공을 던지시겠습니까?:")
def gohome():
    runner = input('타자를 내보내세요 a:')
    while not runner == 'a':
        runner = input('타자를 내보내세요 a:')
    return runner

    
def pitcherC(a) :
    strik = (7,8,9,12,13,14,17,18,19)
    ball = (1,2,3,4,5,6,10,11,15,16,20,21,22,23,24,25)
    perpit = random.randint(1,100)
    throw = random.randint(1,25)
    if 1<=perpit<= 60 :
        while not throw in strik:
            throw = random.randint(1,25)
        return pitcher_(throw,a),throw
    else:
        while not throw in ball:
            throw = random.randint(1,25)
        return pitcher_(throw,a),throw
        
    return random.randint(1,25)
def hitterC(thr,th,a,b):
    strik = (7,8,9,12,13,14,17,18,19)
    ball = (1,2,3,4,5,6,10,11,15,16,20,21,22,23,24,25)
    hi = random.randint(1,25)
    pit = random.randint(1,100)
    pit1 = random.randint(1,100)
    if 1<=pit1<=a:
        return int(thr)
    elif a+1<=pit1<=b:
        return int(th)
    else:
        if 1<=pit<=70:
            while not hi in strik:
                hi = random.randint(1,25)
            return hi
        else:
            while not hi in ball:
                hi = random.randint(1,25)
            return hi
def hitter() :
    """타자 어디 칠지"""
    hit = input("어느곳을 치시겠습니까:")
    while True :
        if hit.isdigit() :
            if 1<=int(hit)<=25 :
                return hit
            else :
                hit = input("어느곳을 치시겠습니까")
        else :
            hit = input("어느곳을 치시겠습니까")
    #if hit in gameBoard1().strikeZone[pitcher().throw] :
      #  print("공을 맞추셨습니다.")
        #a = 1
    #else :
      #  print("헛 스윙을 하셨습니다.")
        
def gameBoard1():
    """게임존 보드 """
    print()
    print (" game Zone")
    print()
    strikeZone = [["┌──────────────┐"],
                 ["│01 02 03 04 05│"],
                 ["│06 07 08 09 10│"],
                 ["│11 12 13 14 15│"],
                 ["│16 17 18 19 20│"],
                 ["│21 22 23 24 25│"],
                 ["└──────────────┘"]]
    
    for i in strikeZone :
        print(i)
    print()

    
def gameBoard2(a,b,c,d,e,f,g,h,i,j) :
    """r은 플레이할 횟수"""
    print('score')
    print()
    print('   ',end ='')
    for term in range(1,6) :
        print('│',term,end =' ')
    print()
    print('─────'*len(range(1,6)))
    print('p1','│',a,' ',b,' ',c,' ',d,' ',e)
    print('p2','│',f,' ',g,' ',h,' ',i,' ',j)
    print()
def gameBoard3(ball,strike,out) :
    ballCount = {'B' : ball, 'S' : strike, 'O' : out}
    print('Ball Count')
    print()
    print('S','│','B','│','O')
    print('─────────')
    print(ballCount['S'], '│',ballCount['B'], '│',ballCount['O'])
    print()
def gameBoard4(a,b,c,d):
    """a는 홈,b는 1루,c 는 2루,d는 4루"""
    base = [a,b,c,d]
    print('base')
    print()
    print('            ',[base[2]],'(2루)','      ')
    print('          ↙       ↖                   ')
    print('(3루)',[base[3]],'       ',[base[1]],'(1루)')
    print('          ↘       ↗                      ')
    print('       ','(홈)',[base[0]],'              ')
    print()
#스트라이크 쳤을때
def homerun(v_aver,bas1,bas2,bas3,bas4):
    if 1<=v_aver<=5:
        print("Home run~~") #그중 10%가 홈런
        if bas1 == 'o' and bas2 == 'o' and bas3 == 'o' and bas4 == 'o':
            print('4점 획득')
            return 'x','x','x','x',4
        elif bas1 == 'o' and bas2 == 'o' and bas3 == 'o' and bas4 == 'x':
            print('3점 획득')
            return 'x','x','x','x',3
        elif bas1 == 'o' and bas2 == 'o' and bas3 == 'x' and bas4 == 'o':
            print('3점 획득')
            return 'x','x','x','x',3
        elif bas1 == 'o' and bas2 == 'x' and bas3 == 'o' and bas4 == 'o':
            print('3점 획득')
            return 'x','x','x','x',3
        elif bas1 == 'o' and bas2 == 'o' and bas3 == 'x' and bas4 == 'x':
            print('2점 획득')
            return 'x','x','x','x',2
        elif bas1 == 'o' and bas2 == 'x' and bas3 == 'x' and bas4 == 'o':
            print('2점 획득')
            return 'x','x','x','x',2
        elif bas1 == 'o' and bas2 == 'x' and bas3 == 'o' and bas4 == 'x':
            print('2점 획득')
            return 'x','x','x','x',2
        else:
            print('1점 획득')
            return 'x','x','x','x',1
    else:
        return bas1,bas2,bas3,bas4,0
            
def ao(v_aver):
    if 6<=v_aver<=15:
        print("넘어갑니다")
        print("아 잡혔습니다.")
        print("뜬공 이였습니다.")
        return 1,'x'
    else:
        return 0,'o'
def go(v_aver):
    if 16<=v_aver<=25:
        print("땅으로 튀었습니다.")#그중 10%가 땅볼
        print("잡혔습니다.")
        return 1,'x'
    else :
        return 0,'o'
def base1(v_aver,bas1,bas2,bas3,bas4):
    if 26<=v_aver<=70:
        print("1루타")
        if bas1 == 'o' and bas2 == 'o' and bas3 == 'o' and bas4 == 'o':
            print('1점 획득')# 1,2,3
            return 'x','o','o','o',1
        elif bas1 == 'o' and bas2 == 'o' and bas3 == 'o' and bas4 == 'x':
            return 'x','o','o','o',0#1,2,
        elif bas1 == 'o' and bas2 == 'o' and bas3 == 'x' and bas4 == 'o':
            print('1점 획득')#1,3
            return 'x','o','o','x',1
        elif bas1 == 'o' and bas2 == 'x' and bas3 == 'o' and bas4 == 'o':
            print('1점 획득')#2,3,
            return 'x','o','x','o',1
        elif bas1 == 'o' and bas2 == 'o' and bas3 == 'x' and bas4 == 'x':
            return 'x','o','o','x',0#1
        elif bas1 == 'o' and bas2 == 'x' and bas3 == 'x' and bas4 == 'o':
            print('1점 획득')#3
            return 'x','o','x','x',1
        elif bas1 == 'o' and bas2 == 'x' and bas3 == 'o' and bas4 == 'x':
            return 'x','o','x','o',0#2
        else:
            return 'x','o','x','x',0
    else:
        return bas1,bas2,bas3,bas4,0
def base2(v_aver,bas1,bas2,bas3,bas4):
    if 71<=v_aver<=100:
        print("2루타")
        if bas1 == 'o' and bas2 == 'o' and bas3 == 'o' and bas4 == 'o':
            print('2점 획득')
            return 'x','x','o','o',2
        elif bas1 == 'o' and bas2 == 'o' and bas3 == 'o' and bas4 == 'x':
            print('1점 획득')
            return 'x','x','o','o',1
        elif bas1 == 'o' and bas2 == 'o' and bas3 == 'x' and bas4 == 'o':
            print('1점 획득')
            return 'x','x','o','o',1
        elif bas1 == 'o' and bas2 == 'x' and bas3 == 'o' and bas4 == 'o':
            print('2점 획득')
            return 'x','x','o','x',2
        elif bas1 == 'o' and bas2 == 'o' and bas3 == 'x' and bas4 == 'x':
            return 'x','x','o','o',0
        elif bas1 == 'o' and bas2 == 'x' and bas3 == 'x' and bas4 == 'o':
            print('1점 획득')
            return 'x','x','o','x',1
        elif bas1 == 'o' and bas2 == 'x' and bas3 == 'o' and bas4 == 'x':
            print('1점 획득')
            return 'x','x','o','x',1
        else:
            return 'x','x','o','x',0
    else:
        return bas1,bas2,bas3,bas4,0
def lev():
    x = input('난이도를 골라주세요. 1.하, 2. 중,3. 상 :')
    leve = [[30,40],[40,60],[30,70]]
    if x == '1':
        return leve[0]
    elif x == '2':
        return leve[1]
    elif x == '3':
        return leve[2]
    else:
        return lev()
def hita(v_aver,bas1,bas2,bas3,bas4,count,n,out):
    bas1,bas2,bas3,bas4,score[n][count] = homerun(v_aver,bas1,bas2,bas3,bas4)[0]\
                                             ,homerun(v_aver,bas1,bas2,bas3,bas4)[1],\
                                             homerun(v_aver,bas1,bas2,bas3,bas4)[2],\
                                             homerun(v_aver,bas1,bas2,bas3,bas4)[3],\
                                             score[n][count] + homerun(v_aver,bas1,bas2,bas3,bas4)[4]
    out,bas1 = out  + ao(v_aver)[0],ao(v_aver)[1]
    out,bas1 = out + go(v_aver)[0],go(v_aver)[1]
    bas1,bas2,bas3,bas4,score[n][count] = base1(v_aver,bas1,bas2,bas3,bas4)[0],\
                                             base1(v_aver,bas1,bas2,bas3,bas4)[1],\
                                             base1(v_aver,bas1,bas2,bas3,bas4)[2],\
                                             base1(v_aver,bas1,bas2,bas3,bas4)[3],\
                                             score[n][count] + base1(v_aver,bas1,bas2,bas3,bas4)[4]
                                             
    bas1,bas2,bas3,bas4,score[n][count] = base2(v_aver,bas1,bas2,bas3,bas4)[0],\
                                             base2(v_aver,bas1,bas2,bas3,bas4)[1],\
                                             base2(v_aver,bas1,bas2,bas3,bas4)[2],\
                                             base2(v_aver,bas1,bas2,bas3,bas4)[3],\
                                             score[n][count] + base2(v_aver,bas1,bas2,bas3,bas4)[4]
    return bas1,bas2,bas3,bas4,score[n][count],out
def ifball(bas1,bas2,bas3,bas4,n,count,ball):
    if ball == 4 :
        if bas2 == 'o' and bas3 == 'o'and bas4 == 'o':
            print('1점획득')
            bas1 = 'x'
            score[n][count] = score[n][count] +1
        elif bas2 == 'o' and bas3 == 'x'and bas4 == 'o':
            bas1,bas2 ,bas3,bas4 = 'x','o','o','o'
        elif bas2 == 'o' and bas3 == 'o'\
                and bas4 == 'x':
            bas1,bas2 ,bas3,bas4 = 'x','o','o','o'
        elif bas2 == 'x' and bas3 == 'o'\
                and bas4 == 'o':
            bas1,bas2,bas3,bas4 = 'x','o','o','o'
        elif bas2 == 'o' and bas3 == 'x'\
                 and bas4 == 'x':
            bas1,bas2,bas3,bas4 = 'x','o','o','x'
        elif bas2 == 'x' and bas3 == 'o'\
                and bas4 == 'x':
            bas1,bas2,bas3,bas4 = 'x','o','o','x'
        elif bas2 == 'x' and bas3 == 'x'\
                and bas4 == 'o':
            bas1,bas2,bas3,bas4 = 'x','o','x','o'
        else:
            bas1,bas2,bas3,bas4 = 'x','o','x','x'
        return bas1,bas2,bas3,bas4,score[n][count]
    else:
        return bas1,bas2,bas3,bas4,score[n][count]
while True :
    gzone =[  ["1" ,"2","3","4",'5'],
                    ["6","7","8","9","10"],
                    ["11","12","13","14","15"],
                    ["16","17","18","19","20"],
                    ["21","22","23","24","25"]]
    ex = input("설명을 보시겠습니까?y/n:")
    
    while True:
        if ex == 'y' or ex =='n':
            break
        else:
            ex = input("설명을 보시겠습니까?y/n:")
    if ex == "y" :
        intro()
    elif ex == 'n':
        print('게임을 시작하겠습니다.')
    print()
    le = lev()
    sx1,sx2 = le[0],le[1] 
    score = [ [0,0,0,0,0],[0,0,0,0,0]]
    count = 0
    while True :
        out = 0
        bas1,bas2,bas3,bas4 = 'x','x','x','x'
        print(count +1 ,'회초 입니다.')
        while True:
            n = 0
            h_aver = random.randint(1,100)
            v_aver = random.randint(1,100)
            if bas1 == 'x':
                strike,ball = 0,0
                runner = gohome()
            if  runner == 'a':
                bas1 = 'o'
            gameBoard1()
            gameBoard2(score[0][0],score[0][1],score[0][2],score[0][3],score[0][4],\
                       score[1][0],score[1][1],score[1][2],score[1][3],score[1][4])
            gameBoard3(ball,strike,out)
            gameBoard4(bas1,bas2,bas3,bas4)
            nhn = hnh()
            thrn = pitcherC(cform())
            thr,thr1 = thrn[0],thrn[1]
            print('투수가',thr1,'를 던졌습니다.')
            if nhn == 'y':
                hit = hitter()
                if hit in gzone[(int(thr)-1)//5 ]:
                    if str(thr) == '7' or str(thr) == '8' or str(thr) == '9' or \
                    str(thr) == '12' or str(thr) == '13' or str(thr) == '14' or\
                    str(thr) == '17' or str(thr) == '18' or str(thr) == '19' :
                        if str(thr) == hit :
                            print("쳤습니다.")
                            hitted = hita(v_aver,bas1,bas2,bas3,bas4,count,n,out)
                            bas1,bas2,bas3,bas4,score[n][count],out  = hitted[0],hitted[1],hitted[2],hitted[3],hitted[4],hitted[5]
                        else :
                            if 1<=h_aver<=80:
                                print("쳤습니다.")
                            
                                hitted = hita(v_aver,bas1,bas2,bas3,bas4,count,n,out)
                                bas1,bas2,bas3,bas4,score[n][count],out  = hitted[0],hitted[1],hitted[2],hitted[3],hitted[4],hitted[5]
                            else :
                                print("파울")
                                if strike < 2:
                                    strike = strike + 1
                    else:
                        if str(thr) == hit :
                            print("쳤습니다.")
                            if 1<=v_aver<=70:
                                hitted = hita(v_aver,bas1,bas2,bas3,bas4,count,n,out)
                                bas1,bas2,bas3,bas4,score[n][count],out  = hitted[0],hitted[1],hitted[2],hitted[3],hitted[4],hitted[5]
                            else:
                                print("파울")
                                if strike < 2:
                                    strike = strike + 1
                        else:
                            if 1<=h_aver<=50:
                                print("쳤습니다.")
                                hitted = hita(v_aver,bas1,bas2,bas3,bas4,count,n,out)
                                bas1,bas2,bas3,bas4,score[n][count],out  = hitted[0],hitted[1],hitted[2],hitted[3],hitted[4],hitted[5]
                            else :
                                print("파울")
                                if strike < 2:
                                    strike = strike + 1
                                    
                else:
                    print("스윙")
                    strike = strike + 1
            else:
                if str(thr) == '7' or  str(thr) == '8' or str(thr) == '9' or \
                str(thr) == '12' or str(thr) == '13' or str(thr) == '14' or\
                str(thr) == '17' or str(thr) == '18' or str(thr) == '19' :
                    print("스트라이크")
                    strike = strike + 1
                else :
                    print('볼')
                    ball = ball + 1
            if strike == 3:
                print('삼진 아웃')
                out = out + 1
                bas1 = 'x'
            ball4 = ifball(bas1,bas2,bas3,bas4,n,count,ball)
            bas1,bas2,bas3,bas4,score[n][count] = ball4[0],ball4[1],ball4[2],ball4[3],ball4[4]
            print('투수가 던진 공이',thr,'로 들어갔습니다.')
            if out == 3:
                print('3 out 체인지')
                out = 0
                bas1,bas2,bas3,bas4 = 'x','x','x','x'
                break
    #컴퓨터 타자
        print(count +1 ,'회말 입니다.')
        while True:
            n = 1
            print()
            h_aver = random.randint(1,100)
            v_aver = random.randint(1,100)
            if bas1 == 'x':
                strike,ball = 0,0
                runner = gohome()
            if  runner == 'a':
                bas1 = 'o'
            gameBoard1()
            gameBoard2(score[0][0],score[0][1],score[0][2],score[0][3],score[0][4],\
                       score[1][0],score[1][1],score[1][2],score[1][3],score[1][4])
            gameBoard3(ball,strike,out)
            gameBoard4(bas1,bas2,bas3,bas4)
            chit = random.randint(1,100)
            if 1<=chit<=90: 
                nhn = 'y'
            else:
                nhn = 'n'
            th = pitcher()
            thr = pitcher_(th,pform())
            if nhn == 'y':
                hit = hitterC(th,thr,sx1,sx2)
                if str(hit) in gzone[(int(thr)-1)//5 ]:
                    if str(thr) == '7' or str(thr) == '8' or str(thr) == '9' or \
                    str(thr) == '12' or str(thr) == '13' or str(thr) == '14' or\
                    str(thr) == '17' or str(thr) == '18' or str(thr) == '19' :
                        if int(thr) == hit :
                            print("쳤습니다.")
                            hitted = hita(v_aver,bas1,bas2,bas3,bas4,count,n,out)
                            bas1,bas2,bas3,bas4,score[n][count],out  = hitted[0],hitted[1],hitted[2],hitted[3],hitted[4],hitted[5]
                        else :
                            if 1<=h_aver<=80:
                                print("쳤습니다.")
                            
                                hitted = hita(v_aver,bas1,bas2,bas3,bas4,count,n,out)
                                bas1,bas2,bas3,bas4,score[n][count],out  = hitted[0],hitted[1],hitted[2],hitted[3],hitted[4],hitted[5]
                            else :
                                print("파울")
                                if strike < 2:
                                    strike = strike + 1
                    else:
                        if str(thr) == hit :
                            print("쳤습니다.")
                            if 1<=v_aver<=70:
                                hitted = hita(v_aver,bas1,bas2,bas3,bas4,count,n,out)
                                bas1,bas2,bas3,bas4,score[n][count],out  = hitted[0],hitted[1],hitted[2],hitted[3],hitted[4],hitted[5]
                            else:
                                print("파울")
                                if strike < 2:
                                    strike = strike + 1
                        else:
                            if 1<=h_aver<=50:
                                print("쳤습니다.")
                            
                                hitted = hita(v_aver,bas1,bas2,bas3,bas4,count,n,out)
                                bas1,bas2,bas3,bas4,score[n][count],out  = hitted[0],hitted[1],hitted[2],hitted[3],hitted[4],hitted[5]
                                             
                                             
                            else :
                                print("파울")
                                if strike < 2:
                                    strike = strike + 1
                else:
                    print("스윙")
                    strike = strike + 1
            else:
                print('타자가 배트를 휘두르지 않았습니다.')
                if str(thr) == '7' or  str(thr) == '8' or str(thr) == '9' or \
                str(thr) == '12' or str(thr) == '13' or str(thr) == '14' or\
                str(thr) == '17' or str(thr) == '18' or str(thr) == '19' :
                    print("스트라이크")
                    strike = strike + 1
                else :
                    print('볼')
                    ball = ball + 1
            if strike == 3:
                print('삼진 아웃')
                out = out + 1
                bas1 = 'x'
            ball4 = ifball(bas1,bas2,bas3,bas4,n,count,ball)
            bas1,bas2,bas3,bas4,score[n][count] = ball4[0],ball4[1],ball4[2],ball4[3],ball4[4]
            print('던진공이',thr,'로 들어갔습니다.')
            print('타자가',hit,'를 쳤습니다.')
            
            if out == 3:
                print('3 out 체인지')
                out = 0
                bas1,bas2,bas3,bas4 = 'x','x','x','x'
                break
        count = count + 1
        if count >4 :
            allscore1 = score[0][0] + score[0][1] + score[0][2] + score[0][3] + score[0][4]
            allscore2 = score[1][0] + score[1][1] + score[1][2] + score[1][3] + score[1][4]
            if allscore1 > allscore2:
                print('플레이어가',allscore1,'vs',allscore2,'로 승리하셨습니다.')
            elif allscore1 == allscore2:
                print('플레이어가',allscore1,'vs',allscore2,'비겼습니다.')
            else:
                print('플레이어가',allscore1,'vs',allscore2,'로 졌습니다.')
            break
    exi = input("종료하려면 q를 입력하시오")
    if exi == 'q':
        break
