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
        print("-------------------------------")
        print(f"주문번호: {self.order_id}")
        print(f"총액: {self.total_price():,}원")
        print(self.customer.summary())


# VIP 고객(포인트 0), BASIC 고객(포인트 1000) 생성
customerA = Customer("하정윤", "vip")
customerB = Customer("박건", "basic", 1000)

# 주문 생성
order1 = Order(1, customerA, [("양파", 10000), ("사과", 20000)])
order2 = Order(2, customerB, [("수박", 30000), ("배", 40000)])
order3 = Order(3, customerB, [("바나나", 50000)])

# 10000+20000 = 30000  30000 * 0.95 = 28500원   포인트 적립 28500 * 0.05 = 1425점
order1.pay()
order1.summary()

# 30000+40000 = 70000  70000 * 0.97 = 67900원   포인트 적립 67900 * 0.05 = 3395점
order2.pay()
order2.summary()

# 50000 + 50000 = 100000  100000 * 0.97 = 97000원   포인트 적립 97000 * 0.05 = 4850점

order3.add_item("딸기", 50000)
order3.pay()
order3.summary()



