f = open("Q15/testinputs.txt","r")
a = [i.strip("\n") for i in f.readlines()]

f = open("Q15/inputs.txt","r")
b = [i.strip("\n") for i in f.readlines()]
print(len(b))
d= {}
def re(cur_cost, x,y):
    if (x,y) in d:
        return d[(x,y)]

    if x == y== len(b)-1:
        d[(x,y)] = int(b[x][y])
        return int(b[x][y])

    out = []
    if x != len(b)-1:
        out += [int(b[x][y]) + re(0,x+1,y)]

    if y != len(b)-1:
        out += [int(b[x][y]) + re(0,x,y+1)]

    d[(x,y)] = min(out)
    return min(out)

print(d)
print(re(0,0,0)-int(b[0][0]))

new_bs = [b]
for i in range(1,9):
    nb = []
    for j in new_bs[-1]:
        k = [(int(l)%9)+1 for l in j]
        nb.append(k)
    new_bs.append(nb)

giant = []

for i in range(5):
    for k in range(len(b)):
        nl = ""
        for j in range(5):
            nl += "".join(map(str,new_bs[i+j][k]))
        giant += [nl]

b = giant
print("start giant")

def djsktra():
    x = 0 
    y = 0
    
    p = {(0,0):0}
    v = set()
    current = (x,y)
    trans = [(1,0),(0,1),(-1,0),(0,-1)]
    uv = set()
    while not(current[0] == 499 and current[1] == 499):
        for i,j in trans:
            nx,ny = current[0]+i, current[1]+j
            if 0<=current[0]+i < len(b) and 0<=current[1]+j < len(b) and (nx,ny) not in v:
                if (nx,ny) not in p:
                    p[(nx,ny)] = p[current] + int(b[nx][ny])
                elif p[current] + int(b[nx][ny]) < p[(nx,ny)]:
                    p[(nx,ny)] = p[current] + int(b[nx][ny])
                uv.add((nx,ny))
        v.add(current)
        uu = current
        current = min(uv,key=lambda x:p[x])
        uv.remove(current)
    print(p[(499,499)])
djsktra()    


    


# import sys
# sys.setrecursionlimit(26000)
# d= {}
# def re(x,y):
#     if (x,y) in d:
#         return d[(x,y)]

#     if x == y== len(b)-1:
#         d[(x,y)] = int(b[x][y])
#         return int(b[x][y])

#     out = []
#     if x != len(b)-1:
#         out += [int(b[x][y]) + re(x+1,y)]

#     if y != len(b)-1:
#         out += [int(b[x][y]) + re(x,y+1)]

#     d[(x,y)] = min(out)
#     return min(out)

# for i in range(4,-1,-1):
#     for j in range(4,-1,-1):
#         re(i*100,j*100)
# print(re(0,0)-int(giant[0][0]))
