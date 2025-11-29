# Inventory Management System 

class Item:
    def __init__(self,name,price,quality):
        self.name=name
        self.price=price
        self.quantity=quality

    def total_values(self):
        return self.price*self.quantity
    
    def display(self):
        print(f" {self.name}   Price = {self.price}    Quantity = {self.quantity}   Total = {self.total_value()}")
    
class Electronics(Item):
    def __init__(self, name, price, quality,brand,warranty):
        super().__init__(name, price, quality)
        self.brand=brand
        self.warranty=warranty

    def display(self):
        print(f""" 
              Electronics = {self.name}    
              Brand = {self.brand}     
              Warranty = {self.warranty} years     
              Price = {self.price}      
              Quantity = {self.quantity}    
              Total={self.total_values()}""")  

class Clothing(Item):
    def __init__(self, name, price, quality,size,material):
        super().__init__(name, price, quality)  
        self.size=size
        self.material=material

    def display(self):
        print(f"""
              Clothing = {self.name}    
              Size = {self.size}    
              Material = {self.material}  
              Price = {self.price}     
              Quantity = {self.quantity}    
              Total = {self.total_values()}""")


class Food(Item):
    def __init__(self, name, price, quality,expiry):
        super().__init__(name, price, quality)
        self.expiry=expiry

    def display(self):
        print(f"""
              Food = {self.name}   
              Expires = {self.expiry}Days   
              Price = {self.price}    
              Quantity = {self.quantity}Kg    
              Total = {self.total_values()}""")

inventory=[(Electronics('Laptop', 59000, 2, 'HP', 2)),(Clothing('Top', 1500, 5, 'XS-XXL', 'Cotton')),(Food('Apple',100,1,10))]

print("\n Inventory List:\n")
for item in inventory:
    item.display()
    print("-"*50)



# Inventory List:


#               Electronics = Laptop
#               Brand = HP
#               Warranty = 2 years
#               Price = 59000
#               Quantity = 2
#               Total=118000
# --------------------------------------------------

#               Clothing = Top
#               Size = XS-XXL
#               Material = Cotton
#               Price = 1500
#               Quantity = 5
#               Total = 7500
# --------------------------------------------------

#               Food = Apple
#               Expires = 10Days
#               Price = 100
#               Quantity = 1Kg
#               Total = 100
# --------------------------------------------------