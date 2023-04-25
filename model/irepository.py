from model.note import Note


class IRepository:
    def get_all_notes(self) -> list[Note]:
        return []

    def save_notes(self, notes: list[Note]):
        pass
