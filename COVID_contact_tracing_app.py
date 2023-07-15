#Kate Eurisse L. Martinez_BSCPE 1-5_COVID Contact Tracing App

# Program General Instruction
#Create “your” own covid contact tracing app with GUI
#Create a program that ask user for typical information found in covid contact tracing app
#Write the collected information in a file (use any format you like)
#The app should be able to add and search entry
#Be creative, the realistic the better.



#Import tkinter (GUI)
import tkinter as tk

#Import Modules(classes)
from file_handling import FileHandling

#Initialize class
fh = FileHandling()

#Create Window
main = tk.Tk() #Creating the application main window
main.title("COVID Contact Tracing APP") #Main window title
main.geometry("900x700") #Main window Size

#Add Widgets
#Ask user for certain information (Possible ones to be used)
#Labels
label_name = tk.Label(main, text ="Name: ") #For the user's name
label_name.grid(row = 1, column = 0, padx = 5, pady = 5)
label_age = tk.Label(main, text ="Age: ") #For the user's age
label_age.grid(row = 2, column = 0, padx = 5, pady = 5)
label_address = tk.Label(main, text ="Address: ") #For the user's address
label_address.grid(row = 3, column = 0, padx = 5, pady = 5)
label_number = tk.Label(main, text ="Phone number: ") #For the user's phone number
label_number.grid(row = 4, column = 0, padx = 5, pady = 5)
#Entries/ Input Fields
input_name = tk.Entry(main)		#For the user's name
input_name.grid(row = 1, column = 1, padx = 5, pady = 5)
input_age = tk.Entry(main)		#For the user's age
input_age.grid(row = 2, column = 1, padx = 5, pady = 5)	
input_address = tk.Entry(main)		#For the user's address
input_address.grid(row = 3, column = 1, padx = 5, pady = 5)	
input_number = tk.Entry(main)		#For the user's number
input_number.grid(row = 4, column = 1, padx = 5, pady = 5)			
#Buttons
button_submit = tk.Button(main, text="Submit", command = fh.save_inputs)
button_submit.grid(row=5, column=1, padx=10, pady=10) 
		#Text
		#Radiobutton
#Get the input of the user user
fh.save_inputs()
#Write or store the data gathered from the user in a text file
	#Let user search for info and display it

#Call the main event loop
main.mainloop()