from datetime import datetime
import csv

def delete_notes(new_notes):
    temp_collection = []
    with open("Notes.csv", 'r') as file:
        reader = csv.reader(file)
        count = 1
        for row in reader:
            if count != new_notes.id_notes:
                temp_collection.append(row)
            count = count + 1

    refresh_file = open('Notes.csv', 'w')
    with refresh_file:
        writer = csv.writer(refresh_file, lineterminator="\r")
        writer.writerows(temp_collection)