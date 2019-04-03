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
        self.orders = {} # {order_id: due_date, ...}

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

    def add_order(self, order_id, due_date):
        if order_id in self.orders.keys():
            print("order already added")
            return False
        else:
            self.orders[order_id] = due_date
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

    def __repr__(self):
        return str(self.code)

    def __eq__(self, other):
        if self.code == other.code:
            return True
        return False

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
    def __init__(self, order_id, date, due_date):
        self.order_id = order_id
        self.date = date
        self.due_date = due_date
        self.items = {} # items = {item.code = [quantity, pending], {..}, ]
        self.pending = {}
        self.dispatched = {}

    def __repr__(self):
        return str(self.order_id)

    def __eq__(self, other):
        if self.order_id == other:
            return True
        return False

    def add_item(self, item, pending=1): # pending 1 = pending 0 = dispatched
        if item in self.items.keys():
            self.items[item][0] += 1 # [item][0] = quantity
            self.items[item][1] += pending # [item][1] = pending
        else:
            self.items[item][0] = 1
            self.items[item][1] = pending

        print("{} added to order".format(item.code))

        for item, info in self.items.items():
            self.pending[item.code] = info[1]
            self.dispatched[item.code] = [info[0]-info[1]]

    def dispatch_item(self, item, quantity=1): # checks item is in order if so remove the quantity
        if item in self.items.keys():
            if (self.items[item][1] - quantity) >= 0:
                self.items[item][1] -= quantity
                return True
            else:
                print("all items already dispatched")
                return False
        else:
            print("Not item with code: {} in order".format(item.code))
            return False

    def get_pending(self):
        return self.pending

    def get_dispatched_items(self):
        return self.dispatched

    def get_total_price(self):
        total_price = 0
        for item, info in self.items.items():
            total_price += item.price * info[0]
        return total_price

#Class Store
class Store():
    def __init__(self):
        self.clients = {} #clients = { Client_phone: Client object, ...}
        self.orders = {} # orders = {order_id : Order object, ...}
        self.inventory = {} # inventory = {Items object: quantity}

    def create_item(self, item_type, institution, size, price):
        temp_item = Item(item_type, institution, size, price)
        if temp_item in self.inventory.keys():
            print("Item alredy exists")
        else:
            return temp_item

    def add_item_to_inventory(self, new_item, qty=1):
        if new_item in self.inventory.keys():
            self.inventory[new_item] += qty
        else:
            self.inventory[new_item] = qty
        print("item has been added")
        return True

    def remove_item_from_inventory(self, item, qty):
        if item in self.inventory.keys() and self.inventory[item] >= qty:
            self.inventory[item] -= qty
            print("item has been removed")
            return True
        else:
            print("item does not exist or quantity to removed is greater than in inventory")
            return False

    def create_order(self, order_id, date, due_date):
        if order_id in self.orders.keys():
            print("order already exist")
            return False
        else:
            return Order(order_id, date, due_date)

    def add_item_to_order(self, item, order_id, qty=1, pending=1):
        if order_id in self.orders.keys():
            if item in self.inventory.keys() and pending == 0:
                if not self.remove_item_from_inventory(item, qty):
                    return False
            for i in range(qty):
                self.orders[order_id].add_item(item, pending)
                return True
        else:
            print("order does not exist. create order before adding items")
            return False

    def add_order_to_client(self, client, order):
        if client.phone in self.clients.keys():
            if order.order_id in self.orders.keys():
                print("order already exist")
                return False
            else:
                client.add_order(order.order_id, order.date, order.due_date)
                self.orders[order.order_id] = order
            return True
        else:
            print("Client does not exist")
            return False





















