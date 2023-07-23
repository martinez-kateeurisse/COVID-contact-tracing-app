#This python file will serve as the data handling file

#Import modules
import csv

#Create class
class FileHandling:
    #Open csv file and append data
    def add_data_to_csv(file_path, data):
        with open(file_path, mode='a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data)

