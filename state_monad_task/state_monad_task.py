from pymonad.tools import curry
from pymonad.state import State

# Для простоты здесь нет класса счета и мы просто вычитаем числа
@curry(2)
def transfer_with_audit(account_to, account_from):
    def transfer(logs):
        return account_from - account_to, [f'Переведены деньги на счет {account_to}'] + logs
    return State(transfer)

@curry(2)
def add_cash_with_audit(value, account):
    def add_cash(logs):
        return account + value, logs + [f'Совершено пополнение на сумму {value}']
    return State(add_cash)

first = State.insert(35)

accountWithAllActions = first.then(transfer_with_audit(15)).then(add_cash_with_audit(10))


res, l = accountWithAllActions.run(['a'])