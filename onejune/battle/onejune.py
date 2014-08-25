def guess(record):
    import random
    # the 4 functions

    # random attack

    def randomAttack(total_quads):
        print 'RANDOM ATTACK !!' # to check
        randomhit = record.data['randomhit']
        randomhit = randomhit + 1
        record.data['randomhit'] = randomhit
        print 'this is randomhit >>  ', randomhit
        # choose random point according to turn
        if randomhit == 50:
            x = total_quads[2][0][0]
            y = total_quads[2][0][1]
            print 'randomhit point >>> ', (x, y)
            return x, y
        elif randomhit == 51:
            x = 0
            y = 0
            print 'over the random' 
            return x, y
        elif randomhit % 12 in [1, 2, 3]:
            if total_quads[0] != []:
                x = total_quads[0][0][0]
                y = total_quads[0][0][1]
                print 'randomhit point >>> ', (x, y)
                return x, y
            else:
                for quad in [1,2,3]:
                    if total_quads[quad] != []:
                        x = total_quads[quad][0][0]
                        y = total_quads[quad][0][1]
                        break
                print 'randomhit point >>> ', (x, y)
                return x, y
        elif randomhit % 12 in [4, 5, 6]:
            if total_quads[1] != []:
                x = total_quads[1][0][0]
                y = total_quads[1][0][1]
                print 'randomhit point >>> ', (x, y)
                return x, y
            else:
                for quad in [0,2,3]:
                    if total_quads[quad] != []:
                        x = total_quads[quad][0][0]
                        y = total_quads[quad][0][1]
                        break
                print 'randomhit point >>> ', (x, y)
                return x, y
        elif randomhit % 12 in [7, 8, 9]:
            if total_quads[2] != []:
                x = total_quads[2][0][0]
                y = total_quads[2][0][1]
                print 'randomhit point >>> ', (x, y)
                return x, y
            else:
                for quad in [0,1,3]:
                    if total_quads[quad] != []:
                        x = total_quads[quad][0][0]
                        y = total_quads[quad][0][1]
                        break
                print 'randomhit point >>> ', (x, y)
                return x, y
        elif randomhit % 12 in [10, 11, 0]:
            if total_quads[3] != []:
                x = total_quads[3][0][0]
                y = total_quads[3][0][1]
                print 'randomhit point >>> ', (x, y)
                return x, y
            else:
                for quad in [0,1,2]:
                    if total_quads[quad] != []:
                        x = total_quads[quad][0][0]
                        y = total_quads[quad][0][1]
                        break 
                print 'randomhit point >>> ', (x, y)
                return x, y
        else:
            print 'end of random Attack'        
    # the first hit

    def firstHit():
        direction = record.data['direction']
        print 'FIRST HIT !!' # to check
        origin_x = log['guess']['x']
        origin_y = log['guess']['y']
        record.data['origin_x'] = origin_x
        record.data['origin_y'] = origin_y
        x = log['guess']['x']
        y = log['guess']['y']
        print 'this is origin >> ', (origin_x, origin_y)
        print 'this is lastest >> ', (x, y)
        # turn up!
        turn_up = True
        record.data['turn_up'] = turn_up

        # right, left, up, down

        if x+1 in range(10) and record.get_status_at(x + 1, y) == Board.Status.EMPTY:
            x = x + 1
            direction = 'right'
            record.data['direction'] = direction
            print 'first hit >> ', direction, (x, y)
            return x, y
        elif x-1 in range(10) and record.get_status_at(x - 1, y) == Board.Status.EMPTY:
            x = x - 1
            direction = 'left'
            record.data['direction'] = direction
            print 'first hit >> ', direction, (x, y)
            return x, y
        elif y+1 in range(10) and record.get_status_at(x, y + 1) == Board.Status.EMPTY:
            y = y + 1
            direction = 'up'
            record.data['direction'] = direction
            print 'first hit >> ', direction, (x, y)
            return x, y
        elif y-1 in range(10) and record.get_status_at(x, y - 1) == Board.Status.EMPTY:
            y = y - 1
            direction = 'down'
            record.data['direction'] = direction
            print 'first hit >> ', direction, (x, y)
            return x, y
        else:
            print 'first hit ERROR!!'

    # from the second hit go for this

    def hitHard():
        print 'HIT HARD !!' # to check

        turn_up = record.data['turn_up']
        direction = record.data['direction']
        print 'turnup and direction >> ', turn_up, direction, log['result']
        if turn_up==True and log['result']==Record.Status.MISSED:
            print 'LAST Missed'
            x = record.data['origin_x']
            y = record.data['origin_y']

            if x+1 in range(10) and record.get_status_at(x + 1, y)==Board.Status.EMPTY:
                x = x + 1
                direction = 'right'
                record.data['direction'] = direction
                print 'miss right', (x, y)
                return x, y
            elif x-1 in range(10) and record.get_status_at(x - 1, y)==Board.Status.EMPTY:
                x = x - 1
                direction = 'left'
                record.data['direction'] = direction
                print 'miss left', (x, y)
                return x, y
            elif y+1 in range(10) and record.get_status_at(x, y + 1)==Board.Status.EMPTY:
                y = y + 1
                direction = 'up'
                record.data['direction'] = direction
                print 'miss up', (x, y)
                return x, y
            elif y-1 in range(10) and record.get_status_at(x, y - 1) == Board.Status.EMPTY:
                y = y - 1
                direction = 'down'
                record.data['direction'] = direction
                print 'miss down', (x, y)
                return x, y
            else:
                print 'turn_up True and status empty ERROR!!'


        elif turn_up == True and log['result'] == Record.Status.HIT:
            print 'LAST Hit'
            x = log['guess']['x']
            y = log['guess']['y']
            print 'hit again but not sink yet at >> ', (x, y)
            if direction == 'right':
                if x+1 in range(10) and record.get_status_at(x + 1, y) == Board.Status.EMPTY:
                    x = x + 1
                    print 'continue hit >> ', (x, y)
                    return x, y
                else:
                    direction = 'left'
                    print 'change direction to left'
                    x, y = backtoOriginal()
                    return x, y
            if direction == 'left':
                if x-1 in range(10) and record.get_status_at(x - 1, y) == Board.Status.EMPTY:
                    x = x - 1
                    print 'continue hit >> ', (x, y)
                    return x, y
                else:
                    direction = 'up'
                    print 'change direction to up'
                    x, y = backtoOriginal()
                    return x, y
            if direction == 'up':
                if y+1 in range(10) and record.get_status_at(x, y + 1) == Board.Status.EMPTY:
                    y = y + 1
                    print 'continue hit >> ', (x, y)
                    return x, y
                else:
                    direction = 'down'
                    print 'change direction to down'
                    x, y = backtoOriginal()
                    return x, y                    
            if direction == 'down':
                if y-1 in range(10) and record.get_status_at(x, y - 1) == Board.Status.EMPTY:
                    y = y - 1
                    print 'continue hit >> ', (x, y)
                    return x, y
                else:
                    print 'end of direction?? continue hit ERROR'
        else:
            print 'hitHard ERROR!!'

    # when the ship went down

    def sinkHard():
        print 'SINK HARD !!' # to check
        turn_up = False
        record.data['direction'] = 'newstart'
        record.data['turn_up'] = turn_up
        record.data['origin_x'] = None
        record.data['origin_y'] = None
        print sunk_ship, ' WENT DOWN!!'

    # the last shot was hit but the targeted point has also been shot
    # when turn up is true 
    def backtoOriginal():
        x = record.data['origin_x']
        y = record.data['origin_y']
        if x-1 in range(10) and record.get_status_at(x-1, y) == Board.Status.EMPTY:
            x = x-1
            record.data['direction'] = 'left'
            print 'goback and attack >> ', record.data['direction'], (x, y)
            return x, y
        elif y+1 in range(10) and record.get_status_at(x, y+1) == Board.Status.EMPTY:
            y = y+1
            record.data['direction'] = 'up'
            print 'goback and attack >> ', record.data['direction'], (x, y)
            return x, y
        elif y-1 in range(10) and record.get_status_at(x, y-1) == Board.Status.EMPTY:
            y = y-1
            record.data['direction'] = 'down'
            print 'goback and attack >> ', record.data['direction'], (x, y)
            return x, y
        else: 
            print 'fucking ERROR back to Origin'


    log = record.get_latest()
    if len(log) == 0:
        turn = 1
        record.data['turn'] = turn
        print turn  # to check
        # initialize random hit
        randomhit = 1
        record.data['randomhit'] = randomhit
        print 'this is randomhit >> ', randomhit
        # initialize direction
        record.data['direction'] = 'start'
        # check hit flag
        turn_up = False
        record.data['turn_up'] = turn_up
        # checking for ships

        ship_id = range(1, 6)
        record.data['ship_id'] = ship_id

        # divide the board into 4 quadrants and random attack

        first_quad = []
        for x in range(5):
            for y in range(5):
                if (x + y) % 2 == 0:
                    first_quad.append((x, y))
        second_quad = []
        for x in range(5, 10):
            for y in range(5):
                if (x + y) % 2 == 0:
                    second_quad.append((x, y))
        third_quad = map(lambda (x, y): (x + 5, y + 5), first_quad)
        fourth_quad = map(lambda (x, y): (x - 5, y + 5), second_quad)
        total_quads = [first_quad, second_quad, third_quad, fourth_quad]
        for quad in total_quads:
            for crd in quad:
                random.shuffle(quad)        

        record.data['total_quads'] = total_quads
        x = total_quads[0][0][0]
        y = total_quads[0][0][1]
        print total_quads
        print 'first turn point >> ', (x, y)
        return x, y

    else:
         # divide the board into 4 quadrants and random attack

        turn = record.data['turn'] + 1
        record.data['turn'] = turn
        print 'number of call>>', turn  # to check
        total_quads = record.data['total_quads']

        # get the only empty points and then shuffle
        print total_quads # to check
        for quad in total_quads:
            for crd in quad:
                if record.get_status_at(crd[0], crd[1]) != Board.Status.EMPTY:
                    print 'the removed point >> ', (crd[0], crd[1])
                    quad.remove(crd)
            random.shuffle(quad)
        print total_quads  # to check
        record.data['total_quads'] = total_quads


        # check hit flag
        turn_up = record.data['turn_up']

        # checking for ships
        ship_id = record.data['ship_id']
        ships_alive = record.get_remaining_ships()
        sunk_ship = [ship for ship in ship_id if ship not in ships_alive]
        empty_ship = []
        for ship in sunk_ship:
            empty_ship.append(ship)

        print sunk_ship  # to check
        if sunk_ship != []:
            ship_id.remove(empty_ship.pop())  # to check
            turn_up = False

        record.data['ship_id'] = ship_id
        record.data['turn_up'] = turn_up
        print 'this is ship_id >> ', ship_id  # to check
        print 'this is sunk_ship >> ', sunk_ship  # to check

        print log
        # decide the mode
        if log['result'] == Record.Status.MISSED and turn_up == False:

            # if there was no hit but only miss
            x, y = randomAttack(total_quads)
            return x, y
        elif log['result'] == Record.Status.MISSED and turn_up == True:
            x, y = hitHard()
            return x, y
        elif log['result'] == Record.Status.HIT and turn_up == True:
            x, y = hitHard()
            return x, y

        elif log['result'] == Record.Status.HIT and turn_up == False:
            x, y = firstHit()
            return x, y
        elif log['result'] == Record.Status.SINK:
            sinkHard()
            print total_quads
            x, y = randomAttack(total_quads)
            return x, y
        elif log['result'] == Record.Status.WIN:
            print 'I WON!!'
            x = 0
            y = 0
            return x, y
        else:
            print 'something WRONG in DECIDE MODE'

