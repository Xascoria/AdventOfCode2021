f = open("Q2/inputs.txt","r")
z = f.readlines()

c = d = 0
for i in z:
    #print(i)
    a,b = i.split()
    if a == "forward":
        c += int(b)
    elif a == "down":
        d += int(b)
    else:
        d -= int(b)
print(c*d)

c = d = 0
aim = 0
for i in z:
    #print(i)
    a,b = i.split()
    if a == "forward":
        c += int(b)
        d += aim*int(b)
    elif a == "down":
        #d += int(b)
        aim += int(b)
    else:
        #d -= int(b)
        aim -= int(b)
print(c*d)

submarine = [
    "         |_             ",
    "   _____|~ |____        ",
    "  (  --         ~~~~--_ ",
    "   ~~~~~~~~~~~~~~~~~~~'`"
]

f = open("Q2/inputs2.txt","r")
commands = f.readlines()

submarine = [
"             _|       ",
"        ____| ~|_____ ",
" _------         --  )",
"/'------------------- ",
]
ocean = [[*"~"*50]for _ in range(10)]
current_cord = [0,0]
for i in range(len(submarine)):
    for j in range(len(submarine[i])):
        ocean[i][j] = submarine[i][j]

for i in ocean:
    print("".join(i))
ocean = [[*"~"*50]for _ in range(10)]
for cmd in commands:
    print(cmd)
    action, num = cmd.split()
    if action == "forward":
        current_cord[1] += int(num)
    elif action == "up":
        current_cord[0] += int(num)
    else:
        current_cord[0] -= int(num)
    for i in range(len(submarine)):
        for j in range(len(submarine[i])):
            ocean[i+current_cord[0]][j+current_cord[1]] = submarine[i][j]

    for i in ocean:
        print("".join(i))
    ocean = [[*"~"*50]for _ in range(10)]

f = open("Q2/inputs.txt","r")
commands = f.readlines()

a = [((j[0][0]=="f")*int(j[1]), (j[0][0]!="f")*([-1,1][j[0][0]=="d"]*int(j[1]))) for i in commands if (j:=i.split())]
print(__import__("math").prod([sum(i) for i in zip(*a)]))

a = [((i.split()[0][0]=="f")*int(i.split()[1]),(i.split()[0][0]!="f")*([-1,1][i.split()[0][0]=="d"]*int(i.split()[1])))for i in open("inputs.txt").readlines()]
print(__import__("math").prod([sum(i)for i in zip(*[((i.split()[0][0]=="f")*int(i.split()[1]),(i.split()[0][0]!="f")*([-1,1][i.split()[0][0]=="d"]*int(i.split()[1])))for i in open("inputs.txt").readlines()])]))
# submarine = [
# "             _|       ",
# "        ____| ~|_____ ",
# " _------         --  )",
# "/'------------------- ",]
# ocean = [[*"~"*50]for _ in range(10)]
# for cmd in commands:
#     print(cmd)
#     action, num = cmd.split()
#     if action == "forward":
#         current_cord[1] += int(num)
#     elif action == "up":
#         current_cord[0] += int(num)
#     else:
#         current_cord[0] -= int(num)
#     for i in range(len(submarine)):
#         for j in range(len(submarine[i])):
#             ocean[i+current_cord[0]][j+current_cord[1]] = submarine[i][j]

#     for i in ocean:
#         print("".join(i))
#     ocean = [[*"~"*50]for _ in range(10)]