class Customer :
    def __init__(self, name, grade="basic", points=0):
        self.name = name
        self.grade = grade
        self.points = points
    def add_points(self, amount) :
        self.points += amount * 0.05
        self.points = int(self.points)
    def get_discount_rate(self) :
        if self.grade == "basic" :
            return 0.03
        elif self.grade == "vip" :
            return 0.05
    def summary(self) :
        return f"[{self.grade}] {self.name} (포인트: {self.points:,})"



class Order :
    def __init__(self, order_id, customer, items) :
        self.order_id = order_id
        self.customer = customer
        self.items = items
    def total_price(self) :
        total = 0
        for item in self.items :
            total += item[1]
        return int(total * (1 - self.customer.get_discount_rate()))
    def add_item(self, name, price) :
        self.items.append((name, price))
    def pay(self) :
        total = self.total_price()
        self.customer.add_points(total)
        return total
    def summary(self) :
        print(f"주문번호: {self.order_id}")
        print(f"총액: {self.total_price():,}원")
        print(self.customer.summary())


