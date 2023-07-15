#This will serve as the main file of the program in which the methods will be called


#Import class
from tk_methods import TkMethods

#Initialize class
gui = TkMethods()

#Calling the method for the name's data
gui.name()
#Calling the method for the age's data
gui.age()
#Calling the method for the address' data
gui.address()
#Calling the method for the number's data
gui.number()
#Running the mainloop
gui.main.mainloop()