from store import *

St = Store()

# create client
Camilo = St.create_client("camilo", 610403952159, "camilo@gmail.com")
Caro = St.create_client("Caro", 316212670, "caro@gmail.com")
Fernando = St.create_client("fercho", 603952159, "fernando@gmail.com")

# create Item
ca = St.create_item("camisa", "manuel aya", 12, 25000)
St.create_item("jean", "ricaute", 8, 30000)

# create Order
St.create_order(1001, "20/10/2019", "20/11/2019")
St.create_order(1002, "20/10/2019", "20/11/2019")

#add item to inventory
St.add_item_to_inventory(St.items["man-cam12"])
St.add_item_to_inventory(St.items["ric-jea8"])

# add item to order
St.add_item_to_order(St.items["man-cam12"], 1001, 2, 0)
St.add_item_to_order(St.items["ric-jea8"], 1001,1 , 0)

print(St.clients)
print(St.items)
print(St.inventory)
print(St.orders[1001].items)


