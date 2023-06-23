class clac_class14:
    num1 = num2 = 0
    def __init__(self, x, y):   # 생성자
        self.num1 = x
        self.num2 = y

    def div(self):              # 나눗셈 메서드
        if self.num2 == 0:
            print('나눗셈 연산은 0으로 나누기가 불가능합니다. 다시입력하세요.')
        else:
            print('나눗셈 : ', self.num1 / self.num2)
        
    def squ(self):              # 제곱 메서드
        print('제곱 : ', self.num1 ** self.num2)

    @classmethod        # 함수 장식자
    def filter(cls, str):
        year = str[:2]
        month = str[2:4]
        days = str[4:6]
        sex = int(str[7])
        
        if sex < 3:         # 1900년대생
            year = f"19{year}"
            if sex == 1:
                sex = "남성"
            else:
                sex = "여성"
            print(f"{year}년 {month}월 {days}일 출생한 {sex}입니다.")
        elif sex < 5:       # 2000년대생
            year = f"20{year}"
            if sex == 3:
                sex = "남성"
            else:
                sex = "여성"
            print(f"{year}년 {month}월 {days}일 출생한 {sex}입니다.")
        else:
            print('잘못된 입력')

n = clac_class14(int(input("정수를 입력하세요 : ")),int(input("정수를 입력하세요 : ")))
jumin_str = (input("주민번호 입력 : "))
n.div()
n.squ()
clac_class14.filter(jumin_str)