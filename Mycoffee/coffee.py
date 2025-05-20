
class Coffee :
    def __init__(self , name):
        if isinstance(name , str) and (3 <= len(name)):
         self.name = name
        else:
            raise ValueError("must be a str, at least 3 characters)")
    @property
    def Coffee(self):
        return self._name 
    
    def __repr__(self):
        return f"Coffee = {self.name}"

    def __str__(self):
        return self.name

    
    
# coffee1 = Coffee(1)   
# print(Coffee) 
    
           