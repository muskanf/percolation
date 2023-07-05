

import random
import matplotlib as plt


#This is the stack class and this will be the basis for the DFS algorithm
class Stack:
    def __init__(self):
        self.items = []
#check if the stack is empty
    def is_empty(self):
        return len(self.items) == 0
#add items in the stack
    def push(self, item):
        self.items.append(item)
#show the top-most value of the stack
    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop from an empty stack")
        return self.items.pop()
#return the top value of the stack
    def top(self):
        if self.is_empty():
            raise Exception("Cannot peek an empty stack")
        return self.items[-1]
#return the size of the stack
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return self.body.__str__()
#This is the queue class and this will be the basis for the BFS algorithm
class Queue:
    def __init__(self):
        self.items = []
#check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0
#add in queue  
    def enqueue(self, item):
        self.items.insert(0,item)
#remove from queue
    def dequeue(self):
        return self.items.pop()
#get size

    def size(self):
        return len(self.items)
    
    def __str__(self):
        return self.body.__str__()
#our forest
class Forest:
    def __init__(self, width, height, d):
        self.width = width
        self.height = height
        self.density = d

        # Create the two-dimensional list.
        self.grid = [[1 if random.random()<d else 0 for _ in range(height)] for _ in range(width)]

    def __str__(self):
        return '\n'.join(['|'.join([str(cell) for cell in row]) for row in self.grid])+'\n'
    

    def depth_first_search(self):
    # Get the last row of the grid
        last_row = self.grid[self.width - 1]
        # Create a stack to store cells to explore
        cells_to_explore = Stack()
        # Set the top row of the grid on fire
        for i in range(len(self.grid[0])):
            self.grid[0][i] = 2
            # Add the top row cells to the stack
            cells_to_explore.push(Cell(0, i))
        # While there are still cells to explore
        while cells_to_explore.size() != 0:
            # Pop a cell from the stack
            current_cell = cells_to_explore.pop()
            row = current_cell.row
            column = current_cell.column
            # Check if the cell below is within the grid and is a tree
            if row + 1 < self.width and self.grid[row + 1][column] == 1:
                # Set the cell on fire
                self.grid[row + 1][column] = 2
                # Add the cell to the stack
                cells_to_explore.push(Cell(row + 1, column))
            # Check if the cell to the right is within the grid and is a tree
            if column + 1 < self.width and self.grid[row][column + 1] == 1:
                # Set the cell on fire
                self.grid[row][column + 1] = 2
                # Add the cell to the stack
                cells_to_explore.push(Cell(row, column + 1))
            # Check if the cell to the left is within the grid and is a tree
            if column - 1 >= 0 and self.grid[row][column - 1] == 1:
                # Set the cell on fire
                self.grid[row][column - 1] = 2
                # Add the cell to the stack
                cells_to_explore.push(Cell(row, column - 1))
        # Return True if there is fire in the last row, False otherwise
        return 2 in last_row


    def breadth_first_search(self):
        # Get the last row of the grid
        last_row = self.grid[self.width - 1]
        # Create a queue to store cells to explore
        cells_to_explore = Queue()
        # Set the top row of the grid on fire
        for i in range(len(self.grid[0])):
            self.grid[0][i] = 2
            # Add the top row cells to the queue
            cells_to_explore.enqueue(Cell(0, i))
        # While there are still cells to explore
        while cells_to_explore.size() != 0:
            # print(self)
            # Dequeue a cell from the queue
            current_cell = cells_to_explore.dequeue()
            row = current_cell.row
            column = current_cell.column
            # Check if the cell below is within the grid and is a tree
            if row + 1 < self.width and self.grid[row + 1][column] == 1:
                # Set the cell on fire
                self.grid[row + 1][column] = 2
                # Add the cell to the queue
                cells_to_explore.enqueue(Cell(row + 1, column))
            # Check if the cell to the right is within the grid and is a tree
            if column + 1 < self.width and self.grid[row][column + 1] == 1:
                # Set the cell on fire
                self.grid[row][column + 1] = 2
                # Add the cell to the queue
                cells_to_explore.enqueue(Cell(row, column + 1))
            # Check if the cell to the left is within the grid and is a tree
            if column - 1 >= 0 and self.grid[row][column - 1] == 1:
                # Set the cell on fire
                self.grid[row][column - 1] = 2
                # Add the cell to the queue
                cells_to_explore.enqueue(Cell(row, column - 1))
        # Return True if there is fire in the last row, False otherwise
        return 2 in last_row

class Cell():
    def __init__(self, row, column):
        self.row=row
        self.column= column

#------------PART 2-----#

def fire_probability_dfs(width, height, density, trials=100):
    fire_spread_count = 0
    for _ in range(trials):
        forest = Forest(width, height, density)
        if forest.depth_first_search():
            fire_spread_count += 1
    return fire_spread_count / trials

def fire_probability_bfs(width, height, density, trials=100):
    fire_spread_count = 0
    for _ in range(trials):
        forest = Forest(width, height, density)
        if forest.breadth_first_search():
            fire_spread_count += 1
    return fire_spread_count / trials

def highest_density_dfs(forest, low_density=0.0, high_density=1.0, max_iterations=20):
    for _ in range(max_iterations):
        density = (high_density + low_density) / 2.0
        p = fire_probability_dfs(forest.width, forest.height, density)
        if p < 0.5:
            low_density = density
        else:
            high_density = density
    return density

def highest_density_bfs(forest, low_density=0.0, high_density=1.0, max_iterations=20):
    for _ in range(max_iterations):
        density = (high_density + low_density) / 2.0
        p = fire_probability_bfs(forest.width, forest.height, density)
        if p < 0.5:
            low_density = density
        else:
            high_density = density
    return density



import matplotlib.pyplot as plt

def plot_fire_probability(forest, max_density=1.0, step=0.01):
    densities = []
    probabilities_dfs = []
    probabilities_bfs = []
    density = 0.0
    while density <= max_density:
        prob_dfs = fire_probability_dfs(forest.width, forest.height, density)
        prob_bfs = fire_probability_bfs(forest.width, forest.height, density)
        densities.append(density)
        probabilities_dfs.append(prob_dfs)
        probabilities_bfs.append(prob_bfs)
        density += step

    plt.plot(densities, probabilities_dfs, label='DFS')
    plt.plot(densities, probabilities_bfs, label='BFS')
    plt.title("Results of Tree Density vs Probability of Fire Spread")
    plt.xlabel('Tree Density')
    plt.ylabel('Probability of Fire Spread')
    plt.legend()
    plt.show()

#creating a fire object and passing 0 here as density bc it doesn't even matter what we pass herre
forest = Forest(20, 20, 0)

# plot the probability of fire spread against tree density
plot_fire_probability(forest)
