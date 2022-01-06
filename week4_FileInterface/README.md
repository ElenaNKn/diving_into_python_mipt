This folder contains solution of the next problem:

An interface should be created to work with files. It should provide the next facilities:
- reading from a file. Read method should return a string with a curent file content
- writing to a file. An argument of a write method is a string with a new file content
- summation of class File objects. A result of this operation is a new object of class File. The new file should be created in a directory, that is to be obtained with a function tempfile.gettempdir. You may use os.path.join to determine a path to a new file. The content of a new file is a content of the first file followed by a content of the second file
- a string representation of a class File object is a string, which contains a path to the file
- iteration on class Fole object is to be performed by lines of a file

A complete path to file is an argument of a constructor of a class File object. If there is no file with such a path, this file is to be created while initialization.

В этой папке находится решение следующей задачи:

Нужно создать интерфейс для работы с файлами. Интерфейс должен предоставлять следующие возможности по работе с файлами:
- чтение из файла, метод read возвращает строку с текущим содержанием файла
- запись в файл, метод write принимает в качестве аргумента строку с новым содержанием файла
- сложение объектов типа File, результатом сложения является объект класса File, при этом создается новый файл и файловый объект, в котором содержимое второго файла добавляется к содержимому первого файла. Новый файл должен создаваться в директории, полученной с помощью функции tempfile.gettempdir. Для получения нового пути можно использовать os.path.join.
- возвращать в качестве строкового представления объекта класса File полный путь до файла
- поддерживать протокол итерации, причем итерация проходит по строкам файла

При создании экземпляра класса File в конструктор передается полный путь до файла на файловой системе. Если файла с таким путем не существует, он должен быть создан при инициализации.