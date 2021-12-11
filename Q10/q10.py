f = open("Q10/inputs.txt","r")

x = [i.strip("\n") for i in f.readlines()]


mappi = {"(":")","[":"]","{":"}","<":">"}
mappi2 = {")":"(","]":"[","}":"{",">":"<"}
err = ""
score = []
for i in x:
    stack = []
    for j in i:
        if j not in mappi and len(stack) == 0:
            err += j
            break
        if j in mappi:
            stack += j
        else:
            if mappi[stack[-1]] != j:
                err += j
                break
            else:
                stack.pop()
    else:
        scorem = {"]":2,")":1,"}":3,">":4}
        total = 0
        for i in stack[::-1]:
            total *= 5
            total += scorem[mappi[i]]
        score += [total]
print(err.count(")")*3 + err.count("]")*57 + err.count("}")*1197 + err.count(">")*25137)
print(score)
print(sorted(score)[len(score)//2])


    


