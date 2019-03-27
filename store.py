"""The program should be capable of adding client, items and orders. Users should be able to be linked
with orders and orders should include items and quantities. The programs should keep track of
 number of in store and dispatched items and orders"""

#Class Client
class Client():
    #Contructor
    def __init__(self, name, phone, email="noemail@null.com"):
        self.name = name
        self.phone = phone
        self.email = email
        self.orders = {}

    def get_phone(self):
        return self.phone

    def get_email(self):
        return self.email

    def get_name(self):
        return self.name

    def get_orders(self):
        return self.orders

    def set_email(self, new_email):
        self.email = new_email

    def set_phone(self, new_phone):
        self.phone = new_phone

    def add_order(self, order_id, status):
        if order_id in self.orders.keys():
            print("order already added")
        else:
            self.orders[order_id] = status
            print("order has been added")

#Class Items
class Items():
    #constructor
    def __init__(self, item_type, institution, size, price):
        self.item_type = item_type
        self.institution = institution
        self.size = size
        self.price = price

    def get_price(self):
        return self.price

    def get_size(self):
        return self.size

    def get_type(self):
        return self.item_type

    def set_price(self, new_price):
        self.price = new_price












