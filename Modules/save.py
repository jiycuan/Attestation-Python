import os
import pandas as pd
from datetime import datetime


def save_notes(new_notes):
    data_frame = pd.DataFrame({'ID': [new_notes.id_notes],
                               'Date_time': [new_notes.current_datetime],
                               'Header': [new_notes.header],
                               'Body': [new_notes.body]})
    data_frame.to_csv('Notes.csv', mode='a', index=False, header=False)