from tkinter import messagebox
from InventoryRepository import InventoryRepo


class InventoryController:
    def __init__(self):
        self.repository = InventoryRepo()
        self.item_table = None

    def get_items(self):
        items = self.repository.get_items()
        return items

    def load_items_to_table(self, items):
        if self.item_table is not None:
            self.item_table.delete(*self.item_table.get_children())
            for item in items:
                id, name, quantity, price, supplier_name = item
                self.item_table.insert('', 'end', values=(id, name, quantity, price, supplier_name))
            self.item_table.update()

    def load_items(self):
        items = self.repository.get_items()
        self.load_items_to_table(items)

    def add_item(self, name, quantity, price, supplier_name):
        result = self.repository.add_item(name, price, quantity, supplier_name)

        if result:
            # display success message in messagebox
            messagebox.showinfo("Success", "Item added successfully.")
            self.load_items()
        else:
            # display error message in messagebox
            messagebox.showerror("Error", "Failed to add item.")

    def delete_item(self, id):
        result = self.repository.delete_item(id)

        if result:
            # display success message in messagebox
            messagebox.showinfo("Success", "Item deleted successfully.")
            self.load_items()
        else:
            # display error message in messagebox
            messagebox.showerror("Error", "Failed to delete item.")

    def search_item(self, id=None, name=None):
        try:
            result = self.repository.search_item(id, name)
            if result:
                messagebox.showinfo("Search Results", "Record found")
                return result
            else:
                messagebox.showerror("Error", "No record found")
                return None
        except Exception as e:
            messagebox.showerror("Error", str(e))
            return None

    def update_item(self, id, name=None, price=None, quantity=None, supplier_name=None):
        try:
            item = self.repository.get_item_by_id(id)
            if not item:
                messagebox.showerror("Update Failed", "Item with ID {} not found.".format(id))
                return False

            self.repository.update_item(id, name, price, quantity, supplier_name)
            updated_item = self.repository.get_item_by_id(id)
            messagebox.showinfo("Update Successful", "Item successfully updated.")

            return updated_item

        except ValueError as ve:
            messagebox.showerror("Update Failed", str(ve))
            return False
