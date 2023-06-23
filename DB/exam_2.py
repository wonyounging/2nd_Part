import pymysql
import sys
import os

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '0000',
    'database' : 'test_db',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True
}
class Stud():
    def __init__(self):
        pass

    def insert_stud(self):      # 입력기능 메서드
        os.system("cls")
        try:
            conn = pymysql.connect(**config)
            cursor = conn.cursor()

            print("===================학생 추가 입력==================")
            # in_id = input('{추가} 학번을 입력하세요 : ')
            in_id = input('학번을 입력하세요 : ')
            in_name = input('이름을 입력하세요 : ')
            in_jumin1 = input('주민(앞)을 입력하세요 : ')
            in_jumin2 = input('주민(앞)을 입력하세요 : ')
            in_addr1 = input('주소(시)를 입력하세요 : ')
            in_addr2 = input('주소(구)를 입력하세요 : ')
            sql = f"insert into stud (studID, name, jumin1, jumin2, addr1, addr2) values('{in_id}','{in_name}','{in_jumin1}','{in_jumin2}','{in_addr1}','{in_addr2}')"
            cursor.execute(sql)
            conn.commit()
            print("학생등록을 성공했습니다.")

        except Exception as e:
            print('db error : ', e)
        finally:
            cursor.close()
            conn.close()

    def search_stud(self):      # 조회기능 메서드
        os.system("cls")
        try:
            conn = pymysql.connect(**config)
            cursor = conn.cursor()

            print("===================학생 목록 조회==================")
            # in_id = input('{조회} 학번을 입력해주세요 : ')
            self.in_id = input('조회 학번을 입력해주세요 : ')
            sql = f"select * from stud where studID = {self.in_id}"
            cursor.execute(sql)
            rows = cursor.fetchall()
            
            print("\n=================학생 목록 조회 결과===============")
            if len(rows) > 0:
                print('학번\t 이름\t 주민(앞)  주민(뒤)  주소(시)  주소(구)') # 레코드 출력
                for row in rows:
                    print (f"{row[0]} {row[1]}  {row[2]}    {row[3]}   {row[4]}    {row[5]}")
            else:
                print("학번에 해당하는 학생이 없습니다.")
        except Exception as e:
            print('db error : ', e)
        finally:
            cursor.close()
            conn.close()

    def update_stud(self):      # 수정기능 메서드
        os.system("cls")
        try :
            conn = pymysql.connect(**config)    
            cursor = conn.cursor()
            self.search_stud()
            print("\n=====================학생 수정====================")
            del_chk = input("정말로 수정하시겠습니까?(Y/N) : ")
            if del_chk.upper() == "Y":
                up_name = input("이름을 입력하세요 : ")
                up_jumin1 = input('주민(앞)을 입력하세요 : ')
                up_jumin2 = input('주민(앞)을 입력하세요 : ')
                up_addr1 = input('주소(시)를 입력하세요 : ')
                up_addr2 = input('주소(구)를 입력하세요 : ')
                if del_chk.upper() == "Y":
                    sql = f"update stud set studID = '{self.in_id}', name = '{up_name}', jumin1 = '{up_jumin1}', jumin2 = '{up_jumin2}', addr1 = '{up_addr1}', addr2 = '{up_addr2}' where studID = {self.in_id};"
                    cursor.execute(sql) # sql문 실행
                    conn.commit()
                    print('수정을 완료했습니다.')
            else:
                print("수정를 취소했습니다.")
        except Exception as e :
            print('db 연동 실패 : ', e)
            conn.rollback() # 실행 취소
        finally:
            cursor.close()
            conn.close()
    
    def delete_stud(self):      # 삭제기능 메서드
        os.system("cls")
        try :
            conn = pymysql.connect(**config)    
            cursor = conn.cursor()
            self.search_stud()
            print("\n=====================학생 삭제====================")
            del_chk = input("정말로 삭제하시겠습니까?(Y/N) : ")
            if del_chk.upper() == "Y":
                sql = f"select * from stud where studID = {self.in_id}"
                cursor.execute(sql) # sql문 실행
                rows = cursor.fetchall()
                if rows :
                    sql = f"delete from stud where studID = {self.in_id}"
                    cursor.execute(sql) # sql문 실행
                    conn.commit()
                    print('삭제 성공했습니다.')
                else :
                    print('삭제 실패했습니다.')
            else:
                print("삭제를 취소했습니다.")
        except Exception as e :
            print('db 연동 실패 : ', e)
            conn.rollback() # 실행 취소
        finally:
            cursor.close()
            conn.close()
        
while(1):
    os.system("cls")
    print("===================학생 관리 시스템=================")
    print("입력 : 1 | 조회 : 2 | 수정 : 3 | 삭제 : 4 | 종료 : 0")
    category = int(input('실행할 기능을 입력해주세요 : '))
    if category == 1 :  # 입력
        s1 = Stud()
        s1.insert_stud()
        os.system("pause")
    elif category == 2 :    #조회
        s2 = Stud()
        s2.search_stud()
        os.system("pause")
    elif category == 3 :    # 수정
        s3 = Stud()
        s3.update_stud()
        os.system("pause")
    elif category == 4:     # 삭제
        s4 = Stud()
        s4.delete_stud()
        os.system("pause")
    elif category == 0:
        print("학생관리를 종료합니다. ")
        os.system("pause")
        os.system('cls')
        sys.exit(0)
    else:
        print("잘못입력했습니다.")
        os.system("pause")