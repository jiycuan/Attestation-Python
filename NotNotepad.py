from datetime import datetime

from Modules.add import add_notes
from Modules.delete import delete_notes
from Modules.edit import edit_notes
from Modules.read import read_notes, read_choose_notes
import os.path
import csv


class Notes:
    current_datetime = datetime.now()
    id_notes = int
    header = str
    body = str

4
def ui():
    new_notes = Notes()
    if os.path.exists("Notes.csv"):
        new_notes.id_notes = sum(1 for line in open('Notes.csv', 'r'))+1
    else:
        new_notes.id_notes = 1
    operation_choose = int(input("Выберите тип операции. "
                                 "1 - добавить заметку. "
                                 "2 - прочитать все заметки. "
                                 "3 - прочитать выбранную заметку. "
                                 "4 - редактировать заметку. "
                                 "5 - удалить заметку. "
                                 "6 - завершить работу. "))
    if operation_choose == 1:
        add_notes(new_notes)
        ui()

    if operation_choose == 2:
        read_notes()
        ui()

    if operation_choose == 3:
        id_for_search = int(input("Укажите идентификатор заметки: "))
        read_choose_notes(id_for_search)
        ui()

    if operation_choose == 4:
        new_notes.id_notes = int(input("Укажите идентификатор заметки: "))
        edit_notes(new_notes)
        ui()

    if operation_choose == 5:
        new_notes.id_notes = int(input("Укажите идентификатор заметки: "))
        delete_notes(new_notes)
        ui()

    if operation_choose == 6:
        print("Надеюсь, это был не самый ужасный опыт в твоей жизни")

ui()
