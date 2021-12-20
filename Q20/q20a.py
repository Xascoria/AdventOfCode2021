import itertools

x = 0
d = {}
for i in itertools.product(".#", repeat=9):
    binnum = int("".join(i).replace(".","0").replace("#","1"),2)
    na = sum([i[j]=="#" for j in range(len(i)) if j != 4])
    if i[4] == "#":
        if na < 2:
            d[binnum] = "."
        elif na > 3:
            d[binnum] = "."
        else:
            d[binnum] = "#"
    else:
        if na == 3:
            d[binnum] = "#"
        else:
            d[binnum] = "."

u = ""
for i in range(max(d.keys())+1):
    #print(d[i])
    u += d[i]
print(u)
