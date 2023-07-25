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
        terms_accepted = self.accept_terms.get()
        # Check if terms have been accepted
        if terms_accepted=="Terms Accepted":
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
            
            # Create a list to store the user input data
            data_to_add = []

            # Name section
            name_str = f"\nName: {self.last_name}"
            if self.first_name:
                name_str += f", {self.first_name}"
            if self.middle_name:
                name_str += f", {self.middle_name}"
            data_to_add.append(name_str)

            # Age, Gender, and other fields
            data_to_add.append(f"Age: {self.age}")
            data_to_add.append(f"Gender: {self.gender}")

            # Address section
            address_str = f"Address:"
            if self.street_address:
                address_str += f" {self.street_address}"
            if self.city_address:
                address_str += f", {self.city_address}"
            if self.state_address:
                address_str += f", {self.state_address}"
            if self.country_address:
                address_str += f", {self.country_address}"
            data_to_add.append(address_str)

            # Postal code, Phone Number, and other fields
            data_to_add.append(f"Postal code: {self.postal_code}")
            data_to_add.append(f"Phone Number: {self.phone_number}")
            data_to_add.append(f"Email: {self.email}")
            data_to_add.append(f"Contact Person: {self.contact_person}")
            data_to_add.append(f"Phone Number: {self.contperson_num}")
            data_to_add.append(f"Relationship: {self.contperson_rel}")
            data_to_add.append(f"Email: {self.contperson_email}")
            data_to_add.append(f"Vaccination Status: {self.vaccine_status}")
            data_to_add.append(f"Symptoms: {self.symptoms_str}")
            data_to_add.append(f"Exposed to a probable case: {self.exposure}")
            data_to_add.append(f"Has Contact (to a probable case): {self.contact}")
            data_to_add.append(f"Tested for COVID: {self.test}")


            # Join the data into a single string with line breaks
            data_to_add_str = '\n'.join(data_to_add)

            #Csv file path
            csv_file = 'data_file.csv'

            # Call the function to add data to the CSV file
            self.storage_file(csv_file, data_to_add_str)

            #opening last window
            self.open_last_window()
        
        #If terms and condition is not checked, message box will pop up
        else:
            messagebox.showwarning(title="Accepting Terms and Condition", message = "This Contact Tracing Form requires you to accept the terms and Condition inorder to submit. Make sure to read it by pressing the button beside the checkbutton. Thank you!")
    
    # Search function using the search_csv function
    def search_data(self):
        # Get the search term from the Entry widget
        search_term = self.search_entry_widget.get()

        # CSV file path
        csv_file = 'data_file.csv'

        # Call the search_csv function to find matching rows
        found_rows = self.search_csv(csv_file, search_term)

        if found_rows:
            # Display the matching rows in the search_results_listbox
            self.search_results_listbox.delete(0, tk.END)  # Clear the listbox
            for row in found_rows:
                # Split the row_str by newline character to handle multiline text
                row_str = row[0].split('\n')
                # Insert each line as a separate item in the listbox
                for line in row_str:
                    self.search_results_listbox.insert(tk.END, line)
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
