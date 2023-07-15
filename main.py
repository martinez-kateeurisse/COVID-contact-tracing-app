#This will serve as the main file of the program in which the methods will be called


#Import class
from user_interface import UserInterface

#Initialize class
ui = UserInterface()

#Calling the main window method
ui.main_window()
#Calling the method for the name's data
ui.name()
#Calling the method for the age's data
ui.age()
#Calling the method for the address' data
ui.address()
#Calling the method for the number's data
ui.number()

#Submit button for saving inputs
ui.submit_button()

#Running the mainloop
ui.main.mainloop()