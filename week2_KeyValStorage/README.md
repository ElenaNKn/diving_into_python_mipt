This folder contains solution of the next problem:

it's nessesary to create a key-value storage. Data should be stored in a file storage.data. A script storage.py is used to add new data to the file and to obtain current values from the file. This script can be executed with the next arguments:
--key <key name>, where <key name> is a key by means of which values can be obtained
--val <value>, where <value> is stored value.
If both arguments are entered, then the script appends the value to the storage using the key. If only --key is entered, then the script reads the storage file and prints values for this key.
Notice that if the key is already in storage, then athe new value don't overwrite values, which are in storage. The new value is appended to existing values.
If there are no values for the --key argument while reading data from the storage, script should print an empty string or None.

В этой папке находится решение следующей задачи:

Необходимо реализовать key-values хранилище. Данные будут сохраняться в файле storage.data. Добавление новых данных в хранилище и получение текущих значений осуществляется с помощью утилиты командной строки storage.py. Утилита может вызваться со следующими параметрами:
--key <имя ключа> , где <имя ключа> - ключ по которому сохраняются/получаются значения
--val <значение>, где <значение> - сохраняемое значение.

Если при запуске утилиты переданы оба параметра, происходит добавление переданного значения по ключу и сохранение данных в файле. Если передано только имя ключа, происходит чтение файла хранилища и вывод на печать значений, которые были сохранены по данному ключу.
Обратите внимание, что значения по одному ключу не перезаписываются, а добавляются к уже сохраненным.
Если значений по ключу не было найдено, выведите пустую строку или None.