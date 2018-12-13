from sys import argv
import re

file = open(argv[1], "r")
# The greatest node is equal to number of nodes - 1
greatest_node = -1
for line in file:
    # Reading only lines there are not comments
    if not re.match("//", line):
        info = line.split(" ")
        # Find the number of nodes
        if int(info[0]) > greatest_node:
            greatest_node = int(info[0])
        if int(info[1]) > greatest_node:
            greatest_node = int(info[1])            

# n = number max of nodes
nodes = greatest_node + 1
file.close()

# Graph list
graph = []
file = open(argv[1], "r")
for line in file:
    # Reading only lines there are not comments
    if not re.match("//", line):
        info = line.split(" ")
        # Create JSON and remove \n of end of line
        arrest = {info[0] + "&" +info[1]: info[2].replace('\n', '')}
        if int(info[0]) > greatest_node:
            greatest_node = int(info[0])
        if int(info[1]) > greatest_node:
            greatest_node = int(info[1])            
        # Add JSON to graph
        graph.append(arrest)

# Set MST with a random value
# List with the result
prim = []
# Auxiliar JSON to find the closest distance
min_dist = {}
# List of added nodes
added = []
# Add arbitary the first element
prim.append(graph[0])
# Add the nodes on added list
added.append(list(graph[0].keys())[0].split("&")[0])
added.append(list(graph[0].keys())[0].split("&")[1])
i = 0
while i < nodes:
    for node in range(len(graph)):
            # If isn't in prim array and is the lookup node, then
            n = list(graph[node].keys())[0].split("&")
            # Filter the nodes that can be added
            # At lest n[0] or n[1] must be added to this node be a candidate
            # And one of them must be not added before 
            if (n[0] in added or n[1] in added) and (n[0] not in added or n[1] not in added):
                #If closest distance is empty, then
                if len(min_dist) == 0:
                    min_dist = graph[node]
                #If the node is before then min_dist node
                elif list(graph[node].values())[0] < list(min_dist.values())[0]:
                        min_dist = graph[node]
    # Append
    if min_dist:
        prim.append(min_dist)
        added.append(list(min_dist.keys())[0].split("&")[0])
        added.append(list(min_dist.keys())[0].split("&")[1])
    # Reset variable
    min_dist = {}
    # Look for next node
    i += 1
# Final report
print("-- MST nodes --")
print(prim)
print("-- Final cost --")
cost = 0
for i in prim:
    if i:
        cost += int(list(i.values())[0])
print(cost)