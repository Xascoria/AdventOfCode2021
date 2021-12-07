f = open("Q7/inputs.txt","r")

#print(((a:=[*map(int,open("inputs.txt","r").readline().split(","))]),min(sum([abs(i-j)*(abs(i-j)+1)//2 for j in a])for i in(int(sum(a)/len(a)),0--sum(a)//len(a))))[1])
#print((a:=[*map(int,f.readline().split(","))],min(sum([abs(j-i)*(abs(j-i)+1)//2 for j in a])for i in range(min(a),max(a)+1)))[1])
#print("yo")

a = [*map(int,f.readline().split(","))]
#a = [1, 1, 1, 1, 1, 100000]
# med = sorted(a)[len(a)//2]
# print(med)
# k = 0
# for i in a:
#     k += abs(i-med)
# print(k)

#a = [0,99,100]
c = min(a)
d = max(a)
u = []
for i in range(c,d+1):
    k = 0
    for j in a:
        n = abs(i-j)
        k += n*(n+1)//2
    u += [(k,i)]
print(min(u,key=lambda x:x[0]))

#a = [*map(int,f.readline().split(","))]
#t = min(sum([abs(j-i)*(abs(j-i)+1)//2 for j in a]) for i in range(c,d+1))
#print((a:=[*map(int,f.readline().split(","))],min(sum([abs(j-i)*(abs(j-i)+1)//2 for j in a]) for i in range(c,d+1)))[1])

# for i in [c,d,sum(a)//len(a)]:
#     k = 0
#     for j in a:
#         n = abs(i-j)
#         k += n*(n+1)//2
#     print("yo",i,k)

# print(min(a),max(a))
# avg = sum(a)/len(a)
# print("avg",avg)
# print(sum([i>avg for i in a]),len(a))

f = open("Q7/testinputs.txt","r")

#print(((a:=[*map(int,open("inputs.txt","r").readline().split(","))]),min(sum([abs(i-j)*(abs(i-j)+1)//2 for j in a])for i in(int(sum(a)/len(a)),0--sum(a)//len(a))))[1])
#print((a:=[*map(int,f.readline().split(","))],min(sum([abs(j-i)*(abs(j-i)+1)//2 for j in a])for i in range(min(a),max(a)+1)))[1])
#print("yo")

k = [*map(int,f.readline().split(","))]
print("mean",sum(k)/len(k))
print("median",sorted(k)[len(k)//2])
u = []
for i in range(0,max(k)):
    p = 0
    for j in k:
        n = abs(i-j)
        p += n*(n+1)//2
    u += [p]
print(min(u),u.index(min(u)))