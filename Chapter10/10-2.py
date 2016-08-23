class FileManager():
    def __init__(self, filename, encoding="utf-8"):
        self.filename = filename
        self.encoding = encoding
        self.file = None
    def __enter__(self):
        self.file = open(self.filename, encoding=self.encoding)
        return self.file

    def __exit__(self, type, value, tb):
        if self.file:
            self.file.close()

if __name__ == "__main__":
    with FileManager("10-2.py") as file:
        print(file.readlines())
