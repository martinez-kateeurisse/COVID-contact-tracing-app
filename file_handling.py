#Codes for file handling will be on this python file

#Create class
class FileHandling:
#Create object of class
    def save_inputs(self):
        #Getting the name input
        self.name = self.input_name.get()
        #Getting the age input
        self.age = self.input_age.get()
        #Getting the address input
        self.address = self.input_address.get()
        #Getting the phone number input
        self.number = self.input_number.get()
    #Write or store the data gathered from the user in a text file
    def storage_file(self):
        #Opening a txt file
        with open("user_inputs.txt", "a") as data_file:
            #Appending the name info
            data_file.write(f"Name: {self.name}\n") 
            #Appending the age info
            data_file.write(f"Age: {self.age}\n")
            #Appending the address info
            data_file.write(f"Address: {self.address}\n")
            #Appending the phone number info
            data_file.write(f"Phone number: {self.number}\n") 