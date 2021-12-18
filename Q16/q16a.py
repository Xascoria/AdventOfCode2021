

def convertb(hexstr):
    binout = ""
    for i in hexstr:
        binout += bin(int(i,16))[2:].zfill(4)
    return binout


vn = 0
def decode_literal(binstr):
    global vn
    pv = int(binstr[:3],2)
    vn += pv
    pt = int(binstr[3:6],2)
    si = 6
    num=[]
    while binstr[si] == "1":
        num += [binstr[si+1:si+5]]
        si += 5
    num += [binstr[si+1:si+5]]
    si += 5
    #print("literal val",pv,pt,num,si)
    return (pv,pt,num,si)

def decode_op(binstr):
    global vn
    pv = int(binstr[:3],2)
    vn += pv
    pt = int(binstr[3:6],2)
    lenid = int(binstr[6])
    starting_index = 7
    outarr = []
    if lenid == 0:
        orglen = length = int(binstr[starting_index:starting_index+15],2)
        starting_index += 15
        while length > 0:
            #print("length",binstr[starting_index:],binstr[starting_index+3:starting_index+6])
            if int(binstr[starting_index+3:starting_index+6],2) == 4:
                a,b,c,d = decode_literal(binstr[starting_index:])
                outarr += [(a,b,c)]
                starting_index += d
                length -= d
            else:
                a,b,c,d = decode_op(binstr[starting_index:])
                outarr += [(a,b,c)]
                starting_index += d
                length -= d
        return (pv,pt,outarr,starting_index)
    else:
        looptime = int(binstr[starting_index:starting_index+11],2)
        starting_index += 11
        
        for _ in range(looptime):
            #print("looptime",looptime,binstr[starting_index:],binstr[starting_index+3:starting_index+6])
            if int(binstr[starting_index+3:starting_index+6],2) == 4:
                a,b,c,d = decode_literal(binstr[starting_index:])
                outarr += [(a,b,c)]
                starting_index += d
            else:
                a,b,c,d = decode_op(binstr[starting_index:])
                outarr += [(a,b,c)]
                starting_index += d
        return (pv,pt,outarr,starting_index)

f = open("Q16/testinputs.txt","r")
test_input = [i.strip("\n") for i in f.readlines()][0]

f = open("Q16/inputs.txt","r")
ques_input = [i.strip("\n") for i in f.readlines()][0]

# binstr = convertb(test_input)
# print(binstr)
# decode_op(binstr)
# print(vn)

vn = 0
def decode_literal(binstr):
    global vn
    pv = int(binstr[:3],2)
    vn += pv
    pt = int(binstr[3:6],2)
    si = 6
    num=[]
    while binstr[si] == "1":
        num += [binstr[si+1:si+5]]
        si += 5
    num += [binstr[si+1:si+5]]
    si += 5
    #print("literal val",pv,pt,num,si)
    newout = int("".join(num),2)
    return (pv,pt,newout,si)

def decode_op(binstr):
    global vn
    pv = int(binstr[:3],2)
    vn += pv
    pt = int(binstr[3:6],2)
    lenid = int(binstr[6])
    starting_index = 7
    outarr = []
    if lenid == 0:
        orglen = length = int(binstr[starting_index:starting_index+15],2)
        starting_index += 15
        while length > 0:
            #print("length",binstr[starting_index:],binstr[starting_index+3:starting_index+6])
            if int(binstr[starting_index+3:starting_index+6],2) == 4:
                a,b,c,d = decode_literal(binstr[starting_index:])
                outarr += [(a,b,c)]
                starting_index += d
                length -= d
            else:
                a,b,c,d = decode_op(binstr[starting_index:])
                outarr += [(a,b,c)]
                starting_index += d
                length -= d
        return (pv,pt,calculation(pt,outarr),starting_index)
    else:
        looptime = int(binstr[starting_index:starting_index+11],2)
        starting_index += 11
        
        for _ in range(looptime):
            #print("looptime",looptime,binstr[starting_index:],binstr[starting_index+3:starting_index+6])
            if int(binstr[starting_index+3:starting_index+6],2) == 4:
                a,b,c,d = decode_literal(binstr[starting_index:])
                outarr += [(a,b,c)]
                starting_index += d
            else:
                a,b,c,d = decode_op(binstr[starting_index:])
                outarr += [(a,b,c)]
                starting_index += d
        return (pv,pt,calculation(pt,outarr),starting_index)

import math
def calculation(pt, outarr):
    real = [i[2] for i in outarr]
    if pt == 0:
        return sum(real)
    if pt == 1:
        return math.prod(real)
    if pt == 2:
        return min(real)
    if pt == 3: 
        return max(real)
    if pt == 5:
        return int(real[0]>real[1])
    if pt == 6:
        return int(real[0]<real[1])
    if pt == 7:
        return int(real[0]==real[1])

binstr = convertb(test_input)
#print(binstr)
print(decode_op(binstr)[2])
#print(vn)

print(convertb("C0015000016115A2E0802F182340"))