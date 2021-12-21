import itertools

s = []
for i in itertools.product((1,2,3),repeat=3):
    s += [sum(i)]
print(s)
for i in range(10):
    print(s.count(i))