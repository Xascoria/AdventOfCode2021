f = open("Q11/testinputs.txt","r")
a = [i.strip("\n") for i in f.readlines()]

f = open("Q11/inputs.txt","r")
b = [i.strip("\n") for i in f.readlines()]

#print(a,b)

c = []
for i in a:
    k = [*map(int,i)]
    c += [k]

alt = [[False]*len(c[0]) for i in range(len(c))]
def re(board, i,j):
    count = 0
    if board[i][j] > 9 and not alt[i][j]:
        count += 1
        alt[i][j] = True
        for ii in range(-1,2):
            for jj in range(-1,2):
                if ii ==jj==0:
                    continue
                if i+ii < 0 or i +ii >= len(board):
                    continue
                if j+jj < 0 or j+jj >= len(board[0]):
                    continue
                board[i+ii][j+jj] += 1
                count += re(board,i+ii,j+jj)
    return count

ff = 0
for i in range(10000):
    d = []
    for j in c:
        d += [[*map(lambda x:x+1, j)]]
    for j in range(len(d)):
        for k in range(len(d[j])):
            ff += re(d, j,k)
    e = []
    for j in d:
        e += [[*map(lambda x: x if x < 10 else 0,j)]]
    
    c = e
    alt = [[False]*len(c[0]) for i in range(len(c))]
    ## PART 2
    p = []
    for j in c: p += j
    if len(set(p)) == 1 and p[0]==0:
        print(i)
        break
    # for j in e:
    #     print(j)
    # print(i)
    # if i == 5:break
print("ans",ff)