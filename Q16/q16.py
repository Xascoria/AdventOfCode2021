# f = open("Q16/testinputs.txt","r")
# a = [i.strip("\n") for i in f.readlines()][0]

# f = open("Q16/inputs.txt","r")
# b = [i.strip("\n") for i in f.readlines()][0]

# bs = ""
# for i in a:
#     bs += bin(int(i,16))[2:].zfill(4)

# vn = 0
# def parser(binstr,pl):
#     global vn 
#     pv = binstr[:3]
#     pt = binstr[3:6]
#     vn += int(pv,2)
#     start = 6
#     nums = []
#     if int(pt,2) == 4:
#         print("literal vn",binstr)
#         while binstr[start] != "0":
#             nums += [int(binstr[start+1:start+5],2)]
#             start += 5
#         nums += [int(binstr[start+1:start+5],2)]
#         start += 5
#         while start % 4 != 0:
#             start += 1
#         if pl - 1 > 0 and len(binstr[start:])>11:
#             parser(binstr[start:],pl-1)
        
#     else:
#         lid = binstr[6]
#         u=0
#         content = ""
#         if lid == "0":
#             sublength = int(binstr[7:7+15],2)
#             u=sublength
#             start = 7+15
#             content = binstr[start:start+sublength]
#             print("c1",lid,u,content)
#             parser(content,10000)
#         else:
#             numsub = int(binstr[7:7+11],2)
#             u=numsub
#             start = 7+11
#             content = binstr[start:]
#             print("c2",lid,u,content)
#             parser(content,numsub)
        

# parser(bs,1) 
# print(vn)

# parser(bin(int("A0016C880162017C3686B18A3D4780",16))[2:])
# parser("0010001000000000010110001000000001011111000011011010000110101100011000101000111101010001111")
# parser("0110001000000001011111000011011010000110101100011000101000111101010001111")
# parser("1111000011011010000110101100011000101000111101010001111")

f = open("Q16/testinputs.txt","r")
test_input = [i.strip("\n") for i in f.readlines()][0]

f = open("Q16/inputs.txt","r")
ques_input = [i.strip("\n") for i in f.readlines()][0]

bs = ""
for i in test_input:
    bs += bin(int(i,16))[2:].zfill(4)

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
    # while si % 4 != 0:
    #     si += 1
    print("literal val",pv,pt,num,si)
    return (pv,pt,num,si)

def decode_op(binstr):
    global vn
    pv = int(binstr[:3],2)
    vn += pv
    pt = int(binstr[3:6],2)
    print("de:",pv,pt)
    lenid = int(binstr[6])
    outcon = []
    if lenid == 0:
        length = int(binstr[7:7+15],2)
        rest = binstr[7+15:7+15+length]
        start = 7+15
        while len(rest)>0:
            print("length decode",len(rest),rest,int(rest[3:6],2))
            if int(rest[3:6],2) == 4:
                a,b,c,d = decode_literal(rest)
                outcon += [(a,b,c)]
                start = d
            else:
                a,b,c,d = decode_op(rest)
                outcon += [(a,b,c)]
                start = d
            rest = rest[start:]
            
            
        return (pv,pt,outcon,7+15+length)
    else:
        times = int(binstr[7:7+11],2)
        start = 7+11
        rest = binstr[start:]
        yo = 7+11
        for i in range(times):
            print("times decode",rest,times)
            if int(rest[3:6],2) == 4:
                a,b,c,d = decode_literal(rest)
                outcon += [(a,b,c)]
                start = d
                yo += d
            else:
                a,b,c,d = decode_op(rest)
                outcon += [(a,b,c)]
                start = d
                yo += d
            rest = rest[start:]
        return (pv,pt,outcon,d)

def convertb(hexstr):
    a = int(hexstr,16)
    return bin(a)[2:]

print(bs)
decode_op(bs)
print(vn)