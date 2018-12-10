from sys import argv
import re

file = open(argv[1], "r")
# n = number of nodes
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

print(graph)