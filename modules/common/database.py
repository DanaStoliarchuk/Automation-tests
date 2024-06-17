import sqlite3


class Database:

    def __init__(self):
        self.connection = sqlite3.connect(
            r"C:\\Users\\Dana\\Desktop\\python_basics\\Automation-tests" + r"\\become_qa_auto.db")
        self.cursor = self.connection.cursor()

    @staticmethod
    def _convert_fetchall_to_dict(_rows, _cursor):
        columns = [col[0] for col in _cursor.description]
        data = [dict(zip(columns, row)) for row in _rows]
        return data

    def test_connection(self):
        sqlite_select_query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_query)
        record = self.cursor.fetchall()

        return f"Connected successfully. SQLite Database Version is: {record}"

    def get_all_users(self):
        query = "SELECT id, name, address, city, postalCode, country FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record

    def get_all_products(self):
        query = "SELECT id, name, description, quantity FROM products"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        data = self._convert_fetchall_to_dict(_rows=rows, _cursor=self.cursor)
        return data

    def get_user_address_by_name(self, name: str) -> dict:
        query = (
            f"SELECT address, city, postalCode, country "
            f"FROM customers WHERE name = '{name}'"
        )
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        data = self._convert_fetchall_to_dict(_rows=rows, _cursor=self.cursor)
        return data[0] if data else {}

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id: int) -> dict:
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        data = self._convert_fetchall_to_dict(_rows=rows, _cursor=self.cursor)
        return data[0] if data else {}

    def add_new_product(self, product_id, name, description, qnt):
        query = f"INSERT INTO products(id, name, description, quantity) \
            VALUES({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def get_product_by_id(self, product_id: int) -> dict:
        query = (
            f"SELECT id, name, description, quantity "
            f"FROM products WHERE id = {product_id}"
        )
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        data = self._convert_fetchall_to_dict(_rows=rows, _cursor=self.cursor)
        return data[0] if data else {}
