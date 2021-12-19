f = open("Q18/inputs.txt","r")
ques_input = [i.strip("\n") for i in f.readlines()]

f = open("Q18/testinputs.txt","r")
test_input = [i.strip("\n") for i in f.readlines()]

def parser(instring):
    stackpath = []
    numstored = ""
    finalarr = []
    for i in range(len(instring)):
        if instring[i] == "[":
            if numstored:
                finalarr += [ [int(numstored), stackpath[::]] ]
                numstored = ""
            stackpath.append(0)
        elif instring[i] == "]":
            if numstored:
                finalarr += [ [int(numstored), stackpath[::]] ]
                numstored = ""
            stackpath.pop()
        elif instring[i] == ",":
            if numstored:
                finalarr += [ [int(numstored), stackpath[::]] ]
                numstored = ""
            stackpath[-1]=1
        else:
            numstored += instring[i]
    return finalarr

import math
def split(input1):
    index = 0
    output = []
    while index < len(input1):
        if input1[index][0] >= 10:
            output += [[int(math.floor(input1[index][0]/2)),input1[index][1][::]+[0]]]
            output += [[int(math.ceil(input1[index][0]/2)),input1[index][1][::]+[1]]]
            output += input1[index+1:]
            return (index, output)
        output += [input1[index]]
        index += 1
    return (len(output), output)

def explode(input1):
    index = 0
    output = []
    while index < len(input1):
        if index != len(input1)-1:
            if len(input1[index][1]) == len(input1[index+1][1]) and len(input1[index+1][1])>= 5 and input1[index][1][:-1] == input1[index+1][1][:-1]:
                if len(output) > 0:
                    output[-1][0] += input1[index][0]
                output += [[0, input1[index][1][::][:-1]]]
                if index != len(input1)-2:
                    input1[index+2][0] += input1[index+1][0]
                output += input1[index+2:]
                return (index,output)

        output += [input1[index]]
        index += 1
    return (len(output), output)


def addition(org, newstr):
    x = parser(newstr)
    for i in org:
        i[1] = [0] + i[1]
    for i in x:
        i[1] = [1] + i[1]
    # for i in org:
    #     print(i)
    # for j in x:
    #     print(j)
    output = org + x
    #output = parser("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]")
    #print("in",output)

    # index = 0
    # newout = []
    # while True:
    #     while index < len(output):
    #         ir = False
    #         ## Split
    #         if output[index][0] >= 10:
    #             newout += [[int(math.floor(output[index][0]/2)),output[index][1][::]+[0]]]
    #             newout += [[int(math.ceil(output[index][0]/2)),output[index][1][::]+[1]]]
    #             newout += output[index+1:]
    #             ir = True

    #         if ir:
    #             output = newout
    #             newout = []
    #             index = 0
    #             break
    #     index = 0
    #     while index < len(output):
    #         if index != len(output)-1:
    #             if len(output[index][1]) == len(output[index+1][1]) and len(output[index+1][1])>= 5 and output[index][1][:-1] == output[index+1][1][:-1]:
    #                 if len(newout) > 0:
    #                     newout[-1][0] += output[index][0]

    #                 newout += [[0, output[index][1][::][:-1]]]
    #                 if index != len(output)-2:
    #                     output[index+2][0] += output[index+1][0]
                        
    #                 newout += output[index+2:]
    #                 ir = True
        
    #     if ir:
    #         output = newout
    #         newout = []
    #         index = 0
    #         continue

    #     newout.append(output[index])
    #     index += 1

    while True:
        ind, out = explode(output)
        if ind != len(out):
            output = out
            continue
        ind, out = split(output)
        if ind != len(out):
            output = out
            continue
        break

    return output

x = parser(test_input[0])
# print(x)
# y = parser(test_input[1])
# print(y)
# print(x)
# print(parser(test_input[1]))
for i in range(1,len(test_input)):
    x = addition(x, test_input[i])

def magnitude(inputans):
    ind = 0
    newarr = []
    while len(inputans) != 1:
        if len(inputans[ind][1]) == len(inputans[ind+1][1]) and inputans[ind][1][:-1] == inputans[ind+1][1][:-1]:
            newarr += [[inputans[ind][0]*3+inputans[ind+1][0]*2 ,inputans[ind][1][:][:-1]]]
            
            newarr += inputans[ind+2:]
            inputans = newarr
            ind = 0
            newarr = []
            continue
        newarr += [inputans[ind]]
        ind += 1
        #print(len(inputans))
    return inputans[0][0]

print(magnitude(x))
mags = []
for i in range(len(test_input)-1):
    for j in range(i+1, len(test_input)):
        a = parser(test_input[i])
        b = parser(test_input[j])
        val1 = magnitude( addition(a,test_input[j]) )
        val2 = magnitude( addition(b,test_input[i]) )
        mags += [val1,val2]
print(max(mags))