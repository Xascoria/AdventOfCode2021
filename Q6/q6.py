f = open("Q6/inputs.txt","r")

# k = [*map(int,f.readline().split(","))]

# d = {}
# for i in k:
#     if i not in d:
#         d[i] = 0
#     d[i] += 1

# for i in range(256):
#     p = {0:0,1:0,2:0,3:0,4:0,5:0,7:0,6:0,8:0}
#     for j in d:
#         if j == 0:
#             p[6] += d[j]
#             p[8] += d[j]
#         else:
#             p[j-1]+=d[j]
#             #print(p[j-1])
#     d = p

# print(d)
# print(sum(d.values()))
import random
fish = "ゅ"
print(fish)

x = [["~"]*25 for _ in range(15)]
arr = [3,4,3,1,2,3,2]

for j in arr:
    rn = random.randrange(1,15)
    y = random.randrange(0,25)
    x[rn][y] = fish
    x[rn-1][y] = str(j)

for i in x:
    print("".join(i))

