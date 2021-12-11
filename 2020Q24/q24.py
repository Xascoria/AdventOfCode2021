f = open("2020Q24/input.txt","r")

x = [i.strip("\n") for i in f.readlines()]

board = {}


for i in x:
    cur_x = cur_y = 0
    
    j = 0
    while j < len(i):
        if i[j] in "ew":
            if i[j] == "e":
                cur_x += 2
            else:
                cur_x -= 2
            j += 1
        else:
            if i[j] == "s":
                cur_y -= 1
            else:
                cur_y += 1
            if i[j+1] == "e":
                cur_x += 1
            else:
                cur_x -= 1
            j += 2
    if (cur_x, cur_y) not in board:
        board[(cur_x, cur_y)] = False
    board[(cur_x, cur_y)] = not board[(cur_x, cur_y)] 

print(sum(board.values()))

changes = [(0,0),(2,0),(-2,0),(1,1),(-1,1),(-1,-1),(1,-1)]

newboard = {}
for j in board:
    if board[j]: newboard[j] = True
board = newboard
#print(board.values())

import copy
for i in range(100):
    newboard = copy.deepcopy(board)
    for j in board:
        for k in changes:
            
            new_cord = (j[0]+k[0], j[1] + k[1])
            c = new_cord in board
            ba = 0
            for l in [(2,0),(-2,0),(1,1),(-1,1),(-1,-1),(1,-1)]:
                if (new_cord[0] + l[0], new_cord[1] + l[1]) in board:
                    ba += 1
            if ba == 0 or ba > 2:
                if c: newboard[new_cord] = False
            elif ba == 2 and not c: newboard[new_cord] = True
    newboard2 = {}
    for j in newboard:
        if newboard[j]: newboard2[j] = True
    board = newboard2
    #print(i,len(newboard), newboard.keys())
    #break

print(sum(newboard.values()))


