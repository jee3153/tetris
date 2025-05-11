import pytest
from tetris import drop_block, Grid, Block, print_grid
from random import randint

blocks = [
    [[1], [1], [1], [1]], 
    [[1, 1], [1, 1]], 
    [[0, 1, 0], [1, 1, 1]], 
    [[1, 0], [1, 0], [1, 1]], 
    [[0, 1, 1], [1, 1, 0]]
]

# Helper function to validate the grid
def validate_grid(grid, expected_block, x, y):
    for i, row in enumerate(expected_block):
        for j, cell in enumerate(row):
            if cell == 1:
                assert grid[y + i][x + j] == 1

@pytest.mark.parametrize("block, x", [
    (Block.I.value, 0),  # Line block at x=0
    (Block.O.value, 4),  # Square block at x=4
    (Block.T.value, 4), 
    (Block.L.value, 2), 
    (Block.Z.value, 6) 
])
def test_empty_blocks(block, x):
    grid_object = Grid()
    grid = grid_object.grid
    expected_y = grid_object.width - len(block)
    drop_block(grid_object, block, x)
    validate_grid(grid, block, x, expected_y)

class UsedGrid(Grid):
    def __init__(self, highest_land):
        super().__init__()
        self.highest_land = highest_land
        self.generate_random()

    def generate_random(self):
        grid_height = self.height-1
        for r in range(grid_height, grid_height - self.highest_land, -1):
            for c in range(self.width):
                value = randint(0, 1)
                self.grid[r][c] = value
                if value == 1:
                    self.drop_point[c] = r-1

@pytest.mark.parametrize("block, x", [
    (Block.I.value, 1)
])
def test_non_empty_block(block, x):
    offset = 2
    grid_object = UsedGrid(offset)
    grid = grid_object.grid
    expected_y = grid_object.drop_point[x] - len(block) + 1
    drop_block(grid_object, block, x)
    validate_grid(grid, block, x, expected_y)

def test_clear():
    grid_obj = Grid()
    grid = grid_obj.grid
    drop_sequence = [
        (Block.T.value, 5),
        (Block.Z.value, 3),
        (Block.O.value, 8),
        (Block.L.value, 0)
    ]
    for block, x in drop_sequence:
        drop_block(grid_obj, block, x)

    expected_rows = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],[1, 0, 0, 0, 1, 1, 1, 0, 1, 1]]
    for i, row in enumerate(expected_rows):
        assert grid[17+i] == row
   
    
