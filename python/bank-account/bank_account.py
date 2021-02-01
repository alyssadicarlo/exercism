import threading
import time

STATUS_OPEN = 'open'
STATUS_CLOSED = 'closed'

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.status = STATUS_CLOSED

    def get_balance(self):
        if self.status == STATUS_OPEN:
            return self.balance
        else:
            raise ValueError("Account is closed")

    def open(self):
        if self.status == STATUS_CLOSED:
            self.status = STATUS_OPEN
            print("Account opened")
        else:
            raise ValueError("Account already open")

    def deposit(self, amount):
        def deposit_thread(amount):
            self.balance += amount
        if self.status == STATUS_OPEN:
            if amount < 0:
                raise ValueError("Cannot deposit a negative amount")
            thread = threading.Thread(target=deposit_thread, args=[amount,])
            thread.start()
            #time.sleep(1e-12)
            thread.join()
        else:
            raise ValueError("Account is closed")

    def withdraw(self, amount):
        def withdraw_thread(amount):
            self.balance -= amount
        if self.status == STATUS_OPEN:
            if amount < 0:
                raise ValueError("Cannot withdraw a negative amount")
            if self.balance - amount < 0:
                raise ValueError(f"Not enough money in your account to withdraw ${amount}")

            thread = threading.Thread(target=withdraw_thread, args=[amount,])
            thread.start()
            #time.sleep(1e-12)
            thread.join()
        else:
            raise ValueError("Account is closed")

    def close(self):
        if self.status == STATUS_OPEN:
            self.status = STATUS_CLOSED
            self.balance = 0
        else:
            raise ValueError("Account already closed")