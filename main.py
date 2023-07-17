#This will serve as the main file of the program in which the methods will be called


#Import class
from user_interface import UserInterface

#Initialize class
ui = UserInterface()

#First window
ui.first_window()
ui.introduction()
#Running first window mainloop
ui.first.mainloop()
#Second Window
ui.second_window()
#Running Second window mainloop
ui.second.mainloop()
#Third window
ui.third_window()
#Running third window mainloop
ui.third.mainloop() 

#Calling the method for Pesonal info data
#ui.personal_info()
#Calling the method for Health Declaration data
#ui.health_info()

#Submit button for saving inputs
#ui.submit_button()