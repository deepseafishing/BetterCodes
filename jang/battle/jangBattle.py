from random import randint
def guess(record):


    B = [[150,100,130,100,100,140,100,130,100,130],[100,150,100,130,100,100,140,100,130,100],
[130,100,150,100,130,100,100,140,100,130],[100,130,100,150,100,130,100,100,140,100],
[100,100,130,100,150,100,130,100,100,140],[140,100,100,130,100,150,100,130,100,100],
[100,140,100,100,130,100,150,100,130,100],[130,100,140,100,100,130,100,150,100,130],
[100,130,100,140,100,100,130,100,150,100],[130,100,130,100,140,100,100,130,100,150]]
    history = record.get_history()
    history1 = record.get_history_at(0,'BACKWARD') #바로 전 턴 둘 이상일 때 마지막 히스토리 받아오기
    history2 = record.get_history_at(1,'BACKWARD')
    history3 = record.get_history_at(2,'BACKWARD')
    history4 = record.get_history_at(3,'BACKWARD')
    history5 = record.get_history_at(4,'BACKWARD')


    for i in history:
        #print i
        key_x = i['guess']['x']
        key_y = i['guess']['y']
        if i["result"] ==0:
            #print "doing1"
            B[key_x][key_y] -= 100000
            if key_x==0 and key_y==0:
                B[key_x+1][key_y] -= 20
                B[key_x][key_y+1] -= 20

            elif key_x==9 and key_y==9:
                B[key_x-1][key_y] -= 20
                B[key_x][key_y-1] -= 20

            elif key_x==0 and key_y==9:
                B[key_x+1][key_y] -= 20
                B[key_x][key_y-1] -= 20

            elif key_x==9 and key_y==0:
                B[key_x-1][key_y] -= 20
                B[key_x][key_y+1] -= 20

            elif key_x==0:
                B[key_x+1][key_y] -= 20
                B[key_x][key_y+1] -= 20
                B[key_x][key_y-1] -= 20
            elif key_x==9:
                B[key_x-1][key_y] -= 20
                B[key_x][key_y+1] -= 20
                B[key_x][key_y-1] -= 20
            elif key_y==0:
                B[key_x+1][key_y] -= 20
                B[key_x][key_y+1] -= 20
                B[key_x-1][key_y] -= 20
            elif key_y==9:
                B[key_x+1][key_y] -= 20
                B[key_x-1][key_y] -= 20
                B[key_x][key_y-1] -= 20
            else:
                B[key_x+1][key_y] -= 20
                B[key_x-1][key_y] -= 20
                B[key_x][key_y-1] -= 20
                B[key_x][key_y+1] -= 20
            #print "done1"

        elif i["result"] ==1:
            #print "doing2"
            B[key_x][key_y] -= 100000
            if key_x==0 and key_y==0:
                B[key_x+1][key_y] += 130
                B[key_x][key_y+1] += 130

            elif key_x==9 and key_y==9:
                B[key_x-1][key_y] += 130
                B[key_x][key_y-1] += 130

            elif key_x==0 and key_y==9:
                B[key_x+1][key_y] += 130
                B[key_x][key_y-1] += 130

            elif key_x==9 and key_y==0:
                B[key_x-1][key_y] += 130
                B[key_x][key_y+1] += 130

            elif key_x==0:
                B[key_x+1][key_y] += 130
                B[key_x][key_y+1] += 130
                B[key_x][key_y-1] += 130
            elif key_x==9:
                B[key_x-1][key_y] += 130
                B[key_x][key_y+1] += 130
                B[key_x][key_y-1] += 130
            elif key_y==0:
                B[key_x+1][key_y] += 130
                B[key_x][key_y+1] += 130
                B[key_x-1][key_y] += 130
            elif key_y==9:
                B[key_x+1][key_y] += 130
                B[key_x-1][key_y] += 130
                B[key_x][key_y-1] += 130
            else:
                B[key_x+1][key_y] += 130
                B[key_x-1][key_y] += 130
                B[key_x][key_y-1] += 130
                B[key_x][key_y+1] += 130
            #print "done2"

        elif i["result"] == 2:
            #print key_x, key_y
            #print "doing3"
            B[key_x][key_y] -= 100000
            if key_x==0 and key_y==0:
                #print "doing31"
                B[key_x+1][key_y] -= 20
                B[key_x][key_y+1] -= 20

            elif key_x==9 and key_y==9:
                #print "doing32"
                B[key_x-1][key_y] -= 20
                B[key_x][key_y-1] -= 20


            elif key_x==0 and key_y==9:
                B[key_x+1][key_y] -= 20
                B[key_x][key_y-1] -= 20

            elif key_x==9 and key_y==0:
                B[key_x-1][key_y] -= 20
                B[key_x][key_y+1] -= 20

            elif key_x==0:
                #print "doing33"
                B[key_x+1][key_y] -= 20
                B[key_x][key_y+1] -= 20
                B[key_x][key_y-1] -= 20
            elif key_x==9:
                #print "doing34"
                B[key_x-1][key_y] -= 20
                B[key_x][key_y+1] -= 20
                B[key_x][key_y-1] -= 20
            elif key_y==0:
                #print "doing35"
                B[key_x+1][key_y] -= 20
                B[key_x][key_y+1] -= 20
                B[key_x-1][key_y] -= 20
            elif key_y==9:
                B[key_x+1][key_y] -= 20
                B[key_x-1][key_y] -= 20
                B[key_x][key_y-1] -= 20
            else:
                B[key_x+1][key_y] -= 20
                B[key_x-1][key_y] -= 20
                B[key_x][key_y-1] -= 20
                B[key_x][key_y+1] -= 20
            #print "done3"
    print B
    #print historyprint B
    temp_x=0
    temp_y=0
    temp=0

    Max_list=[]

    for i in range(0,10):
        for j in range(0,10):
            if temp < B[i][j]:
                temp=B[i][j]
    #print "Max value: ",temp

    for i in range(0,10):
        for j in range(0,10):
            if B[i][j] == temp:
                Max_list.append({"x":i,"y":j})
    #print Max_list

    key = randint(0,len(Max_list)-1)
    #print len(Max_list)
    temp_x = Max_list[key]["x"]
    temp_y = Max_list[key]["y"]
    #print temp_x, temp_y
    x=temp_x
    y=temp_y

    return x, y