import os.path
import tempfile
import uuid

class File:

    def __init__(self,path_to_file):
        self.path_to_file = path_to_file
        self.cur = 0
        try:
            if not os.path.exists(path_to_file):
                raise ValueError
        except ValueError:
            with open(self.path_to_file, 'w') as f:
                pass
                
    def read (self):
        with open(self.path_to_file, 'r', encoding='utf8') as f:
            return f.read()

    def write (self, new_data):
        with open (self.path_to_file, 'w', encoding='utf8') as f:
            f.write(new_data)

    def __add__(self,obj):
        new_filename = str(uuid.uuid4())+'.txt'
        new_path = os.path.join(tempfile.gettempdir(), new_filename)
        result_file = File(new_path)
        result_file.write(self.read() + obj.read())
        return result_file

    def __str__(self):
        return self.path_to_file

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path_to_file, 'r', encoding='utf8') as f:
            f.seek(self.cur)
            cur_line = f.readline()
            if cur_line:
                self.cur = f.tell()
                return cur_line
            else:
                self.cur = 0
                raise StopIteration

if __name__ == '__main__':
    pass
