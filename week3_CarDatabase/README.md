This folder contains a solution of the problem:
https://www.coursera.org/learn/diving-in-python/programming/bd6aI/klassy-i-nasliedovaniie

You are supposed to have data about different vehicles. All vehicles are divided into three groups: cars, trucks and special machines. Some parameters may be assigned to only certain group of vehicles (for example only cars have parameter "number of passengers").
It's necessary to create a class hierarchy for described data.
Next, it's necessary to define a function get_car_list. File *.csv is a parameter of this function. The file contains data about vehicles and their parameters (each line is an information about a specific vehicle and it's parameters). The function should read the file line by line using package csv. Then it should validate parameters from each line and create a list of class objects.


В этой папке находится решение задачи:
https://www.coursera.org/learn/diving-in-python/programming/bd6aI/klassy-i-nasliedovaniie

Предположим есть данные о разных автомобилях и спецтехнике. Вся техника разделена на три вида: спецтехника, легковые и грузовые автомобили. Некоторые характеристики присущи только определенному виду техники.
Необходимо создать свою иерархию классов для данных, которые описаны в таблице. Классы должны называться CarBase (базовый класс для всех типов машин), Car (легковые автомобили), Truck (грузовые автомобили) и SpecMachine (спецтехника). 
Далее необходимо реализовать функцию get_car_list, на вход которой подается имя файла в формате csv. Файл содержит данные, аналогичные строкам из таблицы. Необходимо прочитать этот файл построчно при помощи модуля стандартной библиотеки csv. Затем проанализировать строки на валидность и создать список объектов с автомобилями и специальной техникой. Функция должна возвращать список объектов.