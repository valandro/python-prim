![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

# PRIM Algorithm

In computer science, `Prim's` (also known as Jarník's) algorithm is a greedy algorithm that finds a `minimum spanning tree for a weighted undirected graph`. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized. The algorithm operates by building this tree one vertex at a time, from an arbitrary starting vertex, at each step adding the cheapest possible connection from the tree to another vertex.

### Running

```
python src/prim.py path/to/file
```

### Weighted Undirected Graph
Example:

**Graph**

![Graph image](/img/graph1.png)

**WUG File:**

`(node) (node) (distance)`
```
0 1 2
0 2 3
0 3 3
1 2 4
1 4 3
2 3 5
2 4 1
2 5 6
3 5 7
4 5 8
5 6 9
```

### License
[MIT License](LICENSE)