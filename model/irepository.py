from model.note import Note


class IRepository:
    def read_notes(self) -> list[Note]:
        return []

    def save_notes(self, notes: list[Note]):
        pass

    def create_note(self, name, text):
        pass

    def delete_note(self, _id):
        pass

    def edit_note(self, _id, text):
        pass

    def read_note(self, _id):
        pass
