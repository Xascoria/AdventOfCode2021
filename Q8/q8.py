f = open("Q8/inputs.txt","r")

k = [i.strip("\n")for i in f.readlines()]

arr=["abcefg","cf","acdeg","acdfg","bcdf","abdfg","abdefg","acf","abcdefg","abcdfg"]
#print([len(i)for i in arr])

f = 0
t = []
for i in k:
    arr2 = [len(j) for j in i.split("|")[1].split(" ")]
    #print(arr2)
    t += arr2
arr2 = t
print(arr2.count(2) + arr2.count(4) + arr2.count(3) + arr2.count(7))

arrset = [set(i)for i in arr]
chars = "abcdefg"
import itertools

#print([i for i in itertools.permutations(chars)])


total = 0
for i in k:
    hint = i.split("|")[0].split(" ")[:-1]
    ans = i.split("|")[1].split(" ")[1:]
    a = [i for i in hint if len(i)==2][0]
    b = [i for i in hint if len(i)==3][0]
    original_a = [i for i in b if i not in a][0]
    c = [i for i in hint if len(i)==4][0]
    bandd = [i for i in c if i not in a]
    countc,countf= sum([a[0] in i for i in hint]),sum([a[1] in i for i in hint])
    if countc == 8:
        original_c = a[0]
        original_f = a[1]
    else:
        original_c = a[1]
        original_f = a[0]
    countb,countd = sum([bandd[0] in i for i in hint]),sum([bandd[1] in i for i in hint])
    if countb == 6:
        original_b = bandd[0]
        original_d = bandd[1]
    else:
        original_b = bandd[1]
        original_d = bandd[0]
    eight = [i for i in hint if len(i)==7][0]
    e_and_g = [i for i in eight if i not in [original_a, original_b, original_c, original_d, original_f]]
    counte = sum([e_and_g[0] in i for i in hint])
    if counte == 4:
        original_e = e_and_g[0]
        original_g = e_and_g[1]
    else:
        original_e = e_and_g[1]
        original_g = e_and_g[0]
    mapping = {original_a:"a",original_b:"b",original_c:"c",original_d:"d",original_e:"e",original_f:"f",original_g:"g"}

    u = []
    for i in ans:
        k = ""
        for j in i:
            k += mapping[j]
        u += [arr.index("".join(sorted(k)))]
    
    total += int("".join([str(i) for i in u]))
    
print(total)


f = open("Q8/inputs.txt","r")
k = [i.strip("\n")for i in f.readlines()]
f.close()
alp = "abcdefg"
org=["abcefg","cf","acdeg","acdfg","bcdf","abdfg","abdefg","acf","abcdefg","abcdfg"]

for i in k:
    hint,ans = i.split(" | ")
    four = [i for i in hint.split() if len(i)==4][0]
    mapping = {
        "a":[i for i in alp if hint.count(i)==8 and i not in four][0],
        "b":[i for i in alp if hint.count(i)==6][0],
        "c":[i for i in alp if hint.count(i)==8 and i in four][0],
        "d":[i for i in alp if hint.count(i)==7 and i in four][0],
        "e":[i for i in alp if hint.count(i)==4][0],
        "f":[i for i in alp if hint.count(i)==9][0],
        "g":[i for i in alp if hint.count(i)==7 and i not in four][0],
    }
