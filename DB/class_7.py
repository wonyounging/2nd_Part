class Rectangle:
    width = 0                       
    height = 0
    def __init__(self, w, h):       # 생성자
        self.width = w
        self.height = h

    def area_calc(self):            # 넓이를 구하는 메서드
        print(f"사각형의 넓이 : {self.width * self.height}")
              
    def circum_calc(self):          # 둘레를 구하는 메서드
        print(f"사각형의 둘레 : {(self.width + self.height) * 2}")

if __name__ == "__main__" :         # main 함수 시작점 지정
    print("사각형의 넓이와 둘레를 계산합니다.")
    rect = Rectangle(int(input("사각형의 가로 입력 : ")), int(input("사각형의 세로 입력 : ")))
    print("------------------")
    rect.area_calc()
    rect.circum_calc()
    print("------------------")