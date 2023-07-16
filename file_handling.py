#Codes for file handling will be on this python file

#Create class
class FileHandling:
#Create object of class
    def save_inputs(self, name, age, address, number, vaccination_status, get_symptoms):
        #Getting the name input
        self.name = name
        #Getting the age input
        self.age = age
        #Getting the address input
        self.address = address
        #Getting the phone number input
        self.number = number
        #Getting the vaccination status
        self.vaccination_status = vaccination_status
        #Getting user's possible symptoms
        self.symptoms = get_symptoms
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
            #Appending Vaccination status
            data_file.write(f"Vaccination Status: {self.vaccination_status}\n") 
            #Appending Symptoms data
            non_empty_symptoms = [symptom for symptom in self.symptoms if symptom.strip()]
            symptoms_str = ", ".join(non_empty_symptoms)
            data_file.write(f"Symptoms: {symptoms_str}\n")