current_sum = 0
prev = 0

while True:
    try:
        x = input()
        
        if x.lower() == "u":
            current_sum -= prev
        elif x.lower() == "r":
            current_sum = 0
            prev = 0
        else:
            x = int(x)
            prev = x
            current_sum += x
        print(current_sum)
    except:
        continue