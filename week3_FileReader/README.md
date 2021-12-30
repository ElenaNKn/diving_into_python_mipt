This folder contains solution of the next problem:

It's nessesary to create a python-module, containing a class FileReader. This class receives one parameter: a path to file at a disk. Method read() should be realized in the class FileReader. This method should return a content of a file (the path to the file is entered as an attribute of an instance of the class FileReader). Import of the class FileReader should not cause errors.

The class should handle the case of a missing file: if there is no any file with the entered path then read() should return an empty string.


В этой папке находится решение следующей задачи:

Необходимо написать python-модуль solution.py, внутрь которого необходимо поместить код класса FileReader. Конструктор этого класса принимает один параметр: путь до файла на диске. В классе FileReader должен быть реализован метод read, возвращающий строку - содержимое файла, путь к которому был указан при создании экземпляра класса. Python модуль должен быть написан таким образом, чтобы импорт класса FileReader из него не вызвал ошибок.

При написании реализации метода read, вам нужно учитывать случай, когда при инициализации был передан путь к несуществующему файлу. Требуется обработать возникающее при этом исключение FileNotFoundError и вернуть из метода read пустую строку.