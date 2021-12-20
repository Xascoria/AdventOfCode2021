f = open("Q20/testinputs.txt","r")
#ques_input = [i.strip("\n") for i in f.readlines()]
a,b = f.read().split("\n\n")
b = "".join(b).split("\n")


trans = []
for i in range(-1,2,1):
    for j in range(-1,2,1):
        trans += [(i,j)]

# rowlength = len(b[0])
# top_row = [inf_symbol] * (rowlength+4)
inf_symbol = "."
flip_switch = True
for _ in range(50):
    
    rowlength = len(b[0])
    top_row = [inf_symbol] * (rowlength+4)
    new_matrix = []
    next_iter = []
    for _ in range(2): 
        new_matrix += [top_row[:]]
        next_iter += [top_row[:]]
    for c in b:
        new_matrix += [[inf_symbol]*2 + list(c) + [inf_symbol]*2]
        next_iter += [top_row[:]]
    for _ in range(2): 
        new_matrix += [top_row[:]]
        next_iter += [top_row[:]]

    b = new_matrix

    k = 0
    for i in range(1,len(new_matrix)-1):
        for j in range(1,len(new_matrix[i])-1):
            u = ""
            for x,y in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]:
                u += b[i+x][j+y]
            binnum = int(u.replace(".","0").replace("#","1"),2)
            next_iter[i][j] = a[binnum]
            # if j == 0:
            #     #print(i,j)
    b = [row[1:-1] for row in next_iter[1:-1]]
    if flip_switch:
        if inf_symbol == "#":
            inf_symbol = "."
        else:
            inf_symbol = "#"

    # for i in b:
    #     print("".join(i))
    # 1/0

fstr = ""
for i in b:
    fstr += "".join(i)
print(fstr.count("#"))