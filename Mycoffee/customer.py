class Customer:
    def __init__(self, name):
        self.name = name
        
    @property
    def customer(self):   
        return self._name
    @customer.setter
    def customer(self , name):
        if isinstance(name,str) and (1 <=len(name) <= 15):
            self._name = name
        else:
            
            raise 
    ValueError("must be a str, 1–15 characters")
    
    def orders(self):
        from Mycoffee import order as requests
        return [ request for request in requests.Order.all_orders if self.name == request.customer.name]
    
    def coffees(self):
        from Mycoffee import coffee as drinks
        return[drinks for drink in drinks.order.all_coffees]
    
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return f"Customer('{self.name}')"
    
    
    
yebeee= Customer("yebeee")
yebeee.orders()

    