# Percolation

# My Forest Fire Modeling and Search Algorithms Project


### A. Class and methods:

#### Forests of Certain Density
- I modeled a forest as a two-dimensional list where each cell can either be occupied by a tree or empty.
- For a value d (between 0.0 and 1.0), a forest has density d if each cell is a tree with probability d or empty with probability (1 - d).

#### Modeling the Spread of Fire
- I modeled a forest fire by setting trees in the top row on fire.
- Fire spreads to neighboring trees (left, right, up, or down).
- A forest fire spreads if the fire makes it to the bottom row.

#### What I Implemented
- I created a class `Forest` representing the forest.
- The class has instance variables for the two-dimensional list of integers and two integers for the height and width of the grid.
- `__init__()`: takes integers for width and height, and float d for density. Creates the two-dimensional list and sets each element to either 1 (contains tree) with probability d or 0 (empty) with probability (1 - d).
- `__str__()`: returns string representation of the two-dimensional array.
- `depth_first_search()`: returns true if fire spreads using depth first search.
- `breadth_first_search()`: returns true if fire spreads using breadth first search.

### B. Depth First Search and Breadth First Search Algorithms

#### Depth First Search (DFS)
- I stored elements in a stack to expand one neighbor fully before moving onto the next.

#### Breadth First Search (BFS)
- Similar to DFS but uses a queue instead of a stack.
