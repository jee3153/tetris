import pytest
from tetris import drop_block, Grid
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
    (blocks[0], 0),  # Line block at x=0
    (blocks[1], 4),  # Square block at x=4
    (blocks[2], 4), 
    (blocks[3], 2), 
    (blocks[4], 6) 
])
def test_empty_blocks(block, x):
    grid_object = Grid()
    grid = grid_object.grid
    expected_y = len(grid) - len(block)
    drop_block(grid_object, block, x)
    print(grid)
    validate_grid(grid, block, x, expected_y)

class UsedGrid(Grid):
    def __init__(self, highest_land):
        super().__init__()
        self.highest_land = len(self.grid) - 1 - highest_land
        self.generate_random()

    def generate_random(self):
        for r in range(self.highest_land, len(self.grid)):
            for c in range(len(self.grid[0])):
                value = randint(0, 1)
                self.grid[r][c] = value
                if value == 1:
                    self.drop_point[c] = min(self.drop_point[c], r)

@pytest.mark.parametrize("block, x", [
    (blocks[0], 1)
])
def test_non_empty_block(block, x):
    offset = 2
    grid_object = UsedGrid(offset)
    grid = grid_object.grid
    expected_y = len(grid) - offset - len(block)
    drop_block(grid_object, block, x)
    validate_grid(grid, block, x, expected_y)

def test_clear():
    grid_obj = Grid()
    grid = grid_obj.grid
    drop_sequence = [
        (blocks[2], 5),
        (blocks[4], 3),
        (blocks[1], 8),
        (blocks[2], 0)
    ]
    for block, x in drop_sequence:
        drop_block(grid_obj, block, x)

    expected_row = [0, 1, 0, 0, 1, 1, 1, 0, 1, 1]
    assert grid[19] == expected_row
    assert grid[18] == [0]*len(grid[0])    
    
