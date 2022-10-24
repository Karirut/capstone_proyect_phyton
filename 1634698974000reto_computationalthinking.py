# reto_computationalthinking.py
# Karina Ruiz A01656073
# Aylin Millan A01655861
# Capstone project: Find if there is any movements for the black king and see if it is checkmate or only check.

import random

def createBoard():
  b=[]
  shape='@'
  for row in range(8):
    r=[]
    for col in range(8):
      r.append(shape)
      if col < 7:
        if shape == "@":
          shape = "#"
        else:
          shape = "@"
    b.append(r)
  return b


def printBoard(b):
  for r in range(8):
    for c in range(8):
      print(b[r][c], end=" ")
    print()
  print()

def placek(b):
  rk = random.randint(0,7)
  ck = random.randint(0,7)
  b[rk][ck] = "k"
  return b

def find(piece, b):
  for r in range(8):
    for c in range(8):
      if b[r][c] == piece:
        return [r,c]
  return None

def placeK(b):
  posk = find("k", b)
  rk = posk[0]
  ck = posk[1]

  distR = 0
  distC = 0
  rk = 0
  cK = 0 

  while distR <= 1 and distC <= 1:
    rK = random.randint(0, 7)
    cK = random.randint(0, 7)

    distR = abs(rK - rk)
    distC = abs(cK - ck)
    
  b[rK][cK] = "K"
  return b

def placeQ(b):
  posk = find("k", b)
  rk = posk[0]
  ck = posk[1]

  posk = find("K", b)
  rK = posk[0]
  cK = posk[1]
  
  rQ = random.randint(0, 7)
  cQ = random.randint(0, 7)
  
  while (rQ == rK and cQ ==ck) or(rQ == rk and cQ == cK):
    rQ = random.randint(0, 7)
    cQ = random.randint(0, 7)
  
  b[rQ][cQ] = "Q"
  return b

#board = createBoard()
#board = placek(board)
#board = placeK(board)
#board = placeQ(board)
#printBoard(board)

def isMoveInside(move):
  row = move[0]
  col = move[1]
  if row >= 0 and row <=  7 and col >= 0 and col <= 7:
    return True 
  else:
    return False 

def findNeighborsFork(b):
  posk = find("k", b)
  rk = posk[0]
  ck = posk[1]

  neighborsk = [[rk,   ck+1], [rk-1,   ck+1], [rk-1,   ck], [rk-1,   ck-1], [rk,   ck-1], [rk+1,   ck-1], [rk+1,   ck], [rk+1,   ck+1]]

  positionsk = []
  for n in neighborsk:
    if isMoveInside(n):
      positionsk.append(n)

  return positionsk
  


def findNeighborsForK(b):
  posK = find("K", b)
  rK = posK[0]
  cK = posK[1]

  neighborsK = [[rK,   cK+1], [rK-1,   cK+1], [rK-1,   cK], [rK-1,   cK-1], [rK,   cK-1], [rK+1,   cK-1], [rK+1,   cK], [rK+1,   cK+1]]


  positionsK= []
  nk= findNeighborsFork(b)
  for n in neighborsK:
    if n not in nk:
      positionsK.append(n)

  return positionsK 

def findMovementsFork(b):
  nk= findNeighborsFork(b)
  nK = findNeighborsForK(b)
  nQ = findMovementsForQ(b)[0]

  positions= []
  for n in nk:
    if n not in nK:
      if n not in nQ:
        positions.append(n)
  return positions

def findMovementsForQ(b):
  posK = find("K", b)
  rK = posK[0]
  cK = posK[1]

  posk = find("k", b)
  rk = posk[0]
  ck = posk[1]

  posQ= find("Q", b)
  rQ = posQ[0]
  cQ = posQ[1]

  positionsQ= []
  check = False 

  for c in range(cQ-1, -1, -1):
    if b[rQ][c] == "K":
      break
    if b[rQ][c] == "k":
      check = True
    positionsQ.append([rQ, c])

  for c in range(cQ+1, 8, 1):
    if b[rQ][c] == "K":
      break
    if b[rQ][c] == "k":
      check = True
    positionsQ.append([rQ, c])

  for r  in range(rQ-1, -1, -1):
    if b[cQ][r] == "K":
      break
    if b[cQ][r] == "k":
      check = True
    positionsQ.append([r, cQ])

  for r in range(rQ+1, 8, 1):
    if b[cQ][r] == "K":
      break
    if b[cQ][r] == "k":
      check = True
    positionsQ.append([r, cQ])

  r1 = rQ
  c1 = cQ

  while r1 <= 7 and c1 <= 7:
    if b[r1][c1] == "K":
      break
    if b[r1][c1] == "k":
      check = True
    positionsQ.append([r1, c1])
    r1 += 1
    c1 += 1

  r1 = rQ
  c1 = cQ

  while r1 <= 7 and c1 >= 0:
    if b[r1][c1] == "K":
      break
    if b[r1][c1] == "k":
      check = True
    positionsQ.append([r1, c1])
    r1 += 1
    c1 -= 1
    
  r1 = rQ
  c1 = cQ

  while r1 >= 0 and c1 >= 0:
    if b[r1][c1] == "K":
      break
    if b[r1][c1] == "k":
      check = True
    positionsQ.append([r1, c1])
    r1 -= 1
    c1 -= 1  

  r1 = rQ
  c1 = cQ

  while r1 >= 0 and c1 <= 7:
    if b[r1][c1] == "K":
      break
    if b[r1][c1] == "k":
      check = True
    positionsQ.append([r1, c1])
    r1 -= 1
    c1 += 1

  return [positionsQ, check]


choice = int(input())
board = []

if choice == 1:
  board = createBoard()
  board = placek(board)
  board = placeK(board)
  board = placeQ(board)
else:
  for r in range(8):
    line = input()
    line = line.strip()
    row = line.split(" ")
    board.append(row)
printBoard(board)

#print (find("k", board))
#print(findMovementsFork(board))

movesk = findMovementsFork(board)
print("Black King Moves: ", movesk)

Checkmate= True
check1=findMovementsForQ(board)[1]

if len(findMovementsFork(board)) == 0 and check1 == True:
    print("Check:", check1)
    print("Checkmate:", Checkmate)
elif len(findMovementsFork(board)) != 0 and check1 == True:
    Checkmate = False
    print("Check:", check1)
    print("Checkmate:", Checkmate)
else:
  print("Check:", check1)
  print("Checkmate:", Checkmate)
