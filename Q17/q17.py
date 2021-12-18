
input_str = "target area: x=88..125, y=-157..-103"

ab = input_str.split()
xa,xb= map(int,ab[2][2:-1].split(".."))
ya,yb=map(int,ab[3][2:].split(".."))

pos = [0,0]
movement = [0,0]

x_accept = []
for i in range(1000):
    si = i
    cx = 0
    while si != 0:
        cx += i
        si -= 1
        if xa<=cx<=xb:
            x_accept += [i]
        elif xb<cx:
            break

print(xa,xb,ya,yb)
peaks = []
coords = set()
x_accept = [*set(x_accept)]
print(len(sorted([*set(x_accept)])),len([*range(10,126)]))
import time
st = time.time()
for xc in x_accept:
    for yc in range(-2000,3000,1):
        start = [0,0]
        movement = [xc,yc]
        sm = (xc,yc)
        #peak = start[1]
        while start[0]<=xb and start[1]>=ya:
            start[0] += movement[0]
            start[1] += movement[1]
            if movement[0] != 0:
                movement[0] -= 1
            movement[1] -= 1
            # if start[1] > peak:
            #     peak = start[1]
            if xa<=start[0]<=xb and ya <= start[1] <= yb:
                coords.add(sm)
                #peaks += [peak]
                break
        #print(start)
print(time.time()-st)
#2090 + 1392 + 
print(len(coords))
