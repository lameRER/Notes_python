from model.irepository import IRepository


class NotesController:
    def __init__(self, repository: IRepository):
        self.__repository = repository

    def add(self, name, text):
        self.__repository.create_note(name, text)

    def read(self, _id):
        return self.__repository.read_note(_id)

    def read_all(self):
        return self.__repository.read_notes()

    def delete(self, _id):
        self.__repository.delete_note(_id)

    def edit(self, _id, text):
        self.__repository.edit_note(_id, text)
