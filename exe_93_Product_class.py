class Product:
    next_id = 1
    def __init__(self, name, desc, price, qty):
        self._id = Product.next_id
        Product.next_id +=1
        self.name = name
        self.description = desc
        if price < 0: 
            raise ValueError("Price can't be lower than 0")
        else:
            self.price = float(price)
        if qty <= 0:
            raise ValueError("Quantity has to be higher than 0")
        else:
            self.quantity = float(qty)

    def change_quantity(self, quantity):
        self.quantity = quantity

    @property
    def id(self):
        return self._id
    @property
    def get_total_sum(self):
        return self.quantity * self.price if self.quantity < 3 else self.quantity * self.price * 0.8

class ShoppingCart:
    def __init__(self):
        self.products = dict()

    def add_product(self, new_product):
        self.products[new_product.id] = new_product

    def remove_product(self,product_id):
        self.products.pop(product_id)

    def change_product_quantity(self,product_id, new_quantity):
        temp = self.products.get(product_id)
        if temp is not None:
            temp.change_quantity(new_quantity)
    def print_receipt(self):
        receipt = []
        template = '{:3}: {:10} {:>6} {:>8} {:>8}' 
        receipt.append(template.format( "id", "name", "quantity", "price", "amount"))
        template = '{:3}: {:10} {:>6} {:>8,.2f}  {:>8,.2f}' 
        keys = self.products.keys()
        total_sum = 0
        for product_id in keys:
            product = self.products[product_id]
            receipt.append(template.format( product_id, product.name, product.quantity, product.price, product.get_total_sum))
            total_sum += product.get_total_sum
        template = '{:3}: {:10} {:>6} {:>8}  {:>8,.2f}' 
        receipt.append(template.format("", "Sum:", "","" , total_sum))
        return "Bill \n " + "\n".join(item for item in receipt)

if __name__ ==  '__main__':
    prodlist = ShoppingCart()
    prodlist.add_product(Product("onion", "fresh onion", 1.19, 2))
    prodlist.add_product(Product("felix mix", "mix nuts", 9.99, 3))
    prodlist.add_product(Product("crunchy", "peanut butter", 9.12, 4))
    prodlist.add_product(Product("watermelon", "watermelon from Italy", 3.09, 1))
    print(prodlist.print_receipt())
    prodlist.add_product(Product("onion", "fresh onion", 1.19, 3.12))
    prodlist.change_product_quantity(2, 2)
    print(prodlist.print_receipt())
    prodlist.remove_product(4)
    print(prodlist.print_receipt())
