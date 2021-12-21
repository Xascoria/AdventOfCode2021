f = open("Q21/inputs.txt","r")

a = [i.strip("\n")for i in f.readlines()]

p1s, p2s = [int(i.split()[-1]) for i in a]
p1s = p1s % 10
p2s = p2s % 10

s1 = s2 = 0

# current_side = 1
# nt = 0
# while (s1 < 1000) and (s2 < 1000):

#     cs = 0
#     for j in range(3):
#         cs += current_side
#         current_side += 1
#         if current_side == 101:
#             current_side = 1
#     nt += 3
#     p1s = (p1s + cs)%10
#     s1 += (p1s if p1s != 0 else 10)

#     if (s1>=1000):break
#     cs = 0
#     for j in range(3):
#         cs += current_side
#         current_side += 1
#         if current_side == 101:
#             current_side = 1
#     nt += 3
#     p2s = (p2s+cs)%10
#     s2 += (p2s if p2s != 0 else 10)
#     #print(p1s, p2s, s1,s2)

# print(min(s1,s2)*nt)

path_arr = [3, 4, 5, 6, 7, 8, 9]
multiplier = [0, 0, 0, 1, 3, 6, 7, 6, 3, 1]
def recursion(p1s, p2s, s1, s2, player1turn):
    if s1 >= 21 or s2 >= 21:
        return (s1 >= 21, s2 >= 21)

    out1 = out2 = 0
    if player1turn:
        for i in path_arr:
            np1s = (p1s + i)%10
            ns1 = s1 + (np1s if np1s != 0 else 10)
            re = recursion(np1s, p2s, ns1, s2, False)
            out1 += re[0] * multiplier[i]
            out2 += re[1] * multiplier[i]
    else:
        for i in path_arr:
            np2s = (p2s + i)%10
            ns2 = s2 + (np2s if np2s != 0 else 10)
            re = recursion(p1s, np2s, s1, ns2, True)
            out1 += re[0] * multiplier[i]
            out2 += re[1] * multiplier[i]
    
    return (out1, out2)

print(recursion(p1s, p2s, 0,0, True) )