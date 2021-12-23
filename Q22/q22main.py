import time
from functools import cache

f = open("Q22/inputs.txt","r")
ques_input = [i.strip("\n") for i in f.readlines()]

main_instruc = []
for i in ques_input:
    a,b=i.split(" ")
    xr, yr, zr = b.split(",")
    xs,xe = map(int,xr[2:].split(".."))
    ys,ye = map(int,yr[2:].split(".."))
    zs,ze = map(int,zr[2:].split(".."))
    xe += 1
    ye += 1
    ze += 1
    main_instruc.append( (a, (xs, xe), (ys, ye), (zs,ze)) )

def merge_helper(e_start,e_end,current_ranges):
    return range_merge(e_start, e_end, tuple(current_ranges) )

#@cache
def range_merge(e_start,e_end,current_ranges):
    new_out = []
    inserted = False
    current_start = e_start
    current_end = e_end
    current_ranges = list(current_ranges)
    for index, thisrange in enumerate(current_ranges):
        #print(thisrange[1], current_start)
        #1/0
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

def remove_helper(e_start, e_end, current_ranges):
    return range_remove(e_start, e_end, tuple(current_ranges))

#@cache
def range_remove(e_start, e_end, current_ranges):
    new_out = []
    current_ranges = list(current_ranges)
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

def get_chuck_inst(main_inst):
    output = {}
    chuck_size = 5000

    for step in main_inst:
        for i in range(-100000, 100000, chuck_size):
            min_x = i
            max_x = i+chuck_size
            if step[1][0] >= max_x:
                continue
            if step[1][1] <= min_x:
                continue
            min_x = max(step[1][0], min_x)
            max_x = min(step[1][1], max_x)
            for j in range(-100000, 100000, chuck_size):
                min_y = j
                max_y = j+chuck_size
                if step[2][0] >= max_y:
                    continue
                if step[2][1] <= min_y:
                    continue
                min_y = max(step[2][0], min_y)
                max_y = min(step[2][1], max_y)
                out = (step[0], (min_x, max_x), (min_y, max_y), (step[2][0], step[2][1]))
                if (i,j) not in output:
                    output[(i,j)] = [out]
                else: output[(i,j)].append(out)
    return output

def calculate_chuck(chuck_instr):
    d2 = {}
    for i in chuck_instr:
        if i[0] == "on":
            for j in range(i[1][0], i[1][1]):
                for k in range(i[2][0], i[2][1]):
                    if (j,k) not in d2 or len(d2[(j,k)])==0:
                        d2[(j,k)] = [i[3]]
                    else:
                        d2[(j,k)] = range_merge(i[3][0], i[3][1], d2[(j,k)])
        else:
            for j in range(i[1][0], i[1][1]):
                for k in range(i[2][0], i[2][1]):
                    if (j,k) not in d2 or len(d2[(j,k)])==0:
                        continue
                    d2[(j,k)] = range_remove(i[3][0], i[3][1], d2[(j,k)])
    output = 0
    for i in d2.values():
        for j,k in i:
            output += k-j
    return output

chuck_instrucs = get_chuck_inst(main_instruc)
start_time = time.time()

result = 0

for i in chuck_instrucs:
    print(i)
    cs = time.time()
    result += calculate_chuck(chuck_instrucs[i])
    print("chuck finished",time.time()-cs)
print("End:",time.time()-start_time)
print(result)