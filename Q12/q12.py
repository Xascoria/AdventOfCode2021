f = open("Q12/testinputs.txt","r")
a = [i.strip("\n") for i in f.readlines()]

f = open("Q12/inputs.txt","r")
b = [i.strip("\n") for i in f.readlines()]

graph = {}
lowercase = []

for i in b:
    c,d = i.split("-")
    if c not in graph:
        graph[c] = []
    graph[c] += [d]
    if d not in graph:
        graph[d] = []
    graph[d] += [c]
    if c.lower() == c and c not in lowercase:
        lowercase += [c]
    if d.lower() == d and d not in lowercase:
        lowercase += [d]

start = "start"


start_visited = [i=="start" for i in lowercase]

import copy

def recur(cur_node, cur_visit):

    if cur_node == "end":
        return 1

    count = 0
    possible_node = [i for i in graph[cur_node]]
    filtered = [i for i in possible_node if (i.upper()==i) or (not cur_visit[lowercase.index(i)])]
    #print(filtered)
    if len(filtered) == 0:
        return 0
    for i in filtered:
        if i==i.upper():
            count += recur(i, cur_visit)
        else:
            new_visit = copy.deepcopy(cur_visit)
            new_visit[lowercase.index(i)] = True
            count += recur(i, new_visit)
    return count

#print(lowercase,start_visited)

start_visited = [int(i=="start") for i in lowercase]
def recur2(cur_node, cur_visit):
    if cur_node == "end":
        return 1

    count = 0
    possible_node = [i for i in graph[cur_node]]
    
    filtered = []
    for i in possible_node:
        if i==i.upper():
            filtered += [i]
        elif 2 not in cur_visit:
            filtered += [i]
        elif cur_visit[lowercase.index(i)] == 0:
            filtered += [i]
    if len(filtered) == 0:
        return 0

    for i in filtered:
        if i==i.upper():
            count += recur2(i, cur_visit)
        elif i!="start":
            new_visit = copy.deepcopy(cur_visit)
            if 2 not in cur_visit:
                new_visit[lowercase.index(i)] += 1
            if 2 in cur_visit:
                new_visit[lowercase.index(i)] = 2
            count += recur2(i, new_visit)

    return count

print( recur2("start",start_visited) )



