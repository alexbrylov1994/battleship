###### Exercise Set 7 - Solution  ################

GRID_WIDTH = 10
GRID_HEIGHT = 10

VESSEL_NAMES = ["aircraft carrier", "battleship", "submarine", "destroyer"]
VESSEL_SIZES = [5,4,3,2]
NUM_OF_VESSELS = 4

B = '_'
HIT = 'X'
MISS = 'o'

# The class grid contains a single grid and all the functions that can
# be applied to a grid.  You can create multiple grids using:
# g1 = Grid()  (or grid_provided.Grid() is in a different module)
# g2 = Grid()
# g1 and g2 now are two distinct grids with the same functionality.
class Grid:
    # This code will be executed when a new instance of a grid is created
    def __init__(self) :
        self.grid = [[B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B], \
            [B,B,B,B,B,B,B,B,B,B]]

    def is_empty(self, row, column) :
        return self.grid[row][column] == B

    def on_grid(self, row, column) :
        return (row >= 0 and row < GRID_HEIGHT) and\
            (column >= 0 and column < GRID_WIDTH)

    # Drop some random bombs on the grid, just for testing.  All of
    # them are assumed to miss.
    def drop_test_bombs(self) :
        import random
        num_of_bombs = random.randint(5,50)
        for bomb_num in range(0,num_of_bombs) :
            row = random.randint(0,GRID_HEIGHT-1)
            column = random.randint(0,GRID_WIDTH-1)
            self.grid[row][column] = MISS

    # Pretty-prints this grid to the console.
    def print_grid(self) :
        print("   A B C D E F G H I J")
        for row_index in range(0, GRID_HEIGHT) :
            print(row_index + 1, '', end="")
            if (row_index + 1 < 10) :
                print(' ', end="")

            for column_index in range(0, GRID_WIDTH) :
                print(self.grid[row_index][column_index], '', end="")

            print()

    # Adds the vessel specified by the index to the current grid at top-left row,column
    # in direction indicated.  It does so by putting the size of the vessel
    # at each grid point the vessel occupies.
    def add_vessel(self, index, row, column, direction) :
        size = VESSEL_SIZES[index]

        if (direction == 'h') :
            for column_index in range(column, column + size) :
                self.grid[row][column_index] = size
        else :
            for row_index in range(row, row + size) :
                self.grid[row_index][column] = size

    # Adds the vessel specified by the index to the grid at top-left row,column
    # in direction indicated.  It does so by putting the size of the vessel
    # at each grid point the vessel occupies.
    def has_overlap(self, index, row, column, direction) :
        size = VESSEL_SIZES[index]
        overlap_found = False

        if (direction == 'h') :
            for column_index in range(column, column + size) :
                if (self.grid[row][column_index] != B) :
                    overlap_found = True
        else :
            for row_index in range(row, row + size) :
                if (self.grid[row_index][column] != B) :
                    overlap_found = True

        return overlap_found

    # Drops a bomb on defend grid and update both the defenders grid and
    # attachers grid to show if a vessel has been hit.
    def drop_bomb(self, attack_grid, bomb_row, bomb_column) :
        if (self.is_hit(bomb_row, bomb_column)) :
            self.grid[bomb_row][bomb_column] = HIT
            attack_grid.grid[bomb_row][bomb_column] = HIT
        else :
            self.grid[bomb_row][bomb_column] = MISS
            attack_grid.grid[bomb_row][bomb_column] = MISS

    # Checks if the specified location has been hit by a bomb in the past
    # in this grid.
    def is_hit(self, bomb_row, bomb_column) :
        return (self.grid[bomb_row][bomb_column] in VESSEL_SIZES)



    # Checks if all the vessels in the grid have been sunk.  The way it does this
    # is by ensuring all vessels have been replaced by a bomb.
    def all_vessels_sunk(self) :
        all_sunk = True
        for row in self.grid :
            for cell in row :
                if (cell in VESSEL_SIZES) :
                    all_sunk = False
        return all_sunk

