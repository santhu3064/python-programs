import datetime
import pytz


class Accounts:

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self.__balance = balance
        self._transaction_list= []

        if  self.__balance > 0:
            self._transaction_list.append((Accounts._current_time(), +self.__balance))
            print("Account created for {} with opening balance of {} ".format(self._name, self.__balance))
        elif self.__balance == 0  :
            print("Account created for {} with opening balance of {} ".format(self._name, self.__balance))
        else:
            print ("Account cannot be openend with negative balance")
            exit()



    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_list.append((Accounts._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self._transaction_list.append((Accounts._current_time(), -amount))
        else:
            print("The amount must be greater than zero and less than your current account balance")
            self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.__balance))

    def show_transaction(self):
        for date,amount in self._transaction_list:
            if amount > 0:
                tran_type = "deposit"
            else:
                tran_type = "Withdrawn"
                amount *= -1
            print ( "{:6} {} on (local time is  {})".format(amount,tran_type,date,date.astimezone()))


if __name__ == "__main__":
    # san = Accounts("santhosh",0)
    # san.show_balance()
    # san.deposit(1000)
    # san.show_balance()
    # san.withdraw(500)
    # san.show_balance()
    # san.withdraw(5555)
    # san.show_transaction()


    can = Accounts("canty",1000)
    can.__balance=200
    can.deposit(1000)
    can.withdraw(500)
    can.show_balance()
    #can.withdraw(5555)
    can.show_transaction()
    print(can.__dict__)

