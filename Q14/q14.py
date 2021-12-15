f = open("Q14/inputs.txt","r")
a = [i.strip("\n") for i in f.readlines()]

f = open("Q14/testinputs.txt","r")
b = [i.strip("\n") for i in f.readlines()]

b=a
uec = c = a[0]
d = {}

for i in a[2:]:
    x,y = i.split(" -> ")
    d[x] = y

dd = {}
for i in range(len(c)-1):
    if c[i:i+2] not in dd:
        dd[c[i:i+2]] = 0
    dd[c[i:i+2]] += 1

c = set("".join(d.values()))
cd = {}

for i in range(40):
    for j in c:
        cd[j] = 0
    n = {}
    for j in dd:
        ne = d[j]
        if (j[0] + ne) not in n:
            n[j[0] + ne] = 0
        n[j[0] + ne] += dd[j]

        cd[j[0]] += dd[j]
        cd[ne] += dd[j]

        if (ne + j[1]) not in n:
            n[ne + j[1]] = 0
        n[ne + j[1]] += dd[j]
    cd[uec[-1]] += 1
    dd= n

# c = set("".join(dd.keys()))
# print(c)
# u = {}
# for i in c:
#     u[i] = 0
#     for j in dd.keys():

#         u[i] += dd[j]*(j[0]==i)
#         u[i] += dd[j]*(j[1]==i)
# print(u)
# print(max(u.values())-min(u.values()))

print(max(cd.values())-min(cd.values()))
print(len("COPBCNPOBKCCFFBSVHKO")*2**40/1024/1024/1024/1024)
