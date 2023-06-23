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

        # tb1 테이블 생성
        sql = "create table if not exists tb1(name VARCHAR(20) not null, age integer not null, num integer primary key not null)"
        cursor.execute(sql) # sql문 실행
    # 에러 처리
    except Exception as e:
        print('db error : ', e)
    finally:
        cursor.close()
        conn.close()    
    
# 멤버 추가 함수
def add_member():
    try:
        conn = pymysql.connect(**config)    # db 연동
        cursor = conn.cursor()              # sql 실행 객체

        print('----회원등록----')
        name = input('이름 입력 : ')
        age = int(input('나이 입력 : '))
        num = int(input('번호 입력 : '))
        
        # 번호 중복 확인
        sql = f"select * from tb1 where num = {num}"
        cursor.execute(sql)
        rows = cursor.fetchall()
        if len(rows) > 0:
            print('중복된 번호입니다. 다시 입력해주세요.')
        else:
            sql = f"insert into tb1 values('{name}', {age}, {num})"
            cursor.execute(sql)
            conn.commit()
            print('회원등록을 성공했습니다.')
    # 에러 처리
    except Exception as e:
        print('db error : ', e)
    finally:
        cursor.close()
        conn.close() 

# 테이블 검색 함수
def search_table():
    try:
        conn = pymysql.connect(**config)    # db 연동
        cursor = conn.cursor()              # sql 실행 객체
        # 테이블 조회
        cursor.execute("select * from tb1")
        rows = cursor.fetchall()

        print('----회원목록조회----')
        print('NAME \tAGE \tNUM') # 레코드 출력
        for row in rows:
            print (row[0], '\t', row[1], '\t', row[2])
    # 에러 처리
    except Exception as e:
        print('db error : ', e)
    finally:
        cursor.close()
        conn.close() 

# 멤버 검색 함수
def search_member():
    try:
        conn = pymysql.connect(**config)    # db 연동
        cursor = conn.cursor()              # sql 실행 객체
        # 특정 레코드 조회
        print('----회원개별조회----')
        search_name = input('조회할 이름을 입력하세요 : ')
        sql = f"select * from tb1 where name = '{search_name}'"
        cursor.execute(sql)
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print (f'조회결과는 이름 : {row[0]}, 나이 : {row[1]}, 수량 : {row[2]} 입니다.')
        else:
            print('조회결과 입력한 이름에 맞는 회원이 없습니다.')
    # 에러 처리
    except Exception as e:
        print('db error : ', e)
    finally:
        cursor.close()
        conn.close()

# main 함수 시작점 지정
if __name__ == "__main__":
    create_table()
    while(1):
        os.system("cls")
        print('===========================회원관리===========================')
        print('회원등록 : 1 | 회원목록조회 : 2 | 회원개별조회 : 3 | 종료 : 0')
        print('==============================================================')
        category = int(input("작업을 선택하세요 : "))
        if category == 1:
            add_member()            # 멤버 추가 함수 호출 
            os.system("pause")
        elif category == 2:         # 테이블 검색 함수 호출
            search_table()
            os.system("pause")
        elif category == 3:         # 멤버 검색 함수 호출
            search_member()
            os.system("pause")
        elif category == 0:         # 회원관리 종료 수행
            print('회원관리 종료')
            os.system("pause")
            break
        else:                       # 카테고리 범주 오류 처리
            print('잘못 선택하셨습니다.')
            os.system("pause")