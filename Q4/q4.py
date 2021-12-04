
f = open("Q4/inputs.txt","r")

order = list(map(int,f.readline().split(",")))

def check_board_victory(board):
    for i in board:
        if sum(i)==-5:
            return True
    for i in zip(*board):
        if sum(i) == -5:
            return True
    return False

def check_board_victory2(board):
    for i in board:
        print(i)
        if sum(i)==-5:
            return True
    for i in zip(*board):
        print(i)
        if sum(i) == -5:
            return True
    return False

boards = []
print(order)
b = f.readlines()
for i in range(len(b)//6):
    ri = i*6
    board = []
    for i in range(1,6):
        line1 = list(map(int,b[ri+i].split()))
        board.append(line1)
    boards.append(board)
for i in boards:
    #print(i[0][2])
    if i[0][1] == 12:
        print("yo")
        print(i)

# for num in order:
#     for brd in boards:
#         for j in range(len(brd)):
#             if num in brd[j]:
#                 brd[j][brd[j].index(num)] = -1
#         if check_board_victory(brd):
#             boards.remove(brd)
#             pass
#             # k = sum(brd,[])
#             # a = sum([t for t in k if t >0])
#             # print(a*num)
#             # 1/0;
#         if len(boards) == 1:
#             print(boards[0])
#             k = sum(boards[0],[])
#             a = sum([t for t in k if t >0])
#             print(a*num)
#             1/0;

counted = []
for num in order:
    for j in range(len(boards)):
        for k in range(5):
            while num in boards[j][k]:
                boards[j][k][boards[j][k].index(num)] = -1
        if check_board_victory(boards[j]):
            if j not in counted:
                counted.append(j)
        if len(boards) == len(counted):
            print(boards[counted[-1]])
            k = sum(boards[counted[-1]],[])
            a = sum([t for t in k if t >0])
            print(a,num)
            print(a*num)
            1/0;
    # for brd in boards:
    #     for j in range(len(brd)):
    #         if num in brd[j]:
    #             brd[j][brd[j].index(num)] = -1
    #     if check_board_victory(brd):
    #         boards.remove(brd)
    #         pass
    #         # k = sum(brd,[])
    #         # a = sum([t for t in k if t >0])
    #         # print(a*num)
    #         # 1/0;
    #     if len(boards) == 1:
    #         print(boards[0])
    #         k = sum(boards[0],[])
    #         a = sum([t for t in k if t >0])
    #         print(a*num)
    #         1/0;
