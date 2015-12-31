###### Exercise Set 7 - Solution - human module ################

import grid
from grid import B

defend_grid = grid.Grid()
attack_grid = grid.Grid()

# Interacts with the end user to drop a bomb on the attach grid.
# The function returns a row and column that is currently blank
# on the users attach grid.
def get_choice() :
    print("\n")
    attack_grid.print_grid()
    print("\nChoose a location to drop a bomb.")
    column = ord(input("\tColumn: ")) - ord('A')
    row = int(input("\tRow: ")) - 1
    while (not attack_grid.on_grid(row, column)) :
        print("Invalid location")
        column = ord(input("\tColumn: ")) - ord('A')
        row = int(input("\tRow: ")) - 1

    ###
    if (not attack_grid.is_empty(row, column)) :
        print("\nYou've already thrown a bomb in that location.")
        row,column = get_choice()

    return row,column
        
# Checks if the row,column is valid for vessel of size and direction.
# It also makes sure it won't overlap with an existing vessel on the
# defense grid.  If the location is valid, this function returns True.  
# If not, it prints an appropriate error message and returns False.    
def valid_location(vessel_index, row, column, direction) :
    valid = True
    if (not defend_grid.on_grid(row, column)) :
        # Start point is not on the grid.
        valid = False
    elif (direction != "h" and direction != "v") :
        print(direction)
        # Direction entered is not valid.
        print("Invalid direction.  Direction must be either h for horizontal or v for vertical.")
        valid = False
    else :
        size = grid.VESSEL_SIZES[vessel_index]
        # Need to check if the entire vessel fits on the grid
        if (direction == 'h' and column + size > grid.GRID_WIDTH) :
            print("Invalid column.  The vessel is directed horizontally to the right")
            print("and does not fit on the grid with this starting column.")
            valid = False
        elif (direction == 'v' and row + size > grid.GRID_HEIGHT) :
            print("Invalid row.  The vessel is directed vertically downwards")
            print("and does not fit on the grid with this starting row.")
            valid = False
        elif (defend_grid.has_overlap(vessel_index, row, column, direction)) :
         # The vessel fits, but it overlaps with another vessel on the grid.
            print("There is a vessel on the grid there already!")
            defend_grid.print_grid()
            valid = False

    # We've done all the tests.  If none of them failed, valid is still True.          
    return valid

# Needs to be broken into two functions and also check for overlap
def get_location(vessel_index) :
    name = grid.VESSEL_NAMES[vessel_index]
    size = grid.VESSEL_SIZES[vessel_index]

    print("Enter placement of your", name, "(", size,  "spaces)")
    column = input("Left column (A-J): ")
    row = int(input("Top row (1-10): "))
    direction = input("Direction (h)orizontal or (v)ertical: ")

    column = ord(column) - ord('A')
    row = row - 1

    if (not valid_location(vessel_index, row, column, direction) ):
        get_location(vessel_index)
    else :
        defend_grid.add_vessel(vessel_index, row, column, direction)
