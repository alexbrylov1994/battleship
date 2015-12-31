#Ex 8.3
import tkinter
import tkinter.messagebox
import grid
from grid import Grid
from grid import GRID_HEIGHT
from grid import GRID_WIDTH
import t00_0_ai

class BattleshipGUI :
	def __init__(self) :
		self.main_window = tkinter.Tk()
		
		self.label1 = tkinter.Label(self.main_window, text = "Attack Grid", font=('Helvetica',21))
		self.label2 = tkinter.Label(self.main_window, text = "Defend Grid", font=('Helvetica',21))
        ## You'll have to add the following two lines to the __init__ you created for exercise 1.
        
		self.next_vessel = grid.NUM_OF_VESSELS - 1
		self.attack_grid = Grid()
		self.defend_grid = Grid()		
		
		
		self.label2.grid()
		defend_frame = self.create_defend_grid()
		defend_frame.grid(row=2, column=0)
		
	
		self.label1.grid()
		attack_frame = self.create_attack_grid()
		attack_frame.grid(row=4, column=0)


		tkinter.mainloop()
    
    # This method creates a grid filled with buttons.
	def create_defend_grid(self) :
		frame = tkinter.Frame(self.main_window)
		buttons = []

		for row_index in range(0,GRID_HEIGHT) :
			row = []
			for column_index in range(0,GRID_WIDTH) :
				button = tkinter.Button(frame, \
										text = "  ", \
										command=lambda row=row_index, column=column_index: \
											self.defend_button_clicked(row,column))
				button.grid(row=row_index, column=column_index)
				row.append(button)
			buttons.append(row)

		self.defend_buttons = buttons
		return frame
        

    # Updated to insert vessels on the defend grid as the user
    # presses buttons.  Once all vessels are inserted the 
    # buttons on the defense grid are disabled.
    # This method serves the setup portion of the game.
    # (Provided method.)
	def defend_button_clicked(self,row,column) :
		direction = 'h'  ## for now, default to horizontal
		size = grid.VESSEL_SIZES[self.next_vessel]
        
        # Check to make sure the vessel fits where the user has clicked.
		if (direction == 'h' and column + size > GRID_WIDTH or \
			direction == 'v' and row + size > GRID_HEIGHT or \
			self.defend_grid.has_overlap(self.next_vessel,row,column, direction)) :
            # For now, will do nothing.  There really should be some sort of
            # error message.
			return

        # Add vessel both as indicated by user and let AI also insert.
		t00_0_ai.get_location(self.next_vessel)
		self.defend_grid.add_vessel(self.next_vessel, \
										row, \
										column, \
										direction)

        # Update GUI to reflect data in defend grid
		for row_index in range(0,GRID_HEIGHT) :
			for column_index in range(0,GRID_WIDTH) :
				if (not self.defend_grid.is_empty(row_index, column_index)) :
					button = self.defend_buttons[row_index][column_index]
					button['text'] = self.defend_grid.grid[row_index][column_index]

        # Setup for next vessel to add to grid.
		self.next_vessel = self.next_vessel - 1

        # All vessels are in the grid.  Disable the defense grid buttons.
		if (self.next_vessel < 0) :
			for row_index in range(0,GRID_HEIGHT) :
				for column_index in range(0,GRID_WIDTH) :
					button = self.defend_buttons[row_index][column_index]
					button['state'] = 'disabled'

	def create_attack_grid(self) :
		frame = tkinter.Frame(self.main_window)
        # Initialize a list that we'll also use to store the buttons.
		buttons = []

        # A nexted loop to create one button for each cell in the defend grid.
		for row_index in range(0,grid.GRID_HEIGHT) :
            # create an empty row.
			row = []
            # populate a single row
			for column_index in range(0,grid.GRID_WIDTH) :

				button = tkinter.Button(frame, \
										text = "  ", \
										command=lambda row=row_index, \
											column=column_index: \
											self.attack_button_clicked(row,column))

				button.grid(row=row_index, column=column_index)
   
				row.append(button)
   
			buttons.append(row)

		self.attack_buttons = buttons
		return frame

	def attack_button_clicked(self,row,column) :
		
		t00_0_ai.defend_grid.drop_bomb(self.attack_grid,row,column)			
		ai_row,ai_column = t00_0_ai.get_choice()
		
		self.defend_grid.drop_bomb(t00_0_ai.attack_grid,ai_row,ai_column)
		
		button_clicked = self.attack_buttons[row][column]				
		button_clicked['text'] = self.attack_grid.grid[row][column]		
		entered_location = ("Column:",str(column+1), "Row:" , str(row+1))
		
		tkinter.messagebox.showinfo("Attack Grid", \
									entered_location)

		self.win_state()											
		button_clicked['state'] = 'disabled'								

	def win_state(self):
		if t00_0_ai.defend_grid.all_vessels_sunk():	
			tkinter.messagebox.showinfo("Winner" , "You won the game!")

		
		elif self.defend_grid.all_vessels_sunk() :
			tkinter.messagebox.showinfo("You lost" , "Game is over, loser")
			
		else:
			return

my_gui = BattleshipGUI()