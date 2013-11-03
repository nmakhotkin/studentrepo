import os

from student import settings
from student.utils.file_retriever import base


LOCAL_FILE_DIR = "/files/"
REPLACEMENT_SYMBOL = ":"


class LocalFileRetriever(base.BaseFileRetriever):
    def __init__(self):
        project_path = settings.PROJECT_PATH
        self.files_path = project_path + LOCAL_FILE_DIR

    def get_file(self, key):
        full_file_path = self.files_path + str(key).replace(
            REPLACEMENT_SYMBOL, os.sep)
        if os.path.isfile(full_file_path):
            return open(full_file_path).read()
        else:
            raise IOError("Error. It is not a file: " + full_file_path)

    def save_file(self, key, data, overwrite=True):
        full_file_path = self.files_path + str(key).replace(
            REPLACEMENT_SYMBOL, os.sep)
        if not os.path.exists(full_file_path) and not overwrite:
            raise IOError("Error. File " + full_file_path + "already exists")
        open(full_file_path, "w").write(data)


if __name__ == "__main__":
    content = LocalFileRetriever().get_file("test_dir:test_file.py")
    LocalFileRetriever().save_file("test_dir:test_save_file.py", content)