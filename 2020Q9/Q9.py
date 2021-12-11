f = open("2020Q9/inputs.txt","r")

x = [int(i) for i in f.readlines()]
F=lambda a,b:sum(sum([[x[i]+x[j]==a for j in range(i+1,b)] for i in range(b-25,b)],[]))
F=(lambda a,b:sum(sum([[x[i]+x[j]==a for j in range(i+1,b)] for i in range(b-25,b)],[])))
def has_in_five(number,index):
    for i in range(index-25,index):
        for j in range(i+1,index):
            if x[i] +x[j] == number: return True
    return False
invalid_num = 0
for i in range(25,len(x)):
    if F(x[i],i) == 0:
        print(x[i],i)
        invalid_num = x[i]
        break

print("here")
print((x:=[int(i) for i in open("2020Q9/inputs.txt","r").readlines()],[x[i]for i in range(25,len(x))if not (lambda a,b:sum(sum([[x[i]+x[j]==a for j in range(i+1,b)] for i in range(b-25,b)],[])))(x[i],i)][0])[1])
#invalid_num = [x[i]for i in range(25,len(x))if not F(x[i],i)][0]


current_sum = 0
start_index = 0
end_index = 2
while end_index < 1000:
    if current_sum > invalid_num:
        start_index += 1
        if end_index - start_index < 2:
            end_index = start_index + 2
    elif current_sum < invalid_num:
        end_index += 1
    else:
        rg = x[start_index:end_index]
        print(max(rg)+min(rg))
        break
    current_sum = sum(x[start_index:end_index])
