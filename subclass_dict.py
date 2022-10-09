coupons = {
    'IT61YYN9I': 0.07,
    'RE26XVK3T': 0.05,
    'CN73GRZ1R': 0.05,
    'IQ33WUG3S': 0.03,
    'QG85QKC0U': 0.02
}

class OnlineShoppingCart(dict):
    def __init__(self, items: dict[str, tuple[float, int]]):
        super().__init__()
        self.update(items)
        self.coupons: set[str] = set()

    def apply_coupon(self, coupon_code: str):
        self.coupons.add(coupon_code)

    def total_price(self) -> float:
        res = 0
        for price, amount in self.values():
            res += price * amount
        discount = sum(coupons.get(coup, 0) for coup in self.coupons)
        return res*(1 - discount)


dns0123 = OnlineShoppingCart({
    'Xiaomi MIX': (32200, 2),
    'Noname charger 15W': (340, 3),
    'AKG K272 MK2': (9750, 1)
})
print(dns0123)
print(dns0123.total_price())
dns0123.apply_coupon('CN73GRZ1R')
dns0123.apply_coupon('CN73GRZ1R')
print(dns0123.total_price())
dns0123.apply_coupon('RE26XVK3T')
print(dns0123.total_price())
