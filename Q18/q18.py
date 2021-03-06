import math

f = open("Q18/inputs.txt","r")
ques_input = [i.strip("\n") for i in f.readlines()]

f = open("Q18/testinputs.txt","r")
test_input = [i.strip("\n") for i in f.readlines()]

def parser(instring):
    stackcount = 0
    numstored = ""
    finalarr = []
    for i in range(len(instring)):
        if instring[i] == "[":
            if numstored:
                finalarr += [[stackcount-1, int(numstored)]]
                numstored = ""
            stackcount += 1
        elif instring[i] == "]":
            if numstored:
                finalarr += [[stackcount-1, int(numstored)]]
                numstored = ""
            stackcount -= 1
        elif instring[i] == ",":
            if numstored:
                finalarr += [[stackcount-1, int(numstored)]]
                numstored = ""
        else:
            numstored += instring[i]

    return finalarr

def addition(a,b):
    newarr = parser(b)
    for i in a:
        i[0] += 1
    for i in newarr:
        i[0] += 1
    output = a+newarr
    #return output
    index = 0
    new_out = []
    breakr = 0
    #print("before",output)
    while index < len(output):
        if output[index][0] == 4 and index != len(output)-1 and output[index+1][0] == 4:
            if index != 0:
                new_out[-1][1] += output[index][1]
            if index != len(output)-2:
                output[index+2][1] += output[index+1][1]
                #print(output[index+2][1],output[index+1][1])
            new_out += [[output[index][0]-1, 0]]+output[index+2:]
            output = new_out
            new_out = []
            index = 0

        elif output[index][1] >= 10:
            n1 = [output[index][0]+1, int(math.floor(output[index][1]/2))]
            n2 = [output[index][0]+1, int(math.ceil(output[index][1]/2))]
            new_out += [n1,n2]
            new_out += output[index+1:]
            output = new_out
            new_out = []
            index = 0
        else:
            new_out += [output[index]]
            index += 1
        #print(index,output)
        # breakr += 1
        # if breakr == 12:break


    return new_out

#print(parser(test_input[0]))
start = parser(test_input[0])
print(start)
for i in range(1,len(test_input)):
    start = addition(start, test_input[i])
    #print(start)
print(start)