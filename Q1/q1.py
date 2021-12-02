f = open("Q1/q1inputs.txt","r")
z = [*map(int,f.readlines())]
p=0
for i in range(1,len(z)):p += z[i]>z[i-1]
print(p)

# p=0
# for i in range(len(z)-3):
#     p += z[i+3]>z[i]
# print(p)
z=open("Q1/q1inputs.txt").readlines()
print(sum(int(z[i+3])>int(z[i])for i in range(len(z)-3)))

from math import atan2, degrees
f = open(filename,"r")
arr_of_nums = list(map(int,f.readlines()))

accumulate = 0
for i in range(1,len(arr_of_nums)):
    accumulate += degrees(atan2(arr_of_nums[i]-arr_of_nums[i-1],i-(i-1))) > 0
print(accumulate)
