from connection_problem.connection_problem import ConnectionProblem
from connection_problem.nothing_deleted import NothingDeleted
from data_access_layer.customer_data_access.customer_dao_imp import CustomerDAOImp
from entities.customer_class_info import Customer


customer_dao = CustomerDAOImp()


def test_create_customer_record_success():
    test_customer = Customer(0, "Twilight", "Sparkle")
    returned_customer = customer_dao.insert_into_customers_table(test_customer)
    assert returned_customer.customer_id != 0  # will have to increase to 1 to create a customer


def test_create_customer_operational_error_caught():
    try:
        customer_dao.delete_from_customers_table_by_id(-1)
        assert False
    except ConnectionProblem as e:
        return "Bad Connection. Please try again"

def test_create_customer_with_malformed_id():
    customer = Customer("one", "bad", "id")
    result= customer_dao.insert_into_customers_table(customer)
    assert result.customer_id != 0


def test_delete_customer_record_success():
    result = customer_dao.delete_from_customers_table_by_id(-1)  # will have to 1 to positive number to delete a record
    assert result


def test_delete_customer_operational_error_caught():
    try:
        customer_dao.delete_from_customers_table_by_id(1)
        assert False
    except ConnectionProblem as e:
        return "Bad Connection. Please try again"


def test_no_customer_to_delete():
    try:
        customer_dao.delete_from_customers_table_by_id(-1000)
        assert False
    except NothingDeleted as e:
        assert str(e) == "There was no customer with the given Id"
