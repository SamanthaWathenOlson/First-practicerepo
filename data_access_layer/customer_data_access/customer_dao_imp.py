from data_access_layer.customer_data_access.customer_dao_interface import CustomerDAOInterface
from entities.customer_class_info import Customer
from Utilities.create_connection import connection


class CustomerDAOImp(CustomerDAOInterface):

    def insert_into_customers_table(self, customer_obj: Customer) -> Customer:
        sql = "insert into customer values(default, %s, %s) returning customer_id"
        cursor = connection.cursor()
        cursor.execute(sql, (customer_obj.first_name, customer_obj.first_name))
        connection.commit()
        returned_id = cursor.fetchone()[0]
        customer_obj.customer_id = returned_id
        return customer_obj

    def delete_from_customers_table_by_id(self, customer_id: int) -> bool:
        sql = "delete from customer where customer_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [customer_id])
        connection.commit()
        if cursor.rowcount == 1:
            return True
        else:
            return False
