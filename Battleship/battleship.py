###### Exercise Set 7 - Solution ################

import human
import t00_0_ai
import grid

def info() :
    print("Welcome to the battleship game.")
    print("This iteration has a class for the grid.")
    print()

def has_winner() :
    return t00_0_ai.defend_grid.all_vessels_sunk() or \
        human.defend_grid.all_vessels_sunk()
    return False

def announce_winner() :
    if (t00_0_ai.defend_grid.all_vessels_sunk()) :
        print("You won! Congratulations")
    else :
        print("You lost.  Better luck next time.")
            

def main() :
    for index in range(0, grid.NUM_OF_VESSELS) :
        human.get_location(index)
        t00_0_ai.get_location(index)

#    t00_0_ai.attack_grid.drop_test_bombs()
#    human.attack_grid.drop_test_bombs()

    while (not has_winner()) :
        # user's turn
        row, column = human.get_choice()
        if (t00_0_ai.defend_grid.is_hit(row, column)) :
            print("HIT!!")
        else :
            print("You missed.")
        t00_0_ai.defend_grid.drop_bomb(human.attack_grid, row, column)
        print()

        #ai's turn
        row, column = t00_0_ai.get_choice()
        if (human.defend_grid.is_hit(row, column)) :
            print("You've been hit.")
        else :
            print("I missed.")
        human.defend_grid.drop_bomb(t00_0_ai.attack_grid, row, column)
        human.defend_grid.print_grid()

    announce_winner()

main()
