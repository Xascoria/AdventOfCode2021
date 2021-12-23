f = open("Q22/inputs.txt","r")
ques_input = [i.strip("\n") for i in f.readlines()]

from functools import cache

steps = []
for i in ques_input:
    a,b=i.split(" ")
    xr, yr, zr = b.split(",")
    xs,xe = map(int,xr[2:].split(".."))
    ys,ye = map(int,yr[2:].split(".."))
    zs,ze = map(int,zr[2:].split(".."))
    xe += 1
    ye += 1
    ze += 1
    steps += [(a, (xs, xe), (ys, ye), (zs,ze))]

## Rect format = x,y,x2,y2
@cache
def is_overlap(square_1, square_2):
    if square_1[2] <= square_2[0]:
        return False
    if square_2[2] <= square_1[0]:
        return False
    if square_1[3] <= square_2[1]:
        return False
    if square_2[3] <= square_1[1]:
        return False
    return True

@cache
def carve(square, area):
    if square == area:
        return []

    x_ranges = []
    y_ranges = []
    if square[0] < area[0]:
        x_ranges += [(square[0], area[0])]
    if square[2] > area[2]:
        x_ranges += [(area[2],square[2])]
    if square[1] < area[1]:
        y_ranges += [(square[1], area[1])]
    if square[3] > area[3]:
        y_ranges += [(area[3], square[3])]
    out = []
    if len(x_ranges) == 0:
        for i,j in y_ranges:
            out += [(square[0], i, square[2], j)]
        return out
    if len(y_ranges) == 0:
        for i,j in x_ranges:
            out += [(i, square[1], j, square[3])]
        return out
    for i,j in x_ranges:
        out += [(i, square[1], j, square[3])]
    if len(x_ranges) == 2:
        for i,j in y_ranges:
            out += [(x_ranges[0][1], i, x_ranges[1][0], j)]
        return out
    if x_ranges[0][0] == square[0]:
        for i,j in y_ranges:
            out += [(x_ranges[0][1],i, square[2],j)]
        return out
    for i,j in y_ranges:
        out += [(square[0],i, x_ranges[0][0],j)]
    return out

@cache
def carve_overlap(square_1, square_2):
    start_x = max(square_1[0], square_2[0])
    end_x = min(square_1[2], square_2[2])
    #print(start_x, end_x)
    start_y = max(square_1[1], square_2[1])
    end_y = min(square_1[3], square_2[3])

    area = (start_x, start_y, end_x, end_y)
    #print(square_1, square_2, area)
    ns1 = carve(square_1, area)
    ns2 = carve(square_2, area)
    return (ns1, ns2, area)

#print( carve_overlap((9, 9, 12, 12), (10, 10, 11, 13)) )
#1/0
d2 = {}
for i in steps:
    square = (i[1][0], i[2][0], i[1][1], i[2][1])
    if i[0] == "on":
        for j in range(i[3][0], i[3][1]):
            if j not in d2: 
                d2[j] = []
            overlapped_areas = []
            new_arr = []
            for k in d2[j]:
                if is_overlap(k, square):
                    res = carve_overlap(k, square)
                    new_arr += res[0] + [res[2]]
                    overlapped_areas.append(res[2])
                else:
                    new_arr.append(k)
            #TODO: reduce square turn on area
            new_sqr = [square]
            for k in overlapped_areas:
                new_csqr = []
                for l in new_sqr:
                    if is_overlap(k,l):
                        res = carve_overlap(k, l)
                        new_csqr += res[1]
                    else: new_csqr += [l]
                new_sqr = new_csqr
            new_arr += new_sqr
            d2[j] = new_arr

    else:
        for j in range(i[3][0], i[3][1]):
            if j not in d2:
                continue
            new_arr = []
            for k in d2[j]:
                if is_overlap(square, k):
                    #print(square,k)
                    res = carve_overlap(square, k)
                    #print(res[1])
                    new_arr += res[1]
                else:
                    new_arr += [k]
            
            d2[j] = new_arr
    

ans = 0
for i in d2.values():
    for j in i:
        ans += (j[2] - j[0]) * (j[3] - j[1])
print(ans)