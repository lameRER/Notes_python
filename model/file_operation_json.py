import os
import json

from model.ifile_operation import IFileOperation
from model.note import Note


class FileOperationJson(IFileOperation):
    def __init__(self, file_name):
        self.file_name = file_name
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as f:
                f.write('')

    def read_all_lines(self) -> list[str]:
        try:
            return json.loads(open(self.file_name).read())
        except:
            return []

    def save_all_lines(self, lines):
        with open(self.file_name, 'w') as f:
            f.write(json.dumps([obj.__dict__ for obj in lines]))
