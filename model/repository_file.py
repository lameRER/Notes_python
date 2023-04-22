import datetime

from model.ifile_operation import IFileOperation
from model.irepository import IRepository
from model.note import Note


class RepositoryFile(IRepository):
    def __init__(self, file_operation: IFileOperation):
        self.file_operation = file_operation

    def read_notes(self):
        notes = []
        for i in self.file_operation.read_all_lines():
            notes.append(Note(i['name'], i['text'], i['create_datetime'], i['modify_datetime'], i['id']))
        return notes

    def save_notes(self, notes):
        self.file_operation.save_all_lines(notes)

    def create_note(self, name, text):
        notes = self.read_notes()
        notes.append(Note(name, text))
        self.save_notes(notes)

    def delete_note(self, _id):
        notes = self.read_notes()
        for i in notes:
            if _id == i.id:
                notes.remove(i)
        self.save_notes(notes)

    def edit_note(self, _id, text):
        notes = self.read_notes()
        for i in notes:
            if _id == i.id:
                i.text = text
                i.modify_datetime = datetime.datetime.now().isoformat()
        self.save_notes(notes)

    def read_note(self, _id):
        for i in self.read_notes():
            if _id == i.id:
                return i
        return None
