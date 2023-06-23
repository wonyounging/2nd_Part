import pymysql
import sys
import os

# print(pymysql.version_info)

u = input('user id : ')
p = input('user pw : ')

config = {
    'host' : '127.0.0.1',
    'user' : u,
    'password' : p,
    'database' : 'test_db',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True
}

# 테이블 생성 함수
def create_table():
    try:
        conn = pymysql.connect(**config)    # db 연동
        cursor = conn.cursor()              # sql 실행 객체
        # print('connect success')            # db 연동 성공 출력

        # goods 테이블 생성
        sql = "create table if not exists goods(code integer primary key not null, name VARCHAR(20) not null, su integer default 0, dan integer default 0)"
        cursor.execute(sql) # sql문 실행
    # 에러 처리
    except Exception as e:
        print('db error : ', e)
        conn.rollback() # 실행 취소
    finally:
        cursor.close()
        conn.close()    
    
# 상품 추가 함수
def add_product():
    try:
        conn = pymysql.connect(**config)    # db 연동
        cursor = conn.cursor()              # sql 실행 객체

        print('\n<<<상품등록>>>')
        in_code = int(input('코드 입력 : '))
        
        # 번호 중복 확인
        sql = f"select * from goods where code = {in_code}"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows) > 0:
            print('중복된 코드입니다. 다시 입력해주세요.')
        else:
            in_name = input('상품 입력 : ')
            in_su = int(input('수량 입력 : '))
            in_dan = int(input('단가 입력 : '))
            sql = f"insert into goods values({in_code}, '{in_name}', {in_su}, {in_dan})"
            cursor.execute(sql)
            conn.commit()
            print('상품등록을 성공했습니다.')
    # 에러 처리
    except Exception as e:
        print('db error : ', e)
        conn.rollback() # 실행 취소
    finally:
        cursor.close()
        conn.close() 

# 테이블 검색 함수
def search_table():
    try:
        conn = pymysql.connect(**config)    # db 연동
        cursor = conn.cursor()              # sql 실행 객체
        # 테이블 조회
        cursor.execute("select * from goods")
        rows = cursor.fetchall()

        print('\n<<<상품목록조회>>>')
        print('CODE \t NAME \t\t SU \t DAN') # 레코드 출력
        for row in rows:
            print (row[0],'\t',row[1],'\t',row[2],'\t',row[3])
    # 에러 처리
    except Exception as e:
        print('db error : ', e)
        conn.rollback() # 실행 취소
    finally:
        cursor.close()
        conn.close() 

# 코드별 검색 함수 호출
def search_product_code():
    try:
        conn = pymysql.connect(**config)    # db 연동
        cursor = conn.cursor()              # sql 실행 객체
        # 특정 레코드 조회
        print('\n<<<코드별조회>>>')
        search_code = input('조회할 코드를 입력하세요 : ')
        sql = f"select * from goods where code = {search_code}"
        cursor.execute(sql)
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print (f'조회결과는 코드 : {row[0]}, 상품 : {row[1]}, 수량 : {row[2]}, 단가 : {row[3]} 입니다.')
        else:
            print('조회결과 입력한 상품에 맞는 상품이 없습니다.')
    # 에러 처리
    except Exception as e:
        print('db error : ', e)
        conn.rollback() # 실행 취소
    finally:
        cursor.close()
        conn.close()

def search_product_name():   # 상품명 검색 함수 호출
    try:
        conn = pymysql.connect(**config)    # db 연동
        cursor = conn.cursor()              # sql 실행 객체
        # 특정 레코드 조회
        print('\n<<<상품명조회>>>')
        search_name = input('조회할 상품을 입력하세요 : ')
        sql = f"select * from goods where name = '{search_name}'"
        cursor.execute(sql)
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print (f'조회결과는 코드 : {row[0]}, 상품 : {row[1]}, 수량 : {row[2]}, 단가 : {row[3]} 입니다.')
        else:
            print('조회결과 입력한 상품에 맞는 상품이 없습니다.')
    # 에러 처리
    except Exception as e:
        print('db error : ', e)
        conn.rollback() # 실행 취소
    finally:
        cursor.close()
        conn.close()

# main 함수 시작점 지정
if __name__ == "__main__":
    create_table()
    while(1):
        os.system("cls")
        print('==================================상품관리==================================')
        print('상품등록 : 1 | 상품목록조회 : 2 | 코드별조회 : 3 | 상품명조회 : 4 | 종료 : 0')
        print('============================================================================')
        category = int(input("작업을 선택하세요 : "))
        if category == 1:
            add_product()            # 상품 추가 함수 호출 
            os.system("pause")
        elif category == 2:         # 테이블 검색 함수 호출
            search_table()
            os.system("pause")
        elif category == 3:         # 코드별 검색 함수 호출
            search_product_code()
            os.system("pause")
        elif category == 4:         # 상품명 검색 함수 호출
            search_product_name()
            os.system("pause")
        elif category == 0:         # 상품관리 종료 수행
            print('상품관리 종료')
            os.system("pause")
            os.system('cls')
            sys.exit(0)
        else:                       # 카테고리 범주 오류 처리
            print('잘못 선택하셨습니다.')
            os.system("pause")