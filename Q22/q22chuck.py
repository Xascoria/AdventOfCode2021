pstr="on x=7379..15679,y=62885..66145,z=40785..66699"

steps = []
for i in [pstr]:
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
    # x_min = min(xs,x_min)
    # x_max = max(xe,x_max)
    # y_min = min(ys,x_min)
    # y_max = min(ye,y_max)
    steps += [(a, (xs, xe), (ys, ye), (zs,ze))]

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

x = get_chuck_inst(main_instruc)
for i in x:
    print(i, x[i])