#This python file will serve as the data handling file

#Import modules
import csv
import tkinter as tk
from tkinter import messagebox
from form_user_interface import UserInterface

#Create class
class FileHandling(UserInterface):  
    # Open csv file and append data
    def storage_file(self, csv_file, data):
        with open(csv_file, mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([data])
    
    #Saving submitted data
    def submit_data(self):
        # Retrieve user input data
        self.last_name = self.input_last_name.get()
        self.first_name = self.input_first_name.get()
        self.middle_name = self.input_middle_name.get()
        self.age = self.age_spinbox.get()
        self.gender = self.gender_combobox.get()
        self.street_address = self.input_street_address.get()
        self.city_address = self.input_city_address.get()
        self.state_address = self.input_state_address.get()
        self.country_address = self.input_country_address.get()
        self.postal_code = self.input_postal_code.get()
        self.phone_number = self.input_phone_number.get()
        self.email = self.input_email.get()
        self.contact_person = self.input_contact_person.get()
        self.contperson_num = self.input_contperson_num.get()
        self.contperson_rel = self.input_contperson_rel.get()
        self.contperson_email = self.input_contperson_email.get()
        
        # Retrieve health-related question inputs
        self.vaccine_status = self.var.get()
        self.symptoms = [option.get() for option in self.check_symptom]
        self.non_empty_symptoms = [symptom for symptom in self.symptoms if symptom.strip()]
        self.symptoms_str = ", ".join(self.non_empty_symptoms)
        self.exposure = self.ex_var.get()
        self.contact = self.contact_var.get()
        self.test = self.test_var.get()
        
        # Create a list with the user input data
        # Create a single string with the user input data
        data_to_add = [
            f"Name: {self.last_name}, {self.first_name}, {self.middle_name}",
            f"Age: {self.age}",
            f"Gender: {self.gender}",
            f"Address: {self.street_address}, {self.city_address}, {self.state_address}, {self.country_address}",
            f"Postal code: {self.postal_code}",
            f"Phone Number: {self.phone_number}",
            f"Email: {self.email}",
            f"Contact Person: {self.contact_person}",
            f"Phone Number: {self.contperson_num}",
            f"Relationship: {self.contperson_rel}",
            f"Email: {self.contperson_email}",
            f"Vaccination Status: {self.vaccine_status}",
            f"Symptoms: {self.symptoms_str}",
            f"Exposed to a probable case: {self.exposure}",
            f"Has Contact (to a probable case): {self.contact}",
            f"Tested for COVID: {self.test}"
        ]
        
        #File path
        csv_file = 'data_file.csv'

        # Call the function to add data to the CSV file
        self.storage_file(csv_file, '\n'.join(data_to_add)) 
    
    # Search function using the search_csv function
    def search_data(self):
        # Get the search term from the Entry widget
        search_term = self.search_entry_widget.get()

        # Replace 'file.csv' with the path to your CSV file
        csv_file = 'data_file.csv'

        # Call the search_csv function to find matching rows
        found_rows = self.search_csv(csv_file, search_term)

        if found_rows:
            # Display the matching rows in the search_results_listbox
            self.search_results_listbox.delete(0, tk.END)  # Clear the listbox
            for row in found_rows:
                self.search_results_listbox.insert(tk.END, ', '.join(row))
        else:
            # Display a message if no matching rows are found
            messagebox.showinfo("Search Results", "No matching rows found.")

    # Search function using the search_csv function
    def search_csv(self, csv_file, search_term):
        found_rows = []
        with open(csv_file, mode='r') as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)  # Read the header row to get column names

            for row in reader:
                # Perform the search on the desired column (e.g., assuming the column index is 0 for the last name)
                if search_term.lower() in row[0].lower():
                    found_rows.append(row)

        return found_rows

    