from model.ifile_operation import IFileOperation
from model.irepository import IRepository
from model.note import Note


class RepositoryFile(IRepository):
    def __init__(self, file_operation: IFileOperation):
        self.file_operation = file_operation

    def get_all_notes(self) -> list[Note]:
        notes = []
        for i in self.file_operation.read_all_lines():
            notes.append(Note(i['name'], i['text'], i['create_datetime'], i['modify_datetime'], i['id']))
        return notes

    def save_notes(self, notes):
        self.file_operation.save_all_lines(notes)
