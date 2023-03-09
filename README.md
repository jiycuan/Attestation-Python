Необходимо написать проект, содержащий функционал работы с заметками. 
Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку, удалять заметку.


    while count < len(temp_collection):
        with open('Notes.csv', 'w') as refresh_file:
            writer = csv.writer(refresh_file, delimiter=",", lineterminator="\r")
            writer.writerows(temp_collection[count, 0], temp_collection[count, 1], temp_collection[count, 2], temp_collection[count, 3])
            count = count + 1


    def writeToFile(self):
        if (len(self.notes) > 0):
            with open(self.path, 'w') as data:
                writer = csv.writer(data, delimiter=";", lineterminator="\r")
                for x in self.notes:
                    writer.writerow([x.id_note, x.title, x.body, x.date_create])
            Printer(TxtInterface().notes_saved).prints()
        else:
            Printer(TxtInterface().notes_empty).prints()

