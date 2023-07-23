#This python file will serve as the data handling file

#Import modules
import csv
from form_user_interface import UserInterface

#Create class
class FileHandling(UserInterface):
    #Open csv file and append data
    def add_data_to_csv(self,file_path, data):
        with open(file_path, mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)
    
    #Saving submitted data
    def submit_data(self):
        # Retrieve user input data
        last_name = self.input_last_name.get()
        first_name = self.input_first_name.get()
        middle_name = self.input_middle_name.get()
        age = self.age_spinbox.get()
        gender = self.gender_combobox.get()
        street_address = self.input_street_address.get()
        city_address = self.input_city_address.get()
        state_address = self.input_state_address.get()
        country_address = self.input_country_address.get()
        postal_code = self.input_postal_code.get()
        phone_number = self.input_phone_number.get()
        email = self.input_email.get()
        contact_person = self.input_contact_person.get()
        contperson_num = self.input_contperson_num.get()
        contperson_rel = self.input_contperson_rel.get()
        contperson_email = self.input_contperson_email.get()

        # Create a list with the user input data
        data_to_add = [last_name, first_name, middle_name, age, gender,
                       street_address, city_address, state_address, country_address, postal_code,
                       phone_number, email, contact_person, contperson_num, contperson_rel, contperson_email]

        # Replace 'file.csv' with the path to your CSV file
        csv_file_path = 'data_file.csv'

        # Call the function to add data to the CSV file
        self.add_data_to_csv(csv_file_path, data_to_add)


