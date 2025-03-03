class shoping_cart:

    def __init__(self):
        self.cart = []

    def add_item(self, item):
        self.cart.append(item)

    def remove_item(self, item):
        self.cart.remove(item)

    def show_items(self):
        return self.cart     

    def total_items(self):
        return len(self.cart)      

class shopping:

    s = shoping_cart()
    s.add_item("ball1")
    s.add_item("ball2")
    s.remove_item("ball1")
    print(s.show_items())
    print(s.total_items())
