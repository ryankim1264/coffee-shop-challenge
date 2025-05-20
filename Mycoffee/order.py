
class Order:
    all_orders = []
    all_coffees = []
    
    def __init__(self, customer , coffee, price=float):
        from Mycoffee import customer as client
        from Mycoffee import coffee as liquid
        if isinstance (customer, str):
            self.customer = client.Customer(customer)
        else :
            raise TypeError("must be a customer") 
     
     
        if isinstance (coffee , str):   
             self.coffee = liquid.Coffee(coffee)
        else: 
            raise TypeError("must be a coffee")
     
     
        if isinstance (price , (int ,float)) and (1.0 <= price <= 10.0):
            self.price = price
        else:
            raise TypeError("price must be between 1.0 to 10.0") 
        
        Order.all_orders.append(self)
        Order.all_coffees.append(self.coffee)
        
    def __repr__(self):
        return f"customer={self.customer}, coffee={self.coffee}, price={self.price}"    
     
    def __str__(self):
        return f"{self.customer} ordered {self.coffee} for ${self.price}"
 
         
 
order1 = Order("7g", "mango flavour", 7.0) 
order2 = Order("reeeee" , "cappucinoo" , 9.0)
order3 = Order("maina" , "mango flavour" , 7.0)


mango_flavor =("mango flavour")
print(order1)   
 
        