import mysql.connector


class InventoryRepo:
    def __init__(self):
        self.connection = mysql.connector.connect(
            user="root",
            password="123456789",
            host="localhost",
            database="Inventory"
        )
        self.cursor = self.connection.cursor(prepared=True)

    def get_items(self):
        query = "SELECT id, name, price, quantity, supplier_name FROM Inventory"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def get_item_by_id(self, id):
        query = "SELECT id, name, price, quantity, supplier_name FROM Inventory WHERE id=%s"
        self.cursor.execute(query, (id,))
        return self.cursor.fetchone()

    def add_item(self, name, price, quantity, supplier_name):
        query = "INSERT INTO Inventory (name, price, quantity, supplier_name) VALUES (%s, %s, %s, %s)"
        values = (name, price, quantity, supplier_name)
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
            return self.cursor.lastrowid
        except Exception as e:
            print(str(e))
            self.connection.rollback()
            return None

    def delete_item(self, id):
        query = "DELETE FROM Inventory WHERE id=%s"
        try:
            self.cursor.execute(query, (id,))
            self.connection.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(str(e))
            return False

    def search_item(self, id=None, name=None):
        cursor = self.connection.cursor()
        try:
            if id and name:
                cursor.execute("SELECT * FROM Inventory WHERE id=%s AND name=%s", (id, name))
            elif id:
                cursor.execute("SELECT * FROM Inventory WHERE id=%s", (id,))
            elif name:
                cursor.execute("SELECT * FROM Inventory WHERE name=%s", (name,))
            else:
                return []

            result = cursor.fetchall()
            items = []
            for row in result:
                item = {
                    "id": row[0],
                    "name": row[1],
                    "price": row[2],
                    "quantity": row[3],
                    "supplier_name": row[4]
                }
                items.append(item)

            return items
        except Exception as e:
            print(str(e))
            return []
        finally:
            cursor.close()

    def update_item(self, id, name=None, price=None, quantity=None, supplier_name=None):
        update_query = "UPDATE Inventory SET"
        update_params = []

        if name:
            update_query += " name=%s,"
            update_params.append(name)
        if price:
            update_query += " price=%s,"
            update_params.append(price)
        if quantity:
            update_query += " quantity=%s,"
            update_params.append(quantity)
        if supplier_name:
            update_query += " supplier_name=%s,"
            update_params.append(supplier_name)

        update_query = update_query.rstrip(",") + " WHERE id=%s"
        update_params.append(id)

        try:
            self.cursor.execute(update_query, tuple(update_params))
            self.connection.commit()
            return self.cursor.rowcount > 0
        except Exception as e:
            print(str(e))
            return False
