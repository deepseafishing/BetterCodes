def guess(record):
   board = record.get_board()
   remaining_ships = record.get_remaining_ships()
   latest_log = record.get_latest()

   if record.data == {}:
      record.data['direction'] = 'x'   
      record.data['flag'] = 0   
      record.data['x_count'] = 0
      record.data['y_count'] = 0


   if latest_log != {}:
      x = latest_log['guess']['x']
      y = latest_log['guess']['y']

      if latest_log['result'] == Record.Status.SINK:
         record.data['flag'] = 0

      if latest_log['result'] == Record.Status.HIT and record.data['flag'] == 0:
         record.data['flag'] = 1
         record.data['x'] = x
         record.data['y'] = y

   else:
      x = record.data['x_count']
      y = record.data['y_count']


   while record.get_status_at(x, y) != 0:
      if    latest_log['result'] == Record.Status.HIT and record.data['flag'] != 2:
         record.data['flag'] = 1

         if record.data['direction'] == 'x':
            x += 1

            if x > 9 or record.get_status_at(x, y) == Board.Status.MISSED:
               record.data['direction'] = '-x'
               record.data['flag'] = 2

         elif record.data['direction'] == '-x':
            x -= 1

            if x < 0 or record.get_status_at(x, y) == Board.Status.MISSED:
               record.data['direction'] = 'y'
               record.data['flag'] = 2

         elif record.data['direction'] == 'y':
            y += 1

            if y > 9 or record.get_status_at(x, y) == Board.Status.MISSED:
               record.data['direction'] = '-y'
               record.data['flag'] = 2

         elif record.data['direction'] == '-y':
            y -= 1

            if y < 0 or record.get_status_at(x, y) == Board.Status.MISSED:
               record.data['direction'] = 'x'
               record.data['flag'] = 2

      elif latest_log['result'] == Record.Status.MISSED and record.data['flag'] == 1:
         print "uuuu2"
         x = record.data['x']
         y = record.data['y']

         if record.data['direction'] == 'x':
            record.data['direction'] = '-x'

         elif record.data['direction'] == '-x':
            record.data['direction'] = 'y'

         elif record.data['direction'] == 'y':
            record.data['direction'] = '-y'

         elif record.data['direction'] == '-y':
            record.data['direction'] = 'x'


         if record.data['direction'] == 'x':
            x += 1

            if x > 9 or record.get_status_at(x, y) == Board.Status.MISSED:
               record.data['direction'] = '-x'
               record.data['flag'] = 2

         elif record.data['direction'] == '-x':
            x -= 1

            if x < 0 or record.get_status_at(x, y) == Board.Status.MISSED:
               record.data['direction'] = 'y'
               record.data['flag'] = 2

         elif record.data['direction'] == 'y':
            y += 1

            if y > 9 or record.get_status_at(x, y) == Board.Status.MISSED:
               record.data['direction'] = '-y'
               record.data['flag'] = 2

         elif record.data['direction'] == '-y':
            y -= 1

            if y < 0 or record.get_status_at(x, y) == Board.Status.MISSED:
               record.data['direction'] = 'x'
               record.data['flag'] = 2

      else:
         record.data['y_count'] += 2
      

         if record.data['y_count'] > 9:
            record.data['x_count'] += 1

            if record.data['x_count'] % 2 == 0:
               record.data['y_count'] = 0
            else:
               record.data['y_count'] = 1

         x = record.data['x_count']
         y = record.data['y_count']


      if record.data['flag'] == 2:
         record.data['flag'] = 1
         x = record.data['x']
         y = record.data['y']

   return x, y