f = open("Q1/q1inputs.txt","r")
z = [*map(int,f.readlines())]
p=0
for i in range(1,len(z)):p += z[i]>z[i-1]
print(p)

p=0
for i in range(1,len(z)-2):
    p += sum(z[i:i+3])>sum(z[i-1:i+2])
print(p)