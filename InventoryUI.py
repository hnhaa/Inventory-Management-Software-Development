import tkinter as tk
from tkinter import ttk
from InventoryController import InventoryController


class InventoryUI:
    def __init__(self, master):
        self.master = master
        self.controller = InventoryController()

        self.master.title("Inventory Management System")
        self.master.geometry("1000x600")
        self.master.resizable(True, True)

        self.master.after(0, self.update_treeview)

        self.id_entry = None
        self.name_entry = None
        self.price_entry = None
        self.quantity_entry = None
        self.supplier_name_entry = None

        # create button frame
        button_frame = tk.Frame(master)
        button_frame.grid(row=0, column=0, padx=10, pady=10)

        # create add button
        self.add_button = tk.Button(button_frame, text="Add", command=self.open_add_window)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # create delete button
        self.delete_button = tk.Button(button_frame, text="Delete", command=self.open_delete_window)
        self.delete_button.grid(row=1, column=1, padx=10, pady=10)

        # create update button
        self.update_button = tk.Button(button_frame, text="Update", command=self.open_update_window)
        self.update_button.grid(row=2, column=1, padx=10, pady=10)

        # create search button
        self.search_button = tk.Button(button_frame, text="Search", command=self.open_search_window)
        self.search_button.grid(row=3, column=1, padx=10, pady=10)

        # create search_result_displayed flag
        self.search_results_displayed = False

        self.item_frame = ttk.Frame(master)
        self.item_frame.grid(row=6, column=0, padx=10, pady=10)

        # create treeview
        self.item_table = ttk.Treeview(self.item_frame, columns=('id', 'name', 'price', 'quantity', 'supplier_name'),
                                       show='headings')
        self.item_table.pack(fill='both', expand=True)

        # add columns
        self.item_table.heading('id', text='ID')
        self.item_table.heading('name', text='Name')
        self.item_table.heading('price', text='Price')
        self.item_table.heading('quantity', text='Quantity')
        self.item_table.heading('supplier_name', text='Supplier Name')

        # data to treeview
        items = self.controller.get_items()
        for item in items:
            id, name, price, quantity, supplier_name = item
            self.item_table.insert('', 'end', values=(id, name, price, quantity, supplier_name))

    def update_treeview(self, update_type=None):
        if update_type in ['add', 'delete', 'update']:
            items = self.controller.get_items()
            self.item_table.delete(*self.item_table.get_children())
            for item in items:
                id, name, quantity, price, supplier_name = item
                self.item_table.insert('', 'end', values=(id, name, price, quantity, supplier_name))
        self.master.after(3000, self.update_treeview)

    def load_items(self):
        return self.controller.load_items()

    # Add
    def open_add_window(self):
        add_window = tk.Toplevel(self.master)
        add_window.title("Add Item")

        # add_entry widgets and button here
        add_frame = tk.Frame(add_window)
        add_frame.grid(row=0, column=0, padx=10, pady=10)

        add_frame_label = tk.Label(add_frame, text="Add Item ")
        add_frame_label.grid(row=0, column=0, sticky="e")

        name_label = tk.Label(add_frame, text="Name: ")
        name_label.grid(row=1, column=0, sticky="e")
        self.name_entry = tk.Entry(add_frame)
        self.name_entry.grid(row=1, column=1, sticky="e")

        price_label = tk.Label(add_frame, text="Price: ")
        price_label.grid(row=2, column=0, sticky="e")
        self.price_entry = tk.Entry(add_frame)
        self.price_entry.grid(row=2, column=1, sticky="e")

        quantity_label = tk.Label(add_frame, text="Quantity: ")
        quantity_label.grid(row=3, column=0, sticky="e")
        self.quantity_entry = tk.Entry(add_frame)
        self.quantity_entry.grid(row=3, column=1, sticky="e")

        supplier_name_label = tk.Label(add_frame, text="Supplier Name: ")
        supplier_name_label.grid(row=4, column=0, sticky="e")
        self.supplier_name_entry = tk.Entry(add_frame)
        self.supplier_name_entry.grid(row=4, column=1, sticky="e")

        add_item_button = tk.Button(add_frame, text="Add", command=self.add_item)
        add_item_button.grid(row=5, column=2, padx=5)

    def add_item(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        supplier_name = self.supplier_name_entry.get()
        result = self.controller.add_item(name, quantity, price, supplier_name)

        # clear the ID entry
        self.name_entry.delete(0, 'end')
        self.price_entry.delete(0, 'end')
        self.quantity_entry.delete(0, 'end')
        self.supplier_name_entry.delete(0, 'end')

        # update the treeview to show the new item
        self.update_treeview('add')

        return result

    # Delete
    def open_delete_window(self):
        delete_window = tk.Toplevel(self.master)
        delete_window.title("Delete Item")

        # delete_entry widgets and button here
        delete_frame = tk.Frame(delete_window)
        delete_frame.grid(row=0, column=0, padx=10, pady=10)

        delete_frame_label = tk.Label(delete_frame, text="Delete Item ")
        delete_frame_label.grid(row=0, column=0, sticky="e")

        id_label = tk.Label(delete_frame, text="ID: ")
        id_label.grid(row=1, column=0, sticky="e")
        self.id_entry = tk.Entry(delete_frame)
        self.id_entry.grid(row=1, column=1, sticky="e")

        delete_item_button = tk.Button(delete_frame, text="Delete", command=self.delete_item)
        delete_item_button.grid(row=5, column=2, padx=5)

    def delete_item(self):
        # get the ID from the ID entry
        id = self.id_entry.get()

        result = self.controller.delete_item(id)

        # clear the ID entry
        self.id_entry.delete(0, 'end')

        # update the treeview to show the new item
        self.update_treeview('delete')

        return result

    # Search
    def open_search_window(self):
        search_window = tk.Toplevel(self.master)
        search_window.title("Search Item")

        # search_entry widgets and button here
        search_frame = tk.Frame(search_window)
        search_frame.grid(row=0, column=0, padx=10, pady=10)

        search_frame_label = tk.Label(search_frame, text="Search Item ")
        search_frame_label.grid(row=0, column=0, sticky="e")

        id_label = tk.Label(search_frame, text="ID: ")
        id_label.grid(row=1, column=0, sticky="e")
        self.id_entry = tk.Entry(search_frame)  # Renamed to search_id_entry
        self.id_entry.grid(row=1, column=1, sticky="e")

        name_label = tk.Label(search_frame, text="Name: ")
        name_label.grid(row=2, column=0, sticky="e")
        self.name_entry = tk.Entry(search_frame)  # Renamed to search_name_entry
        self.name_entry.grid(row=2, column=1, sticky="e")

        search_item_button = tk.Button(search_frame, text="Search", command=self.search_item)
        search_item_button.grid(row=5, column=2, padx=5)

    def search_item(self):
        # get the ID & name from the ID & name entry
        id = self.id_entry.get()
        name = self.name_entry.get()

        # Call the controller's search_item method to retrieve search results
        result = self.controller.search_item(id, name)

        # Clear the ID and name fields
        self.id_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')

        # Clear the current contents of the treeview

        self.item_table.delete(*self.item_table.get_children())

        # If search results are found, insert them into the treeview
        if result:
            for item in result:
                self.item_table.insert("", "end", values=list(item.values()))
            self.search_results_displayed = True
        else:
            self.search_results_displayed = False

    # Update
    def open_update_window(self):
        update_window = tk.Toplevel(self.master)

        update_window.title("Update Item")

        # update_entry widgets and button here
        update_frame = tk.Frame(update_window)
        update_frame.grid(row=0, column=0, padx=10, pady=10)

        update_frame_label = tk.Label(update_frame, text="Update Item ")
        update_frame_label.grid(row=0, column=0, sticky="e")

        id_label = tk.Label(update_frame, text="ID: ")
        id_label.grid(row=1, column=0, sticky="e")
        self.id_entry = tk.Entry(update_frame)
        self.id_entry.grid(row=1, column=1, sticky="e")

        name_label = tk.Label(update_frame, text="Name: ")
        name_label.grid(row=2, column=0, sticky="e")
        self.name_entry = tk.Entry(update_frame)
        self.name_entry.grid(row=2, column=1, sticky="e")

        price_label = tk.Label(update_frame, text="Price: ")
        price_label.grid(row=3, column=0, sticky="e")
        self.price_entry = tk.Entry(update_frame)
        self.price_entry.grid(row=3, column=1, sticky="e")

        quantity_label = tk.Label(update_frame, text="Quantity: ")
        quantity_label.grid(row=4, column=0, sticky="e")
        self.quantity_entry = tk.Entry(update_frame)
        self.quantity_entry.grid(row=4, column=1, sticky="e")

        supplier_name_label = tk.Label(update_frame, text="Supplier: ")
        supplier_name_label.grid(row=5, column=0, sticky="e")
        self.supplier_name_entry = tk.Entry(update_frame)
        self.supplier_name_entry.grid(row=5, column=1, sticky="e")

        update_item_button = tk.Button(update_frame, text="Update", command=self.update_item)
        update_item_button.grid(row=5, column=2, padx=5)

    def update_item(self):
        id = self.id_entry.get()
        name = self.name_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()
        supplier_name = self.supplier_name_entry.get()

        result = self.controller.update_item(id, name, price, quantity, supplier_name)

        self.id_entry.delete(0, 'end')
        self.name_entry.delete(0, 'end')
        self.price_entry.delete(0, 'end')
        self.quantity_entry.delete(0, 'end')
        self.supplier_name_entry.delete(0, 'end')

        # Clear the current contents of the treeview
        self.item_table.delete(*self.item_table.get_children())

        # If search results are found, insert them into the treeview
        if result:
            self.item_table.insert("", "end", values=result)
            self.search_results_displayed = True
        else:
            self.search_results_displayed = False


if __name__ == '__main__':
    root = tk.Tk()
    inventory = InventoryUI(root)
    root.mainloop()
