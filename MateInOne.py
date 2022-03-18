# Problem Description:
# https://open.kattis.com/problems/checkmateinone

rows, cols = (8,8)
check = False
#'K': (5,6) -> King at 5th row, 6th column. 1-indexed
board = {}
for i in range(8):
  curr = list(input())
  for ii in range(8):
    if(curr[ii] == 'K' or curr[ii] == 'k' or curr[ii] == 'R'):
      board[curr[ii]] = (i+1,ii+1)

#if king is on last file
if(board['k'][0] == 8):
  if(board['K'][0] == 6):
    if(board['K'][1] == board['k'][1]):
      #if rook can reach 8th file 2 squares away
      if(board['R'][1] != board['k'][1] and (board['R'][1] != board['k'][1]+1) and (board['R'][1] != board['k'][1]-1)):
        print("Yes")
        exit()
    #if king is in corner
    elif(board['k'][1] == 1 and board['K'][1] == 2):
      if(board['R'][1] != 2):
        print("Yes")
        exit()
    elif(board['k'][1] == 8 and board['K'][1] == 7):
      if(board['R'][1] != 7):
        print("Yes")
        exit()

#if king is on first file
if(board['k'][0] == 1):
  if(board['K'][0] == 3):
    if(board['K'][1] == board['k'][1]):
      #if rook can reach 1st file 2 squares away
      if(board['R'][1] != board['k'][1] and (board['R'][1] != board['k'][1]+1) and (board['R'][1] != board['k'][1]-1)):
        print("Yes")
        exit()
    #if king is in corner
    elif(board['k'][1] == 1 and board['K'][1] == 2):
      if(board['R'][1] != 2):
        print("Yes")
        exit()
    elif(board['k'][1] == 8 and board['K'][1] == 7):
      if(board['R'][1] != 7):
        print("Yes")
        exit()

#if king is on last rank
if(board['k'][1] == 8):
  if(board['K'][1] == 6):
    if(board['K'][0] == board['k'][0]):
      #if rook can reach 8th rank 2 squares away
      if(board['R'][0] != board['k'][0] and (board['R'][0] != board['k'][0]+1) and (board['R'][0] != board['k'][0]-1)):
        print("Yes")
        exit()
    #if king is in corner
    elif(board['k'][0] == 1 and board['K'][0] == 2):
      if(board['R'][0] != 2):
        print("Yes")
        exit()
    elif(board['k'][0] == 8 and board['K'][0] == 7):
      if(board['R'][0] != 7):
        print("Yes")
        exit()

#if king is on first rank
if(board['k'][1] == 1):
  if(board['K'][1] == 3):
    if(board['K'][0] == board['k'][0]):
      #if rook can reach that rank/file 2 squares away
      if(board['R'][0] != board['k'][0] and (board['R'][0] != board['k'][0]+1) and (board['R'][0] != board['k'][0]-1)):
        print("Yes")
        exit()
    #if king is in corner
    elif(board['k'][0] == 1 and board['K'][0] == 2):
      if(board['R'][0] != 2):
        print("Yes")
        exit()
    elif(board['k'][0] == 8 and board['K'][0] == 7):
      if(board['R'][0] != 7):
        print("Yes")
        exit()

print("No")
