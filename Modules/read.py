import csv

def read_notes():
    with open("Notes.csv", 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def read_choose_notes(id_for_search):
    with open("Notes.csv", 'r') as file:
        reader = csv.reader(file)
        count = 1
        for row in reader:
            if count == id_for_search:
                print(row)
            count = count+1


