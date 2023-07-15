#Codes for file handling will be on this python file

#Create class
class FileHandling:
#Create object of class
    def save_inputs(self, name, age, address, number):
        #Getting the name input
        self.name = name
        #Getting the age input
        self.age = age
        #Getting the address input
        self.address = age
        #Getting the phone number input
        self.number = number
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