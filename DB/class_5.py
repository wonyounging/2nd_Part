class Employee:
    name = None
    pay = 0

    def __init__(self, name):
        self.name = name

    def pay_calc(self):
        pass

class Permanent(Employee):  # 자식클래스 : 정규직
    def __init__(self, name):
        super().__init__(name)
    
    def pay_calc(self, base, bonus):
        self.pay = base + bonus
        print('총 수령액 : ', format(self.pay, ','), '원')

class Temporary(Employee):  # 자식클래스 : 임시직
    def __init__(self, name):
        super().__init__(name)

    def pay_calc(self, tpay, time):
        self.pay = tpay * time
        print('총 수령액 : ', format(self.pay, ','), '원')

class Alba(Employee):       # 자식클래스 : 알바
    def __init__(self, name):
        super().__init__(name)
    
    def pay_calc(self, tpay, time):
        if time >= 160:     # 만근인 경우
            self.pay = (tpay * time) + (tpay * 8)
        else:               # 만근이 아닐 경우
            self.pay = tpay * time
        print('총 수령액 : ', format(self.pay, ','), '원')

p = Permanent("홍길동")
t = Temporary("홍길동")
a = Alba("홍길동")

p.pay_calc(3000000, 200000)
t.pay_calc(15000, 80)
a.pay_calc(20000, 160)