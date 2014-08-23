def guess(record):
    import random
    # the 4 functions

    # random attack

    def randomAttack(total_quads):

        # choose random point according to turn
        if turn == 50:
            x = total_quads[2][0][0]
            y = total_quads[2][0][1]
            print (x, y)
            return x, y
        elif turn == 51:
            x = 0
            y = 0
            print (x, y)
            return x, y
        elif turn % 12 in [1, 2, 3]:
            x = total_quads[0][0][0]
            y = total_quads[0][0][1]
            print (x, y)
            return x, y
        elif turn % 12 in [4, 5, 6]:
            x = total_quads[1][0][0]
            y = total_quads[1][0][1]
            print (x, y)
            return x, y
        elif turn % 12 in [7, 8, 9]:
            x = total_quads[2][0][0]
            y = total_quads[2][0][1]
            print (x, y)
            return x, y
        elif turn % 12 in [10, 11, 0]:
            x = total_quads[3][0][0]
            y = total_quads[3][0][1]
            print (x, y)
            return x, y

    # the first hit

    def firstHit():
        direction = record.data['direction']

        origin_x = log['guess']['x']
        origin_y = log['guess']['y']
        record.data['origin_x'] = origin_x
        record.data['origin_y'] = origin_y
        x = log['guess']['x']
        y = log['guess']['y']
        # turn up!
        turn_up = True
        record.data['turn_up'] = turn_up

        # right, left, up, down

        if record.get_status_at(x + 1)(y) == Board.Status.EMPTY:
            x = x + 1
            direction = 'right'
            return x, y
        elif record.get_status_at(x - 1)(y) == Board.Status.EMPTY:
            x = x - 1
            direction = 'left'
            return x, y
        elif record.get_status_at(x)(y + 1) == Board.Status.EMPTY:
            y = y + 1
            direction = 'up'
            return x, y
        elif record.get_status_at(x)(y - 1) == Board.Status.EMPTY:
            y = y - 1
            direction = 'down'
            return x, y
        else:
            print 'first hit ERROR!!'

        record.data['direction'] = direction

    # from the second hit go for this

    def hitHard():
        direction = record.data['direction']
        if turn_up==True && log['result']==Record.Status.MISSED:
            x = record.data['origin_x']
            y = record.data['origin_y']

            if record.get_status_at(x + 1)(y)==Board.Status.EMPTY:
                x = x + 1
                direction = 'right'
                return x, y
            elif record.get_status_at(x - 1)(y)==Board.Status.EMPTY:
                x = x - 1
                direction = 'left'
                return x, y
            elif record.get_status_at(x)(y + 1)==Board.Status.EMPTY:
                y = y + 1
                direction = 'up'
                return x, y
            elif record.get_status_at(x)(y - 1) == Board.Status.EMPTY:
                y = y - 1
                direction = 'down'
                return x, y
            else:
                print 'turn_up True and status empty ERROR!!'

            record.data['direction'] = direction

        elif turn_up == True && log['result'] == Record.Status.HIT:
            x = log['guess']['x']
            y = log['guess']['y']
            if direction == 'right':
                if record.get_status_at(x + 1, y) == Board.Status.EMPTY:
                    x = x + 1
                    return x, y
                else:
                    direction = 'left'
                    record.data['direction'] = direction
                    print 'change direction to left'
            elif direction == 'left':
                if record.get_status_at(x - 1, y) == Board.Status.EMPTY:
                    x = x - 1
                    return x, y
                else:
                    direction = 'up'
                    record.data['direction'] = direction
                    print 'change direction to up'

            elif direction == 'up':
                if record.get_status_at(x, y + 1) == Board.Status.EMPTY:
                    y = y + 1
                    return x, y
                else:
                    direction = 'down'
                    record.data['direction'] = direction
                    print 'change direction to down'
            elif direction == 'down':
                if record.get_status_at(x, y - 1) == Board.Status.EMPTY:
                    y = y - 1
                    return x, y
                else:
                    direction = None
                    record.data['direction'] = direction
                    print 'end of direction??'
            else:
                print 'turn_up True and status hit ERROR!!'
        else:
            print 'hitHard ERROR!!'

    # when the ship went down

    def sinkHard():
        turn_up = False
        record.data['turn_up'] = turn_up
        record.data['origin_x'] = None
        record.data['origin_y'] = None
        print sunk_ship, ' WENT DOWN!!'



    log = record.get_latest()
    if len(log) == 0:
        turn = 1
        record.data['turn'] = turn
        print turn  # to check
        trick = 'False'
        record.data['trick'] = trick

        # check hit flag
        turn_up = False
        record.data['turn_up'] = turn_up
        # checking for ships

        record.data['turn'] = turn
        ship_id = range(1, 6)
        record.data['ship_id'] = ship_id
        print turn  # to check

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
        record.data['total_quads'] = total_quads
        x = total_quads[0][0][0]
        y = total_quads[0][0][1]
        return x, y

    else:
         # divide the board into 4 quadrants and random attack

        turn = record.data['turn'] + 1
        record.data['turn'] = turn
        print turn  # to check
        total_quads = record.data['total_quads']

        # get the only empty points and then shuffle

        for quad in total_quads:
            for crd in quad:
                if record.get_status_at(crd[0], crd[1]) != Board.Status.EMPTY:
                    quad.remove(crd)
            random.shuffle(quad)
        print total_quads  # to check
        record.data['total_quads'] = total_quads


        # check hit flag
        turn_up = record.data['turn_up']

        # checking for ships
        trick = record.data['trick']
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
        print ship_id  # to check
        print sunk_ship  # to check
        print empty_ship  # to check


        # decide the mode
        if log['result'] == Record.Status.MISSED && turn_up == False:

            # if there was no hit but only miss

            randomAttack(total_quads)

        elif log['result'] == Record.Status.MISSED && turn_up == True:
            hitHard()

        elif log['result'] == Record.Status.HIT && turn_up == True:
            hitHard()

        elif log['result'] == Record.Status.HIT && turn_up == False:
            firstHit()

        elif log['result'] == Record.Status.SINK:
            sinkHard()
            randomAttack(total_quads)

        elif log['result'] == Record.Status.WIN:
            print 'I WON!!'
            x = 0
            y = 0
            return x, y
        else:
            print 'something WRONG in DECIDE MODE'


