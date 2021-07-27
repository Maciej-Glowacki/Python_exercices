class Product:
    """
    This is a class representing a simple shop product.

    :argument _new_id : int
        Unique ID setter 
    :param name : str
        Name for a product
    :param description : str
        Product description
    :param price : float
        Product price (in PLN) { > 0}
    :param quantity : int
        Product quantity { > 0}
    """
    next_id = 1
    def __init__(self, name, desc, price, qty):
        self._id = Product.next_id
        Product.next_id +=1
        self.name = name
        self.description = desc
        if price < 0: 
            raise ValueError("Price can't be lower than 0.00")
        else:
            self.price = float(price)
        if qty <= 0:
            raise ValueError("Quantity has to be greater than 0")
        else:
            self.quantity = float(qty)

    @property
    def id(self):
        return self._id
    
    @property
    def get_total_sum(self):
        return self.quantity * self.price

if __name__ ==  '__main__':
    prodlist = []
    try:
        prodlist.append(Product("onion", "onion", 1.19, 2))
        prodlist.append(Product("Almond milk", "Almond milk for shakes", 9.99, 3))
        prodlist.append(Product("peanut butter", "peanut butter - crunchy", 9.12, 4))
        prodlist.append(Product("nuddles", "nuddles for tomato soup", 3.34, 1))
    except ValueError as er:
        print("Error!!! ", er)
        print("------------------------------")
    for prod in prodlist:
        print(f'id: {prod.id}\n product: {prod.name}\n description: {prod.description}\n price: {prod.price}\n quantity: {prod.quantity}\n payment: {prod.get_total_sum}')
