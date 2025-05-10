import pytest
from tetris import drop_block, Grid

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
    def __init__(self, row_fill = 0):
        super().__init__()
        self.grid = [[1 if r <= row_fill else 0 for r in range(self.width)] for _ in range(self.height)]
        self.start = [len(self.grid)-1-row_fill for _ in range(len(self.grid[0]))] 


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



