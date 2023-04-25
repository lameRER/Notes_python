import datetime
from model.irepository import IRepository
from model.note import Note


class NotesController:
    def __init__(self, repository: IRepository):
        self.__repository = repository

    def add(self, name, text):
        notes = self.read_all()
        notes.append(Note(name, text))
        self.__repository.save_notes(notes)

    def read(self, _id):
        notes = self.read_all()
        for i in notes:
            if i.id == _id:
                return i

    def read_all(self):
        return self.__repository.get_all_notes()

    def delete(self, _id):
        notes = self.read_all()
        for i in notes:
            if _id == i.id:
                notes.remove(i)
        self.__repository.save_notes(notes)

    def edit(self, _id, text):
        notes = self.read_all()
        for i in notes:
            if _id == i.id:
                i.text = text
                i.modify_datetime = datetime.datetime.now().isoformat()
        self.__repository.save_notes(notes)
