f = open("Q19/inputs.txt","r")
ques_input = [i.strip("\n") for i in f.readlines()]

scanners = {}

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


all_pos_arr = [None]
for i in range(1,count):
    arr2 = []
    for j in scanners[i]:
        arr2 += [get_all_postrans(j)]
    all_pos_arr.append([*zip(*arr2)])

scanners_pos = []

def cross_compare(ind1, ind2, absvals1):
    global scanners_pos
    for i, point1 in enumerate(absvals1):
        for posspaceind in range(24):
            for j, point2 in enumerate(all_pos_arr[ind2][posspaceind]):
                trans = (point1[0]-point2[0], point1[1]-point2[1], point1[2]-point2[2],)
                shifted_points = [(i[0]+trans[0],i[1]+trans[1],i[2]+trans[2]) for i in all_pos_arr[ind2][posspaceind]]
                overlaps = [i for i in abscords[ind1] if i in shifted_points]
                if len(overlaps) >= 12:
                    scanners_pos += [trans]
                    return (True, shifted_points)
    
    return (False, None)


known = [True] + [False]*(count-1)
abscords = [scanners[0]] + [None]*(count-1)
no_overlaps = []


while not all(known):
    for i in range(count):
        for j in range(count):
            if i!=j and ((i,j) not in no_overlaps) and known[i] and (not known[j]):
                res,points = cross_compare(i,j, abscords[i])
                if res:
                    known[j] = True
                    print(j, "is known",31-sum(known),"left")
                    abscords[j] = points
                else:
                    no_overlaps += [(i,j),(j,i)]
    print("iteration finished")

fset = set(sum(abscords,[]))
print("finished")
print(len(fset))
        
# Part 2
print(scanners_pos)
finalpos =[]

flen = scanners_pos + [(0,0,0)] 

bigman = float("-inf")
for i in range(len(flen)-1):
    for j in range(i+1,len(flen)):
        man = abs(flen[i][0]-flen[j][0])+abs(flen[i][1]-flen[j][1])+abs(flen[i][2]-flen[j][2])
        if man> bigman:
            bigman = man
print(bigman)

