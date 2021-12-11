
f = open("Q9/inputs.txt","r")

x = [[*map(int,list(i.strip("\n")))] for i in f.readlines()]
low = 0
for i in range(len(x)):
    for j in range(len(x[i])):
        nc = 4
        if i == 0: nc -= 1
        if j == 0: nc -= 1
        if i == len(x)-1 : nc -= 1
        if j == len(x[i])-1: nc -= 1
        changes = [(1,0),(0,1),(-1,0),(0,-1)]
        real = 0
        for k,l in changes:
            if len(x) > i+k >= 0 and len(x[i]) > j+l >= 0:
                if x[i+k][j+l] > x[i][j]:
                    real += 1
        if real == nc:
            low += 1 + x[i][j]
print(low)

heatmap = [[False]*len(i) for i in x]
l1,l2 = len(x),len(x[0])

def recur(i,j):
    changes = [(1,0),(0,1),(-1,0),(0,-1)]
    count = 0
    if l1 > i >= 0 and l2 > j >= 0 and x[i][j] != 9 and not heatmap[i][j]:
        heatmap[i][j] = True
        count += 1
        for k,l in changes:
            count += recur(i+k, j+l)
    return count
        
def count_recur(i,j):
    changes = [(1,0),(0,1),(-1,0),(0,-1)]
    ns = 0
    if l1 > i >= 0 and l2 > j >= 0 and x[i][j] != 9 and heatmap[i][j]:
        heatmap[i][j] = False
        ns += 1
        for k,l in changes:
            ns += count_recur(i+k, j+l)
    return ns

counts = []
for i in range(len(x)):
    for j in range(len(x[i])):
        nc = 4
        if i == 0: nc -= 1
        if j == 0: nc -= 1
        if i == len(x)-1 : nc -= 1
        if j == len(x[i])-1: nc -= 1
        changes = [(1,0),(0,1),(-1,0),(0,-1)]
        real = 0
        for k,l in changes:
            if len(x) > i+k >= 0 and len(x[i]) > j+l >= 0:
                if x[i+k][j+l] > x[i][j]:
                    real += 1
        if real == nc:
            counts += [recur(i, j)]
            #low += 1 + x[i][j]
import math
print(math.prod(sorted(counts)[-3:]))