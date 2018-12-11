from sys import argv
import re

file = open(argv[1], "r")
# n = number max of nodes
nodes = 9
# m = number of arrests per node
arrests = (nodes - 1)
# Initialize graph array
graph = [[] * arrests] * nodes
# [[{'2', '5'}],[{'1', '6'}]]
# Each position of list is the node, and the structure is 'key' == node and 'value' == distance
# Reading all file into a arrays of arrays
for line in file:
    # Reading only lines there are not comments
    if not re.match("//", line):
        info = line.split(" ")
        # Remove \n of end of line
        arrest = {info[1]: info[2].replace('\n', '')}
        # If array is empty, so initalize them and append
        if len(graph[int(info[0])]) == 0:
            graph[int(info[0])] = []
            graph[int(info[0])].append(arrest)
        else:
            graph[int(info[0])].append(arrest)

# Set MST with a random value
prim = []
mst = []
mst = graph
min_dist = {}
lookup_node = 1
i = 0
while i < nodes:
    for node in range(len(mst)):
        for k in range(len(mst[node])):
            #If isn't in prim array and is the lookup node, then
            if mst[node][k] not in prim and int(list(mst[node][k].keys())[0]) == lookup_node:
                #If closest distance is empty, then
                if len(min_dist) == 0:
                    min_dist = mst[node][k]
                #If the node is before then min_dist node
                elif list(mst[node][k].keys())[0] <= list(min_dist.keys())[0]:
                    #And have a shorter distance, then
                    if list(mst[node][k].values())[0] < list(min_dist.values())[0]:
                        min_dist = mst[node][k]
    #Append
    prim.append(min_dist)
    #Reset variable
    min_dist = {}
    #Look for next node
    lookup_node += 1
    i += 1
print("-- MST nodes --")
print(prim)
print("-- Final cost --")
cost = 0
for i in prim:
    if i: 
        cost += int(list(i.values())[0])
print(cost)