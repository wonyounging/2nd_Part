class clac_class13:
    num1 = num2 = 0
    
    def member_clear(self, x, y):     # 멤버변수 초기화 메서드
        self.num1 = x
        self.num2 = y

    def div(self):              # 나눗셈 메서드
        if self.num2 == 0:
            print('나눗셈 연산은 0으로 나누기가 불가능합니다. 다시입력하세요.')
            return 0
        else:
            return self.num1 / self.num2
        
        
    def squ(self):              # 제곱 메서드
        return self.num1 ** self.num2

n = clac_class13()
n.member_clear(int(input("정수를 입력하세요 : ")),int(input("정수를 입력하세요 : ")))
print('나눗셈 : ', n.div())
print('제곱 : ', n.squ())
