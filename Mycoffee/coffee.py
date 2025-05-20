
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
        from Mycoffee import Order
        return [order for order in Order.all_orders if order.coffee == self] 
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        """Returns order count for this coffee"""
        return len(self.orders())
    
    def average_price(self):
        coffee_orders = self.orders()
        total = sum(order.price for order in coffee_orders)
        return total / len(coffee_orders)
    
    def __repr__(self):
        return f"Coffee = {self.name}"

    def __str__(self):
        return self.name

    
    
# coffee1 = Coffee(1)   
# print(Coffee) 
    
           