f = open("Q3/inputs.txt","r")
z = f.readlines()
f.close()

a = ""
b = ""
for i in zip(*z):
    lst = list(i)
    if lst.count("1") > len(lst)//2:
        a += "1"
        b += "0"
    else:
        a += "0"
        b += "1"
print(int(a,2)*int(b,2))

f = open("Q3/inputs.txt","r")
z = f.readlines()
f.close()

current_index = 0
while len(z) != 1:
    lst = list(list(zip(*z))[current_index])
    if lst.count("1") > lst.count("0"):
        z = [i for i in z if i[current_index] == "1"]
    elif lst.count("1") < lst.count("0"):
        z = [i for i in z if i[current_index] == "0"]
    else:
        z = [i for i in z if i[current_index] == "1"]
    current_index += 1

a = int(z[0],2)

f = open("Q3/inputs.txt","r")
z = f.readlines()
f.close()

current_index = 0
while len(z) != 1:
    lst = list(list(zip(*z))[current_index])
    if lst.count("1") > lst.count("0"):
        z = [i for i in z if i[current_index] == "0"]
    elif lst.count("1") < lst.count("0"):
        z = [i for i in z if i[current_index] == "1"]
    else:
        z = [i for i in z if i[current_index] == "0"]
    current_index += 1

b = int(z[0],2)
print(a*b)