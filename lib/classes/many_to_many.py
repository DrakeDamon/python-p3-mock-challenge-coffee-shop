class Coffee:
    def __init__(self, name):
        self._name = name
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        if len(name) <= 2:
            raise Exception("Name must be longer than 2 characters")


    @property
    def name(self):
        return self._name
    

        
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
        
    
    def customers(self):
        customers_orders = self.orders()
        return list(set([order.customer for order in customers_orders]))
    
    def num_orders(self):
        customers_orders = self.orders()
        return len(customers_orders)

    
    def average_price(self):
        customers_orders = self.orders()
        return sum([order.price for order in customers_orders]) / len(customers_orders)

class Customer:
    def __init__(self, name):
    
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        
        if len(name) < 1 or len(name) > 15:
            raise Exception("Name must be between 1 and 15 characters") 
        self._name = name


    @property
    def name(self):
        return self._name
    
    @name.setter 
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Name must be a string")
        if len(value) < 1 or len(value) > 15:
            raise Exception("Name must be between 1 and 15 characters") 
        self._name = value


        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        customers_orders = self.orders()
        return list(set([order.coffee for order in customers_orders]))
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self._price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price


    @price.setter 
    def price(self, value):
        if not isinstance(value, (int, float)):
            raise Exception("Price must be a number")

