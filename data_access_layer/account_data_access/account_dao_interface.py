from abc import ABC, abstractmethod

from entities.account_class_info import Account


class AccountDAOInterface(ABC):

    @abstractmethod
    def create_account_method(self, account: Account) -> Account:
        pass

    @abstractmethod
    def select_account_by_id(self, account_id: int) -> Account:
        pass

    @abstractmethod
    def select_all_account_by_customer_id (self, customer_id: int) -> list[Account]:
        pass

    @abstractmethod
    def update_account_by_id(self, account: Account) -> Account:
        pass

    @abstractmethod
    def transfer_funds(self, sender_id: int, receiver_id: int, amount: float):
        pass

    @abstractmethod
    def delete_account_by_id(self, account_id: int) -> bool:
        pass
