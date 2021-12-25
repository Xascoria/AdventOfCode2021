f = open("Q25/inputs.txt","r")
ques_input = [[*i.strip("\n")] for i in f.readlines()]

turn = 0
def destination(i,j, going_right):
    if going_right:
        if j == len(ques_input[0])-1:
            return (i,0)
        else:
            return (i,j+1)
    if i == len(ques_input)-1:
        return (0,j)
    return (i+1,j)

for i in ques_input:
    print("".join(i))

itar = 0
changed = False
new_iter = [["."]*len(ques_input[0]) for _ in range(len(ques_input))]
while True:
    for i in range(len(ques_input)):
        for j in range(len(ques_input[0])):
            if ques_input[i][j] == ">":
                des1,des2 = destination(i,j, True)
                if ques_input[des1][des2] == ".":
                    new_iter[des1][des2] = ">"
                    changed = True
                else:
                    new_iter[i][j] = ">"

    for i in range(len(ques_input)):
        for j in range(len(ques_input[0])):                 
            if ques_input[i][j] == "v":
                #print("yo",i,j)
                des1,des2 = destination(i,j, False)
                if new_iter[des1][des2] == "." and ques_input[des1][des2] != "v":
                    new_iter[des1][des2] = "v"
                    changed = True
                else:
                    new_iter[i][j] = "v"

    if True:
        if not changed:
            break
        ques_input = new_iter
        itar = 0
        turn += 1
        #print(turn)
        changed = False
        new_iter = [["."]*len(ques_input[0]) for _ in range(len(ques_input))]

print(turn+1)