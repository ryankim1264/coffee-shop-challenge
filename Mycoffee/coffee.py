
class Coffee :
    def __init__(self , name):
        if isinstance(name , str) and (3 <= len(name)):
         self.name = name
        else:
            raise ValueError("must be a str, at least 3 characters)")
    @property
    def Coffee(self):
        return self._name 
    
    
    def orders(self):
        from Mycoffee import Order as requests
        return [requests for request in requests.Order.all_orders if request.order.coffee == self] 
    
    def customers(self):
        from Mycoffee import order as requests
        return [requests for request in requests.Order.all_orders if request.order.coffee == self]
    
    def num_orders(self):
        from Mycoffee import order as requests
        lists = [requests for request in requests.Order.all_orders if self == request.order.coffee]
    
    def average_price(self):
        return sum(order.price for order in self.orders()) / len(self.orders()) if self.orders() else 0
    
    def __repr__(self):
        return f"Coffee = {self.name}"

    def __str__(self):
        return self.name

    
    
# coffee1 = Coffee(1)   
# print(Coffee) 
    
           