import math
f = open("Q24/inputs.txt","r")
ques_input = [i.strip("\n").split() for i in f.readlines()]


cache = {}

def run_prog(input_str):
    #input_str = input_string
    in_index = 0
    
    vars = {'w': 0, 'x':0, 'y': 0, 'z': 0}
    for i in ques_input:
        if i[0] == "inp":
            vars[i[1]] = int(input_str[in_index])
            in_index += 1
        elif i[0] == "add":
            if i[2] in vars:
                vars[i[1]] += vars[i[2]]
            else:
                vars[i[1]] += int(i[2])
        elif i[0] == "mul":
            if i[2] in vars:
                vars[i[1]] *= vars[i[2]]
            else:
                vars[i[1]] *= int(i[2])
        elif i[0] == "div":
            
            if i[2] in vars:
                sec = vars[i[2]]
            else:
                sec = int(i[2])
            ion = ((vars[i[1]] < 0) + (sec < 0)) == 1
            vars[i[1]] //= sec
            vars[i[1]] += ion
            # if ans >= 0:
            #     ans = int(ans)
            # else:
            #     ans = math.ceil(ans)
            #vars[i[1]] = ans
        elif i[0] == "mod":
            if i[2] in vars:
                vars[i[1]] %= vars[i[2]]
            else:
                vars[i[1]] %= int(i[2])
        elif i[0] == "eql":
            if i[2] in vars:
                vars[i[1]] = int(vars[i[1]] == vars[i[2]])
            else:
                vars[i[1]] = int(vars[i[1]] == int(i[2]))
        
    return vars

# for i in range(a,b-1, -1):
#     if "0" not in str(i):
#         res = run_prog(str(i))
#         if res:
#             print(i)
#             break
#     if i % 10000 == 0:
#         print(i)
#         break
# print(run_prog("4"))

# import itertools
# for i in itertools.product([9,8,7,6,5,4,3,2,1],repeat= 14):
#     res = run_prog(i)
#     if res:
#         print(i)
#         break
    # y -= 1
    # if  y == 0: 
    #     print(i)
    #     break

input_points = []
for index,i in enumerate(ques_input):
    if i[0] == "inp":
        input_points += [index]

from functools import cache
@cache
def eighteen_steps(w,z, z_divisor, x_adder, y_adder):
    x = int(((z % 26) + x_adder) != w)
    
    z = ((z//z_divisor) + (z < 0)) * ((25 * x) + 1) 
    y = (w + y_adder) * x
    z += y
    return z

@cache
def get_segment(start):
    x_adder = int(ques_input[start+5][2])
    z_divisor = int(ques_input[start+4][2])
    y_adder = int(ques_input[start+ 15][2])
    return (z_divisor,x_adder,y_adder)

def recursion(cur_string, cur_z):
    if len(cur_string) == 14:
        if cur_z == 0:
            print("SUCCESS", cur_string)
            1/0
        return 

    base26_digits = 0
    calz = cur_z
    while calz:
        calz //= 26
        base26_digits += 1
    base26_digits = max(base26_digits,1)
    if base26_digits > 7 or base26_digits > (14-len(cur_string)):
        #print("op",cur_string)
        return 

    for i in range(1,10):
        zd, xa, ya = get_segment(len(cur_string)*18)
        newz = eighteen_steps(i, cur_z, zd, xa, ya)
        recursion(cur_string+[i],newz)

#recursion([],0)
    
    
#print(run_prog([5, 1, 9, 3, 9, 3, 9, 7, 9, 8, 9, 9, 9, 9]))
print("".join(map(str,[1, 1, 7, 1, 7, 1, 3, 1, 2, 1, 1, 1, 9, 5])))
# prev = (0,)
# prev_same = 0
# stack = []
# itera = 10
# start_time = time.time()
# for i in itertools.product([1,2,3,4,5,6,7,8,9],repeat=14):
#     for j in range(14):
#         if i[j] != prev[j]:
#             break
#     stack = stack[:j]
#     if len(stack) != 0:
#         z_val = stack[-1]
#     else:
#         zd, xa, ya = get_segment(0)
#         stack += [eighteen_steps(i[0], 0, zd, xa, ya)]
#         j += 1
#     for k in range(j,14):
#         zd, xa, ya = get_segment(k*18)
#         stack.append(eighteen_steps(i[k], stack[-1], zd, xa, ya))
#     if stack[-1] == 0:
#         print(i, stack)
#         print(time.time()-start_time)
#         break
#     prev = i
