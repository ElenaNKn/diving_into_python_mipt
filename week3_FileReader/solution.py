import sys
import os.path

class FileReader:
    # adding parameter file_path to __init__ 
    def __init__(self,file_path):
        self.path = file_path

    def read(self):
        # exception handling
        try:
            #if file don't exist, function return ""
            if not os.path.exists(self.path):
                raise FileNotFoundError
            # otherwise, function returns file content
            else:
                f = open(self.path,'r')
                return f.read()
        except FileNotFoundError:
            return ''

# main function. Creation of class instance and execution of function read()
def main(file_path):
    output = FileReader(file_path)
    output.read()

# module will be exicuted from comand line with argument - path to file
if __name__ == '__main__':
    file_path = sys.argv[1]
    main(file_path)