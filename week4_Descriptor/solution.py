class Value:
    def __init__(self):
        self.amount = None

    def __get__(self,obj,objtype):
        return self.amount

    def __set__(self, obj, amount):
        self.amount = amount *(1-obj.commission)
        return self.amount

class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission

if __name__ == '__main__':
    pass

# test case
# new_account = Account(0.1)
# new_account.amount = 100
# print(new_account.amount)
# Output>> 90