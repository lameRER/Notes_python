import datetime

class Note:
    count = 0

    def __init__(self, name: str, text: str, create_date = datetime.datetime.now().isoformat(), modify_date = datetime.datetime.now().isoformat(), id = 0):

        if id == 0:
            Note.count += 1
            self.id = Note.count
        else:
            self.id = id
            Note.count = id
        self.create_datetime = create_date
        self.modify_datetime = modify_date
        self.name = name
        self.text = text

    def __str__(self):
        return f'Note: {self.id} create_datetime: {self.create_datetime}, modify_datetime: {self.modify_datetime}, name: {self.name}, text: {self.text}'
