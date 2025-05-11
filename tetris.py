from enum import Enum

class Grid:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.drop_point = [len(self.grid)-1 for _ in range(len(self.grid[0]))] 
        
class Block(Enum):
  I = [[1], [1], [1], [1]]
  O = [[1, 1], [1, 1]]
  T = [[0, 1, 0], [1, 1, 1]]
  L = [[1, 0], [1, 0], [1, 1]]
  Z = [[0, 1, 1], [1, 1, 0]]       

def mark_cells(grid_object, changing_cells):
    grid = grid_object.grid
    drop_point = grid_object.drop_point

    for r, c in changing_cells:
        grid[r][c] = 1
        drop_point[c] = min(drop_point[c], r-1)


def get_droppable(grid_object, block, x):
    grid = grid_object.grid    
    drop_point = grid_object.drop_point
    block_width = len(block[0])
    y_min = drop_point[x]
    y_max = drop_point[x]
    for i in range(x + 1, x + block_width):
        y_min = min(y_min, drop_point[i])
        y_max = max(y_max, drop_point[i])

    height = len(block)
    for y in range(y_max, y_min-1, -1):
        changing_cells = []
        valid = True

        for i, row in enumerate(block):
            for j, cell in enumerate(row):
                r = y-height+1+i
                c = x+j
                
                if r < 0:
                    valid = False
                    changing_cells.clear()
                    break
                if cell == 1 and grid[r][c] == 0:
                    changing_cells.append((r, c))     
                elif cell == 1 and grid[r][c] == 1:
                    valid = False
                    changing_cells.clear()
                    break  
            if not valid:
                break
        if valid:
            mark_cells(grid_object, changing_cells)
            return y    
    raise ValueError("No valid drop position found.")    



def clear_full_row(grid_object):
    grid = grid_object.grid
    drop_point = grid_object.drop_point
    highest_row = min(drop_point)

    for i in range(len(grid)-1, highest_row-1, -1):
        clear = False
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                clear = True
            else:
                clear = False
                break
        if clear:
            for r in range(i-1, -1, -1):
                grid[r+1] = grid[r][:] 
            grid[0] = [0] * len(grid[0])    

def recalculate_drop_points(grid_object):
    grid = grid_object.grid

    for c in range(grid_object.width):
        for r in range(grid_object.height):
            if grid[r][c] == 1:
                grid_object.drop_point[c] = r - 1
                break
        grid_object.drop_point[c] = grid_object.height-1

def drop_block(grid_object, block, x):
    grid = grid_object.grid

    if 0 > x or x + len(block[0]) > grid_object.width:
        raise ValueError("x value is not valid.")
    
    drop_point = grid_object.drop_point
    y = get_droppable(grid_object, block, x)
    height = len(block)

    for i, row in enumerate(block):
        for j, cell in enumerate(row):
            if cell == 1:
                r = y-height+1+i
                c = x+j
                grid[r][c] = 1 
                drop_point[c] = min(drop_point[c], r-1)

    clear_full_row(grid_object) 
    recalculate_drop_points(grid_object)           

def print_grid(grid):
    print("***********grid************")
    for row in grid:
        print_line = ""
        for cell in row:
            print_line += f"{cell} "
        print(print_line)
    print("***************************")    
# grid_object = Grid()

# blocks = [
#     [[1], [1], [1], [1]], 
#     [[1, 1], [1, 1]], 
#     [[0, 1, 0], [1, 1, 1]], 
#     [[1, 0], [1, 0], [1, 1]], 
#     [[0, 1, 1], [1, 1, 0]]
# ]
# drop_block(grid_object, [[0, 1, 0], [1, 1, 1]], 5)     
# print_grid(grid_object.grid)  
# drop_block(grid_object, [[0, 1, 1], [1, 1, 0]], 3) 
# print_grid(grid_object.grid)
# drop_block(grid_object, [[1, 1], [1, 1]], 8)
# print_grid(grid_object.grid)
# drop_block(grid_object, [[0, 1, 0], [1, 1, 1]], 0)
# print_grid(grid_object.grid)
