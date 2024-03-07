class Pesanan:
    def __init__(self, no_pesanan, items, total):
        self.no_pesanan = no_pesanan
        self.items = items
        self.total = total

    def tampilkan_pesanan(self):
        print(f"Nomor Pesanan : {self.no_pesanan}")
        print("Items:")
        for item in self.items:
            print(f"- {item}")
        print(f"Harga Total: Rp{self.total}")

    def __del__(self):
        print(f"Pesanan {self.no_pesanan} Telah diantar!")

def pesanan_decorator(func):
    def wrapper(self, no_pesanan, items, total):
        print(f"Pesanan baru diterima: Pesanan {no_pesanan}")
        func(self, no_pesanan, items, total)
    return wrapper

class FastFoodRestaurant:
    def __init__(self, nama):
        self.nama = nama
        self.orders = []

    @pesanan_decorator
    def place_order(self, no_pesanan, items, total):
        new_order = Pesanan(no_pesanan, items, total)
        self.orders.append(new_order)

    def tampilkan_pesanan(self):
        print(f"Orders at {self.nama}:")
        for order in self.orders:
            order.tampilkan_pesanan()
            print()



restaurant = FastFoodRestaurant("QuickBite")

restaurant.place_order(1, ["Naspad", "Gorengan", "Es Teh"], 25000)
restaurant.place_order(2, ["Bubur Ayam", "Es Teh"], 10000)

restaurant.tampilkan_pesanan()

del restaurant