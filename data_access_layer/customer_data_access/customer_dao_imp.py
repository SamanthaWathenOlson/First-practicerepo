from connection_problem.connection_problem import ConnectionProblem
from connection_problem.nothing_deleted import NothingDeleted
from data_access_layer.customer_data_access.customer_dao_interface import CustomerDAOInterface
from entities.customer_class_info import Customer


class CustomerDAOImp(CustomerDAOInterface):

    def insert_into_customer_table(self, customer: Customer) -> Customer:
        try:
            sql = "insert into customer values(default, %s, %s) returning customer_id"
            cursor = connection.cursor()
            cursor.execute(sql, (customer.first_name, customer.last_name))
            connection.commit()
            returned_id = cursor.fetchone()[0]
            customer.customer_id = returned_id
            return customer
        except ConnectionProblem as e:
            raise ConnectionProblem(str(e))

    def delete_from_customer_table_by_id(self, customer_id: int) -> bool:
        try:
            sql = "delete from customer where customer_id = %s"
            cursor = connection.cursor()
            cursor.execute(sql, [customer_id])
            connection.commit()
            if cursor.rowcount != 0:
                return True
            else:
                raise NothingDeleted("No record was deleted")
        except ConnectionProblem as e:
            raise ConnectionProblem(str(e))
