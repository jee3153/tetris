class Grid:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.start = [len(self.grid)-1 for _ in range(len(self.grid[0]))] 
        

def drop_block(grid_object, block, x):
    grid = grid_object.grid
    if 0 > x or x + len(block[0]) >= len(grid)-1:
        raise ValueError("x value is not valid.")
    start = grid_object.start
    print(start)
    y = start[x] 
    width = len(block[0])
    height = len(block)

    for r in range(y, y-height, -1):
        for c in range(x, x+width):
            print(r, c)
            grid[r][c] = 1  
    start[x] -= height
    print(start)    
    print(grid)                      
