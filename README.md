![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)

# PRIM Algorithm

In computer science, `Prim's` (also known as Jarník's) algorithm is a greedy algorithm that finds a `minimum spanning tree for a weighted undirected graph`. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized. The algorithm operates by building this tree one vertex at a time, from an arbitrary starting vertex, at each step adding the cheapest possible connection from the tree to another vertex.

### Running

```
python src/prim.py examples/*.wug
```

### Weighted Undirected Graph
Examples:

**Graph 1**

![Graph image](/img/graph1.png)

```
(node) (node) (distance)
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

**Graph 2**

![Graph image](/img/graph2.png)

```
(node) (node) (distance)
0 3 4
0 1 5
1 2 3
3 1 2
3 2 6
```

**Graph 3**

![Graph image](/img/graph3.png)

```
(node) (node) (distance)
0 1 7
0 3 5
1 3 9
1 2 8
1 4 7
2 4 5
3 4 15
3 5 6
4 5 8
4 6 9
5 6 11
```

### License
MIT License. [Click here for more information.](LICENSE)