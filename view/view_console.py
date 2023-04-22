import os

from model.commands import Commands
from controller.user_controller import NotesController


class ViewConsole:
    def __init__(self, controller: NotesController):
        self.controller = controller

    def run(self):
        while True:
            com = input("Введите команду: ").upper()
            match com:
                case Commands.ADD.value:
                    self.add_note()
                case Commands.READ.value:
                    self.read_node()
                case Commands.DELETE.value:
                    self.delete_note()
                case Commands.EDIT.value:
                    self.edit_note()
                case Commands.READALL.value:
                    self.read_notes()
                case Commands.EXIT.value:
                    exit()

    def add_note(self):
        name = input('Название заметки: ')
        text = input('Описание заметки: ')
        self.controller.add(name, text)

    def read_node(self):
        _id = self.read_id()
        note = self.controller.read(_id)
        if note is not None:
            print(note)
        else:
            print(f'Заметка с id {_id} не найдена ')

    def delete_note(self):
        _id = self.read_id()
        self.controller.delete(_id)

    def read_id(self):
        _id = input('Удажите id заметки: ')
        try:
            return int(_id)
        except ValueError as e:
            print(e)

    def edit_note(self):
        _id = self.read_id()
        note = self.controller.read(_id)
        if note is not None:
            text = input('Введите описание заметки: ')
            self.controller.edit(note.id, text)
        else:
            print(f'Заметка с id {_id} не найдена ')

    def read_notes(self):
        [print(i) for i in self.controller.read_all()]
