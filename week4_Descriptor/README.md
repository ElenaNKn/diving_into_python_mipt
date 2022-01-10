This folder contains solution of the next problem:

We are often taken comission when we credit money to an account. It's nessesary to create a descriptor Value for a class Acount.
class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission

This descriptor should provide a calculation of an amount atribute with a comission, which is the atribute of class Account. 


В этой папке находится решение следующей задачи:

Часто при зачислении каких-то средств на счет с нас берут комиссию. Давайте реализуем похожий механизм с помощью дескрипторов. Напишите дескриптор Value, который будет использоваться в нашем классе Account.
class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission

У аккаунта будет атрибут commission. Именно эту коммиссию и нужно вычитать при присваивании значений в amount.