import csv
from datetime import datetime


def edit_notes(new_notes):
    new_notes.header = input("Укажите новый заголовок заметки: ")
    new_notes.body = input("Укажите новое тело заметки: ")
    new_notes.current_datetime = datetime.now()
    data_for_file = [new_notes.id_notes, new_notes.current_datetime, new_notes.header, new_notes.body]
    temp_collection = []
    with open("Notes.csv", 'r') as file:
        reader = csv.reader(file)
        count = 1
        for row in reader:
            if count != new_notes.id_notes:
                temp_collection.append(row)
            else:
                temp_collection.append(data_for_file)
            count = count + 1

    refresh_file = open('Notes.csv', 'w')

    with refresh_file:
        writer = csv.writer(refresh_file, lineterminator="\r")
        writer.writerows(temp_collection)
