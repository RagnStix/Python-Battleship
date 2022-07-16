import random
import sys
reveal=False                                                                     #Makes the ships appear on the board.
def printboard(board, reveal):                                                   #Function that prints game board/reveals game board.
  if reveal==True:
    for i in board:
      print(" ".join(map(str, i)))
  if reveal==False:
    for i in board1:
      print(" ".join(map(str, i)))
def sinkship(board, board1):                                                     #Detects how many shots it will take to sink a ship.
  flat_list = []                                                                 #Converts the nested list (gameboard) into one list to count number of required hits.
  for row in board:
      for item in row:
          flat_list.append(item)
  flat_listx= []
  for row in board1:
    for item in row:
      flat_listx.append(item)
  cs=flat_list.count('C')                                                        #Counts # of 'C's. Subtract one because the first collumn has a C.
  c=cs-1
  bs=flat_list.count('B')
  b=bs-1
  ds=flat_list.count('D')
  d=ds-1
  s=flat_list.count('S')
  xx=flat_listx.count('X')
  totalships=c+b+d+s                                                             #Adds up all the required hits.
  if totalships==xx:                                                             #Determines of player has hit all the ships.
    points1=1                                                                    #Value that tells program that the user has won.
    return points1
def torpedo(board, coord):                                                       #Function that lets user fire shots on game board.
  guessr=int(ord(coord[0])-64)                                                   #Converts the letter in the coordinate to a number. Y axis.
  guessc=int(coord[1])                                                           #Determins x axis position.
  target_value=board[guessr][guessc+1]                                           #Sets variable to coordinate points.
  if target_value=='-':                                                          #Determines if the shot was a miss. Will print 'O'
    board1[guessr][guessc+1]='O'
    print('Miss!')
    return board1                                                                #Updates gameboard.
  else:
    board1[guessr][guessc+1]='X'                                                 #Determines if the shot hit. Will print 'X'
    print('Hit!')
    return board1                                                                #Updates gameboard.
def vessel(board):                                                               #Assembles gameboard and assigns ships to it.
  ships={1: {'name': 'ship1', 'length': '5', 'orientation': random.randint(0,1)}, 2: {'name': 'ship2', 'length': '4', 'orientation': random.randint(0,1)}, 3: {'name': 'ship3', 'length': '3', 'orientation': random.randint(0,1)}, 4: {'name': 'ship4', 'length': '2', 'orientation': random.randint(0,1)}} #Includes ship name, length, and orientation.
  ship1=random.randint(1,2)                                                      #Randomly assigns a ship length of either 5 or 4.
  if ship1==1:                                                                   #Assigns ship length of 5 to board.
    shipa=5
    if ships[1]['orientation'] == 0:                                             #Makes the ship's orientation verticle.
      bb=random.randint(1, 4)                                                    #Determines the place where the ship will spawn along the y axis.
      bc=random.randint(1,8)                                                     #Determines the place where the ship will spawn along the x axis.
      board[bb][bc]='C'
      board[bb+1][bc]='C'
      board[bb+2][bc]='C'
      board[bb+3][bc]='C'
      board[bb+4][bc]='C'
      
    else:                                                                         #Makes the ship's orientation horizontal.
      aa=random.randint(1,8)
      ac=random.randint(1,4)
      board[aa][ac]='C'
      board[aa][ac+1]='C'
      board[aa][ac+2]='C'
      board[aa][ac+3]='C'
      board[aa][ac+4]='C'
  if ship1==2:                                                                    #Determines that the ship's length is 4.
    shipa=4
    if ships[2]['orientation'] == 0:
      bb=random.randint(1, 5)
      bc=random.randint(1, 8)
      board[bb][bc]='B'
      board[bb+1][bc]='B'
      board[bb+2][bc]='B'
      board[bb+3][bc]='B'


    else:
      aa=random.randint(1,8)
      ac=random.randint(1,5)
      board[aa][ac]='B'
      board[aa][ac+1]='B'
      board[aa][ac+2]='B'
      board[aa][ac+3]='B'

  ship2=random.randint(3,4)                                                        #Determines if the ship's length is 3 or 2.
  if ship2==3:                                                                     #Spawns the ship with a length of 3.
    shipb=3
    if ships[3]['orientation'] ==0:
      cc=random.randint(1,5)
      ca=random.randint(1,8)
      board[cc][ca]='S'
      board[cc+1][ca]='S'
      board[cc+2][ca]='S'

    else:
      cc=random.randint(1,8)
      ca=random.randint(1,5)
      board[cc][ca]='S'
      board[cc][ca+1]='S'
      board[cc][ca+2]='S'

  elif ship2==4:                                                                    #Spawns the ship with a length of 2.
    shipb=2
    if ships[4]['orientation'] ==0:
      cc=random.randint(1,6)
      ca=random.randint(1,8)
      board[cc][ca]='D'
      board[cc+1][ca]='D'

    else:
      cc=random.randint(1,8)
      ca=random.randint(1,6)
      board[cc][ca]='D'
      board[cc][ca+1]='D'

