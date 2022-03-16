from data_access_layer.account_data_access.account_dao_interface import AccountDAOInterface
from entities.account_class_info import Account


class AccountDAOImp(AccountDAOInterface):



def create_account_method(self, account: Account) -> Account:
    account =


def select_account_by_id(self, account_id: int) -> Account:
    pass


def select_all_account_by_customer_id(self, customer_id: int) -> list[Account]:
    pass


def update_account_by_id(self, account: Account) -> Account:
    pass


def transfer_funds(self, sender_id: int, receiver_id: int, amount: float):
    pass


def delete_account_by_id(self, account_id: int) -> bool:
    pass
