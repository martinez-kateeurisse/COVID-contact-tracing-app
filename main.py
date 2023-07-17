#This will serve as the main file of the program in which the methods will be called


#Import class
from user_interface import UserInterface

#Initialize class
ui = UserInterface()

#Calling the main window method
ui.first_window()

#Calling the method for Pesonal info data
ui.personal_info()
#Calling the method for Health Declaration data
ui.health_info()

#Submit button for saving inputs
ui.submit_button()

#Running the mainloop
ui.main.mainloop()