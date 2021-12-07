
f = open("Q5/inputs.txt","r")

x = [i.split(" -> ")for i in f.readlines()]

z = {}

for a,b in x:
    x1,y1 = map(int, a.split(","))
    x2,y2 = map(int, b.split(","))
    #print(x1,x2,y1,y2)
    #print(x1 ==x2 , y1==y2)
    if x1 == x2:
        a,b = min(y1,y2),max(y1,y2)
        for i in range(a,b+1):
            if (x1, i) not in z:
                z[(x1, i)] = 0
            z[(x1, i)] += 1
    elif y1 == y2:
        a,b = min(x1,x2),max(x1,x2)
        for i in range(a,b+1):
            if (i, y1) not in z:
                z[(i, y1)] = 0
            z[(i, y1)] += 1
    elif abs(x1-x2) == abs(y1-y2):
        # #print(x1,x2,y1,y2)
        # lowrx = min(x1,x2)
        # lowry = min(y1,y2)
        # #a,b = min(y1,y2),max(y1,y2)
        # for i in range(abs(x1-x2)-1):
        #     print(lowrx + i, lowry + i)
        #     if (lowrx + i, lowry + i) not in z:
        #         z[(lowrx + i, lowry + i)] = 0
        #     z[(lowrx + i, lowry + i)] += 1 
        xinc = [1,-1][abs(x2-x1) != (x2-x1)]
        yinc = [1,-1][abs(y2-y1) != (y2-y1)]
        for i in range(abs(x1-x2)+1):
            cord = (x1 + xinc*i, y1 + yinc*i)
            if cord not in z:
                z[cord] = 0
            z[cord] += 1 

#print(z)
for i in range(10):
    for j in range(10):
        if (j,i) in z:
            print(z[(j,i)],end="")
        else:
            print(".",end="")
    print()

k = 0
for i in z:
    if z[i] > 1: k += 1
print(k)