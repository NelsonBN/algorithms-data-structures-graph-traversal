# Algorithms and Data Structures - Graphs Traversal

## Demos

### From Matrix to Graph

**Problem**

Given a matrix, we will traverse it with graph traversal techniques to find the target element.

![Maze](./media/maze.svg)

**Movements Graph**
```mermaid
graph LR
  A((0,0))
  B((0,1))
  C((0,2))
  D((0,3))
  E((1,1))
  F((1,3))
  G((2,0))
  H((2,1))
  I((2,2))
  J((2,3))
  K((3,0))
  L((3,3))
  M((4,1))
  N((4,2))
  O((4,3))

  style B stroke:#0AF,stroke-width:2px;
  style M stroke:#FA0,stroke-width:2px;

  B <--> A
  B <--> E
  B <--> C
  C <--> D
  D <--> F
  E <--> H
  F <--> J
  H <--> G
  H <--> I
  I <--> J
  J <--> L
  G <--> K
  L <--> O
  O <--> N
  M <--> N
```

**Notes**
- The position start is at (0,1) where the cell has the value 'S'
- The target position is at (4,1) where the cell has the value 'E'
- The cells with the value 'X' are blocked cells

**Traversal**
- [Matrix - BFS (Breadth-First Search) Traversal](./src/matrix_bfs.py)
- [Matrix - DFS (Depth-First Search) Traversal](./src/matrix_dfs.py)


## References
- [Other Algorithms & Data Structures](https://github.com/NelsonBN/algorithms-data-structures)