board=[[' ', 0, 1, 2, 3, 4, 5, 6 ,7],                                               #The board that the ships will spawn on.
        ['A', '-','-','-','-','-','-','-','-',],
        ['B', '-','-','-','-','-','-','-','-',],
        ['C', '-','-','-','-','-','-','-','-',],
        ['D', '-','-','-','-','-','-','-','-',],
        ['E', '-','-','-','-','-','-','-','-',],
        ['F', '-','-','-','-','-','-','-','-',],
        ['G', '-','-','-','-','-','-','-','-',],
        ['H', '-','-','-','-','-','-','-','-',]]
board1=[[' ', 0, 1, 2, 3, 4, 5, 6 ,7],                                              #The board where the 'X'(hits) and 'O'(misses) are placed.
        ['A', '-','-','-','-','-','-','-','-',],
        ['B', '-','-','-','-','-','-','-','-',],
        ['C', '-','-','-','-','-','-','-','-',],
        ['D', '-','-','-','-','-','-','-','-',],
        ['E', '-','-','-','-','-','-','-','-',],
        ['F', '-','-','-','-','-','-','-','-',],
        ['G', '-','-','-','-','-','-','-','-',],
        ['H', '-','-','-','-','-','-','-','-',]]
        
shots=20                                                                             #Sets the number of shots the player gets. 

print('+-------------------------------------------------------------+')             #The game's instructions.
print('| This program will randomly choose two ships from your fleet | ')
print('| made up of the following vessels: Carrier, Battleship, Sub- | ')
print('| marine, and Destroyer. It will then randomly assign both of | ')
print('| the vessels to the board that are oriented either vertical- | ')
print('| ly or horizontally. As a player you will then have up to 20 | ')
print('| tries to sink both of the computer\'s vessels                | ')
print('+-------------------------------------------------------------+')
print('Initializing board...')
print('Assigning ships...')
vessel(board)                                                                        #Assigns the ships to the board.
while True:                                                                          #Loop that catches errors.
  try:                                                                               #Loops each turn.
    while shots >= 1:                                                                #Lets the player play the game if they have shots left.
      printboard(board, reveal)                                                      #Prints gameboard.
      move=str(input("Please enter a coordinate to fire a torpedo(EX: C4): "))       #Prompts user to enter a point.
      #if move =='SAVE':                                                              
      coord=list(move)                                                               #Assigns the coordinate to a list.
      torpedo(board, coord)                                                          #Detects if entered point hit/missed the ships.
      shots-=1                                                                       #Takes away one shot from player's shots.
      sinkship(board, board1)                                                        #Checks to see if user sunk the ships.
      points1=sinkship(board, board1)                                                #Checks to see if user sunk all the ships and won.
      point=points1                                                                  #Value that determines if user won the game.
      if point!=1:                                                                   #Tells user how many shots they have if they haven't won.
        print('You have',shots,'shot(s) remaing!')
      if point==1:                                                                   #Tells user they won the game.
        print('You win! You sank my battleships in',shots,'shots!')
        for i in board:                                                              #Prints the gameboard with ships visable.
          print(" ".join(map(str, i)))
        sys.exit(0)                                                                  #Closes program.
    if shots ==0:                                                                    #Path is user runs out of shots.
      reveal=True                                                                    #Shows user gameboard if they run out of shots (lose).
      print('You lose! Get good.')                                                   #Statement that reminds user of their failure.
      for i in board:
        print(' '.join(map(str, i)))
      sys.exit(0)
  except IndexError:                                                                 
    print('Enter in a valid Y coordinate point and try again.')
    print(shots)
  except NameError:
    print('Please enter in a valid coordinate point')
  except ValueError:
    print('Please enter in a X valid coordinate point')