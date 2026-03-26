# walrus operator for concise code
numbers = [1, 2, 3, 4, 5]
if n:= len(numbers):
    print(numbers, n)
# next() for memory efficient looping
orders=[
    {"order_id": 1, "order_status": "not started"},
    {"order_id": 2, "order_status": "completed"},
    {"order_id": 3, "order_status": "in progress"},
    {"order_id": 4, "order_status": "completed"}
]
order=next((o for o in orders if o["order_status"]=="completed"), None) # generator expression ; returns first match
print(order)

#Concept of threading
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def threaded_function():
    for number in range(3):
        print(f"Printing from {threading.current_thread().name}. {number=}")
        time.sleep(0.1)

with ThreadPoolExecutor(max_workers=4, thread_name_prefix="Worker") as executor:
    for _ in range(4):
        executor.submit(threaded_function)

#race condition
import time
from concurrent.futures import ThreadPoolExecutor

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            new_balance = self.balance - amount
            time.sleep(0.1)  # Simulate a delay
            self.balance = new_balance
        else:
            raise ValueError("Insufficient balance")

account = BankAccount(1000)

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(account.withdraw, 500)
    executor.submit(account.withdraw, 700)

print(f"Final account balance: {account.balance}")