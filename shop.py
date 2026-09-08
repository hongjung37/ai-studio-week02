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



        