from order import Order
class Coffee:
    def __init__ (self, name):
        if isinstance (value, str) and len (value) >= 3:
            self._name = name
        else:
            raise ValueError("Name must be a string with at least 3 characters.")


    @property
    def name (self):
        return self._name

    @name.setter
    def name (self, value):
        raise AttributeError(" name is immutable.")

    def orders(self):
        return [order for order in Order.all() if order.coffee == self]

    def customers(self):
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return 0
        return sum(order.price for order in orders) / len(orders)

