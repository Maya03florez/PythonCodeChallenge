#!/usr/bin/env python3

# Encapsulation:
# Implement a CuentaBancaria class with a private saldo attribute. Add
# methods to deposit and withdraw money.

class BankAccount():
    def __init__(self, balance) -> None:
        self.__balance = balance

    def withdraw_money(self, amount_to_withdraw):
        if self.__balance >= amount_to_withdraw:
            self.__balance -= amount_to_withdraw
            return f'Here is your money {amount_to_withdraw} and you have {self.__balance} left'
        else:
            return f'You do not have enough balance'
        
    def deposit_money(self, money_to_deposit):
        print(self.__balance)
        if money_to_deposit > 0:
            self.__balance += money_to_deposit
            return f'You have a total of {self.__balance}'
        else:
            return f'You must add a positive number'
        
carlos_account = BankAccount(400)
print(carlos_account.deposit_money(600))
print(carlos_account.withdraw_money(1000))