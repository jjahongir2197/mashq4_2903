class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        return f"{self.name} - {self.price} so'm"


class Cart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} savatga qo'shildi.")

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)
                print(f"{name} o'chirildi.")
                return
        print("Mahsulot topilmadi.")

    def total_price(self):
        total = 0
        for product in self.products:
            total += product.price
        return total

    def show_cart(self):
        print("\nSavat:")
        for product in self.products:
            print(product.get_info())
        print("Jami:", self.total_price())


class Shop:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def show_products(self):
        print("\nMahsulotlar:")
        for product in self.products:
            print(product.get_info())


def start_shop():
    shop = Shop()
    cart = Cart()

    p1 = Product("Telefon", 2000000)
    p2 = Product("Noutbuk", 7000000)
    p3 = Product("Quloqchin", 150000)

    shop.add_product(p1)
    shop.add_product(p2)
    shop.add_product(p3)

    shop.show_products()

    cart.add_product(p1)
    cart.add_product(p3)

    cart.show_cart()

    cart.remove_product("Telefon")

    cart.show_cart()


start_shop()
