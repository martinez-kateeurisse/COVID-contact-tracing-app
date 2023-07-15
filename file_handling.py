#Codes for file handling will be on this python file

#Create class
class FileHandling:
#Create object of class
    def save_inputs(self):
        self.name = self.input_name.get()
        self.age = self.input_age.get()
        self.address = self.input_address.get()
        self.phone_number = self.input_number.get()
    #Write or store the data gathered from the user in a text file