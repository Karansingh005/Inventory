class Product:

    def __init__(self,price,id,qty):

        self.price=price
        self.id=id
        self.quantity=qty

    def __str__(self):
        return "Product of ID %s has a price of %s and quantity of %s" %(self.id,self.price,self.quantity)

    def get_price(self):
        return self.price

    def get_id(self):
        return self.id

    def get_quantity(self):
        return self.quantity

    def sum_up(self):
        return self.quantity * self.price

class Inventory(Product):

    def __init__(self,price,id,qty):
        super().__init__(price,id,qty)
        self.invo={}
        self.inv=[]

    def add_item(self):
        self.invo[f'{self.id}']=[f'{self.price}',f'{self.quantity}']

    def add_total(self):
        self.inv.append(self.sum_up())

    def get_total(self):

        total=0
        for i in self.inv:
            total+=i

        print(total)

def replay():

    return input('Do you want to continue? Enter Yes or No: ').lower().startswith('y')


def main():
    while True:
        print("Please enter the following options for various functions")
        print("1. To add product to inventory")
        print("2. To display the inventory")
        print("3. To display total value of inventory")
        print("4. To exit ")
        p = eval(input("So, what is your option?"))
        choice=True
        while choice:
            if p==1:

                ID=input("Please enter the ID for the product.")
                Price=input("Please enter the price for the product.")
                Quantity=input("Please enter the Quantity for the product.")
                ine = Inventory(Price, ID, Quantity)
                ine.add_item()
                print(ine)
                if replay():
                    main()
                else:
                    choice = False

            elif p==2:

                print(ine)

main()