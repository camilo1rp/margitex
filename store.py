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
            return False
        else:
            self.orders[order_id] = status
            print("order has been added")
            return True

#Class Item
class Item():
    #constructor
    def __init__(self, item_type, institution, size, price):
        self.item_type = item_type
        self.institution = institution
        self.size = size
        self.price = price
        self.code = item_type[::3] + institution[::3] + str(size)

    def get_code(self):
        return self.code

    def get_price(self):
        return self.price

    def get_size(self):
        return self.size

    def get_type(self):
        return self.item_type

    def set_price(self, new_price):
        self.price = new_price

#Class Order
class Order():
    def __init__(self, order_id, date):
        self.order_id = order_id
        self.date = date
        self.items = {} # items = {item.code = [quantity, pending], {..}, ]
        self.pending = {}

    def add_item(self, item, pending=1): # pending 1 = pending 0 = dispatched
        if item in items.keys():
            self.items[item][0] += 1 # [item][0] = quantity
            self.items[item][1] += pending # [item][1] = pending
        else:
            self.items[item][0] = 1
            self.items[item][1] = pending

        for item, info in self.items.items():
            self.pending[item] = info[1]

    def dispatch_item(self, item, quantity=1):
        if item in items.keys():
            if (self.items[item][1] - quantity) >= 0:
                self.items[item][1] -= quantity
                return True
            else:
                print("all items already dispatched")
                return False
        else:
            print("Not item with code: {} in order".format(item))
            return False

    def get_pending(self):
        return self.pending

    def get_total_price(self):
        total_price = 0
        for item, info in self.items.items():
            total price += item.price * info[0]
        return total_price













