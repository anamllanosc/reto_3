class MenuItem:
    def __init__(self,name:str,price:int):
        self.name=name
        self.price=price

class Beverage(MenuItem):
    def __init__(self,name,price,temperature:str):
        super().__init__(name,price)
        self.temperature=temperature

class Appetizer(MenuItem):
    def __init__(self,name,price,pieces:int):
        super().__init__(name,price)
        self.pieces=pieces

class MainCourse(MenuItem):
    def __init__(self,name,price,accompainments):
        super().__init__(name,price)
        self.accompainments=accompainments


class Order:
    def __init__(self,item):

        self.order_list=[]
        self.item=item

    def add_item(self):
        while True:
            item= str(input("Ingrese el producto que desea agregar a su pedido o (fin) para terminar: "))
            if self.item.lower()=="fin":
                break
            elif self.item.lower() in menu_items:
                self.order_list.append(menu_items[self.item.lower()].name)
            else:
                print(f"El producto '{item}' no esta en el menu. Ingrese nuevamente su pedido: ")
                True
        print("\n")
        print (f"-> Order: {self.order_list}")
    

    def total_bill(self):

        self.bill=0
        for product in self.order_list:
            if product.lower() in menu_items:
                self.bill+=menu_items[product.lower()].price
        
        print(f"->TOTAL A PAGAR = ${self.bill}")

    def discounts(self):
        beverage_count=sum(isinstance(menu_items[item.lower()], Beverage) for item in self.order_list)
        appetizer_count=sum(isinstance(menu_items[item.lower()], Appetizer) for item in self.order_list)
        main_course_count=sum(isinstance(menu_items[item.lower()], MainCourse) for item in self.order_list)
        
        discount=0

        if   beverage_count== appetizer_count== main_course_count and 3>=beverage_count >=1:
            
            
            discount=(self.bill*0.05)
            final_bill=self.bill-discount
            print(f"Descuento a aplicar: -{discount}$")
            print(f"TOTAL A PAGAR (Descuento aplicado)=> {final_bill}$") 
            

        elif beverage_count== appetizer_count== main_course_count and beverage_count >=4:

            discount=(self.bill*0.10)
            final_bill=self.bill-discount
            print(f"Descuento a aplicar: -{discount}$")
            print(f"TOTAL A PAGAR (Descuento aplicado)=>  {final_bill}$") 



        elif beverage_count==main_course_count and beverage_count==4:
            discount=(self.bill*0.08)
            final_bill=self.bill-discount
            print(f"Descuento a aplicar: -{discount}$")
            print(f"TOTAL A PAGAR (Descuento aplicado)=> {final_bill}$")

        else: 
            print(f"Descuento a aplicar: 0$")

        
    
#Beverages
coffe=Beverage("Coffe",3000,"Hot")
chocolate=Beverage("Chocolate",3500,"Hot")
lemonade=Beverage("Lemonade",2500,"Cold")
water=Beverage("Water",2000,"Hot")

#Appetizer
spicy_shrimp=Appetizer("Spicy Shrimp",20000,"6")
mini_quiches=Appetizer("Mini Quiches",18000,"4")
fried_platains=Appetizer("Fried Platains",15000,"8")
capresse_salad=Appetizer("Capresse Salad",15000,"1")

#Main Course
grilled_salmon=MainCourse("Grilled Salmon",38000,"Accompainments= Mashed Potatoes and Mango Salad")
BBQ_ribs=MainCourse("Bbq Ribs",34000,"Accompainments= Fries")
stuffed_chicken=MainCourse("Stuffed Chicken",30000,"Accompainments= Parsley Rice")
vegetarian_curry=MainCourse("Vegetarian Curry",30000,"Accompainments= Pita Bread")

order = Order()

menu_items={"coffe":coffe,"chocolate":chocolate,"lemonade":lemonade,"water":water,
            "spicy shrimp":spicy_shrimp,"mini quiches":mini_quiches,"fried platains":fried_platains,"capresse salad":capresse_salad,
            "grilled salmon":grilled_salmon,"bbq ribs":BBQ_ribs,"stuffed chicken":stuffed_chicken,"vegetarian curry":vegetarian_curry}
categories={}


print ("\nMENU:\n")
for item in menu_items:
    print(f"-{menu_items[item].name.capitalize()}")

print("\n")
print("DESCUENTOS:\n-Entre uno y tres productos de cada categoria: 5% de descuento\n-Desde cuatro productos de cada categoria: 10% de descuento\n-Cuatro bebidas y cuatro platos principales:8% de descuento")
print("\n")
    
order.add_item(menu_items)
order.total_bill()
order.discounts()

