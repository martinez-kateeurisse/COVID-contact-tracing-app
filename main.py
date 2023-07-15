#This will serve as the main file of the program in which the methods will be called


#Import class
from tk_methods import TkMethods

#Initialize class
gui = TkMethods()

#Calling the method for the name data
gui.name()

#Running the mainloop
gui.main.mainloop()