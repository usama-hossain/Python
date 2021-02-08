# Notes

import datetime

# Store the next available id

last_id = 0


class Note:
    "Represent a note in a class. "

    def __init__(self, memo, tag=''):
        self.memo = memo
        self.tag = tag
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):

        return filter in self.memo or filter in self.tag


class Notebook:

    def __init__(self):
        self.notes = []

    def new_note(self, memo, tag=''):
        self.notes.append(Note(memo, tag))

    def modify_memo(self, note_id, memo):
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id, tag):
        for note in self.notes:
            if note.id == note_id:
                note.tag = tag
                break

    def search(self, filter):
        return [note for note in self.notes if note.match(filter)]
