from controller.user_controller import NotesController
from model.file_operation_json import FileOperationJson
from model.repository_file import RepositoryFile
from view.view_console import ViewConsole


def main():
    file_operation = FileOperationJson('notes.json')
    repository = RepositoryFile(file_operation)
    controller = NotesController(repository)
    ViewConsole(controller).run()


if __name__ == '__main__':
    main()