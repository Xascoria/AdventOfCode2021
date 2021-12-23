f = open("Q22/inputs.txt","r")
ques_input = [i.strip("\n") for i in f.readlines()]

steps = []
x_min = 0
x_max = 0
y_min = 0
y_max = 0
for i in ques_input:
    a,b=i.split(" ")
    xr, yr, zr = b.split(",")
    xs,xe = map(int,xr[2:].split(".."))
    ys,ye = map(int,yr[2:].split(".."))
    zs,ze = map(int,zr[2:].split(".."))
    # xs = max(-50, xs)
    # ys = max(-50, ys)
    # zs = max(-50, zs)
    # xe = min(50, xe)
    # ye = min(50, ye)
    # ze = min(50, ze)
    xe += 1
    ye += 1
    ze += 1
    x_min = min(xs,x_min)
    x_max = max(xe,x_max)
    y_min = min(ys,x_min)
    y_max = min(ye,y_max)
    steps += [(a, (xs, xe), (ys, ye), (zs,ze))]

print(x_min,x_max,y_min,y_max)

def range_merge(e_start,e_end,current_ranges):
    new_out = []
    inserted = False
    current_start = e_start
    current_end = e_end
    for index, thisrange in enumerate(current_ranges):
        if thisrange[1] < current_start:
            new_out += [thisrange]
            continue
        if thisrange[0] > current_end:
            new_out += [(current_start, current_end)]
            new_out += current_ranges[index:]
            inserted = True
            break
        if thisrange[0] <= current_start:
            current_start = thisrange[0]
        if thisrange[1] > current_end:
            current_end = thisrange[1]
            new_out += [(current_start, current_end)]
            new_out += current_ranges[index+1:]
            inserted = True
            break
    if not inserted:
        new_out += [(current_start,current_end)]

    return new_out

def range_remove(e_start, e_end, current_ranges):
    new_out = []
    for index, thisrange in enumerate(current_ranges):
        if thisrange[1] < e_start:
            new_out += [thisrange]
            continue
        if thisrange[0] > e_end:
            new_out += current_ranges[index:]
            break
        if thisrange[0] < e_start:
            # if thisrange[1] > e_end:
            #     new_out += [(thisrange[0], e_start), (e_end, thisrange[1])]
            #     new_out += current_ranges[index+1:]
            #     break
            new_out += [(thisrange[0], e_start)]
        if thisrange[1] > e_end:
            new_out += [(e_end, thisrange[1])]
            new_out += current_ranges[index+1:]
            break

    return new_out

res = range_merge(-6,6,[(-5,1),(6,7)])
res = range_remove(-2,15,[(-3,-1),(1,2),(3,4),(6,7)])
print(res)


        


d = set()
d2 = {}
for i in steps:
    if i[0] == "on":
        for j in range(i[1][0], i[1][1]):
            for k in range(i[2][0], i[2][1]):
                for l in range(i[3][0], i[3][1]):
                    d.add((j,k,l))
    else:
        for j in range(i[1][0], i[1][1]):
            for k in range(i[2][0], i[2][1]):
                if (j,k) in d:d.remove((j,k))
                for l in range(i[3][0], i[3][1]):
                    if (j,k,l) in d:
                        d.remove((j,k,l))

print(len(d))
# k = [i for i in d if 50>=i[0]>=-50 and 50>=i[1]>=-50 and 50>=i[2]>=-50]
# print(len(k))
