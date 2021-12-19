f = open("Q19/inputs.txt","r")
ques_input = [i.strip("\n") for i in f.readlines()]

scanners = {}
dists = {}


count = -1
arr = []
for i in range(len(ques_input)):
    if "" == ques_input[i]:
        scanners[count] = arr
        arr = []
        continue
    if "--" in ques_input[i]:
        count += 1
        continue
    a,b,c = map(int,ques_input[i].split(","))
    arr += [(a,b,c)]
scanners[count] = arr
count += 1

print(len(scanners[0]))

import math

for i in scanners:
    dists[i] = {}
    for j in range(len(scanners[i])-1):
        if j not in dists[i]: dists[i][j] = []
        for k in range(j+1,len(scanners[i])):
            if k not in dists[i]: 
                dists[i][k] = []
            #dists[i] += [(j,k,math.dist(scanners[i][j], scanners[i][k]))]
            ## Distance of scanner i of beacon j
            dists[i][j] += [math.dist(scanners[i][j], scanners[i][k])]
            dists[i][k] += [math.dist(scanners[i][j], scanners[i][k])]

# overlaps = {}
# for i in range(count-1):
#     set1 = set(dd[2]for dd in dists[i])
#     for j in range(i+1,count):
#         set2 = set(dd[2]for dd in dists[j])
#         overlaps[(i,j)] = len(set1 & set2)

# print(overlaps)
# y = get_all_postrans((1,2,3))
# print(y)
# print(len(set(y)))

def get_all_postrans(incord):
    a,b,c = incord
    first_axis = [(a,b,c), (-a,b,-c),(-b,a,c), (b,-a,c), (-c,b,a), (c,b,-a)]

    output = []
    for i in range(len(first_axis)):
        new_arr = []
        unchanged_axis = i//2
        #print(i//2)
        cx, cy = [i for i in (0,1,2) if i != unchanged_axis]
        x, y = [first_axis[i][k] for k in range(3) if k != unchanged_axis]
        transed = [(x,y),(-y,x),(-x,-y),(y,-x)]

        for j in range(4):
            nd = {}
            nd[unchanged_axis] = first_axis[i][unchanged_axis]
            nd[cx] = transed[j][0]
            nd[cy] = transed[j][1]
            new_t = (nd[0],nd[1],nd[2])
            new_arr.append(new_t)
        output += new_arr
    return output

solved = [True] + [False]*(count-1)
relative_rotation = [scanners[0]] + [None]*(count-1)

def cross_reference(stable_cords, first, second):
    #print(first, second)
    for i in dists[first]:
        original_coord = stable_cords[i]
        for j in dists[second]:
            overlap = [c for c in dists[first][i] if i in dists[second][j]]
            if len(overlap) >= 11:
                print("ypes")
                1/0
                for k in get_all_postrans(scanners[second][j]):
                    #print(k)
                    pass



while not all(solved):
    for i in range(count):
        if solved[i]:
            for j in range(count):
                if not solved[j]:
                    cross_reference(relative_rotation[i],i,j)
                    pass

