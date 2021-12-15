f = open("Q13/inputs.txt","r")
a = [i.strip("\n") for i in f.readlines()]

points = []
for i in range(a.index("")):
    x,y = map(int,a[i].split(","))
    points += [(x,y)]

instru = []
for i in range(a.index("")+1,len(a)):
    x,y,z = a[i].split()
    x,y = z.split("=")
    instru += [(x,y)]

for j in instru:
    new_points = []
    which = j[0] == "y"

    for k in points:
        yo = [k[0],k[1]]
        if yo[which] > int(j[1]):
            yo[which] = int(j[1])-(yo[which]-int(j[1]))
        new_points += [(yo[0],yo[1])]
    #print(len(set(new_points)))
    #break

    points = [*set(new_points)]

mat = [[" "]*50 for i in range(20)]
for i,j in points:
    mat[j][i] = "."
for i in mat:
    print("".join(i))

percentage = 2
cost = 15
for i in range(5):
    cost *= 1.02
    print(cost)
print(cost)