import pymysql
import sys
import os
from datetime import datetime
from re import match

config = {
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '0000',
    'database' : 'test_db',
    'port' : 3306,
    'charset' : 'utf8',
    'use_unicode' : True
}

class Filter():
    def __init__(self):
        pass

    def studID_filter(self):
        s_id = ''
        while(1):
            id_year = int(input("입학년도를 입력하세요.(1900~2023) : "))
            if 1900 <= id_year <= 2023:
                s_id += str(id_year)
                break
            else:
                print("입학년도를 잘못 입력하셨습니다.(1900~2023)")
        while(1):
            id_code = input("학과코드를 입력하세요.(01~99) : ")
            if '00' < id_code < '100':
                s_id += str(id_code)
                break
            else:
                print("학과코드를 잘못 입력하셨습니다.(01~99)")
        while(1):
            id_num = input("순번을 입력하세요.(01~99) : ")
            if '00' < id_num < '100':
                s_id += str(id_num)
                break
            else:
                print("순번을 잘못 입력하셨습니다.(01~99)")
        return(s_id)

    def jumin_filter(self) :
        while(1):
            jumin = input('주민번호를 입력하세요 : ')
            if match('[0-9]{6}-[1-4][0-9]{6}', jumin):      # 조건 1 : 올바른 형식의 주민번호 확인(앞_6, -_1, 뒤_7 / 숫자로만 구성)
                flag1 = True
                print(f"1 조건 {flag1}")
                now = datetime.today()      # 현재 날짜 가져오기
                now_year = now.year         # 현재 년
                now_month = now.month       # 현재 월
                now_day = now.day           # 현재 일
                member_year = 0
                member_year_st ='평년'

                split_jumin = jumin.split('-')
                front_jumin = split_jumin[0]
                rear_jumin = split_jumin[1]
                
                # 조건마다 사용 될 변수
                sex_code = int(rear_jumin[0])
                member_year = int(front_jumin[0:2])
                member_month = int(front_jumin[2:4])
                member_day = int(front_jumin[4:6])
                # print(split_jumin,front_jumin,rear_jumin,sex_code, now_year, now_month, now_day)
                
                # 조건 2, 3 : 앞자리(1,2)와 뒷자리(1)를 이용하여 올바른 연도, 성별 확인
                if (sex_code == 1 or sex_code == 2) and (20 <= member_year <= 99):
                    flag2 = True
                    member_year = member_year+1900
                    print(f"2 조건 {flag2}, 출생연도 : {member_year}({member_year_st})")
                    if sex_code == 1:
                        flag3 = True
                        print(f'3 조건 {flag3}, 성별 : 남')
                    else:
                        flag3 = True
                        print(f'3 조건 {flag3}, 성별 : 여')
                elif (sex_code == 3 or sex_code == 4) and (00 <= member_year <= (now_year%2000)):
                    flag2 = True
                    member_year = member_year+2000
                    print(f"2 조건 {flag2}, 출생연도 : {member_year}({member_year_st})")
                    if sex_code == 3:
                        flag3 = True
                        print(f'3 조건 {flag3}, 성별 : 남')
                    else:
                        flag3 = True
                        print(f'3 조건 {flag3}, 성별 : 여')
                else:
                    flag2 = False
                    flag3 = False
                    print(flag2, "error : 잘못 된 성별")
                
                # 윤년체크
                month = [31,28,31,30,31,30,31,31,30,31,30,31]
                if member_year % 4 == 0 :
                    if member_year % 100 == 0 :
                        if member_year % 400 == 0:
                            member_year_st = '윤년'
                        else:
                            member_year_st = '평년'
                    else:
                        member_year_st = '윤년'
                else:
                    member_year_st = '평년'
                #
                if member_year_st == '평년' :
                    month[1] = 28 # 평년에 해당하는 2월의 일 수
                else :
                    month[1] = 29 # 윤년에 해당하는 2월의 일 수
                # 조건 4 : 올바른 월인지 확인
                if (member_year == now_year) and (member_month > now_month):
                    flag4 = False
                    print(flag4, 'error : 잘못 된 월')
                else:
                    if member_year_st == '평년':
                        if month[member_month-1] < member_day:
                            flag4 = False
                            print(flag4, 'error : 잘못 된 월')
                        else:
                            flag4 = True
                            print(f'4 조건 {flag4}, 출생월 : {member_month}')
                    else:
                        if month[member_month-1] < member_day:
                            flag4 = False
                            print('error : 잘못 된 월')
                        else:
                            flag4 = True
                            print(f'4 조건 {flag4}, 출생월 : {member_month}')

                # 조건 5 : 올바른 일인지 확인
                if (member_year == now_year) and (member_month == now_month) and (member_day > now_day):
                    flag5 = False
                    print(flag5, 'error : 잘못 된 일')
                else:
                    if member_day <= month[int(jumin[2:4])-1]:
                        flag5 = True
                        print(f'5 조건 {flag5}, 출생일 : {member_day}')
                    else:
                        flag5 = False
                        print(flag5, 'error : 잘못 된 일')

                result = flag1&flag2&flag3&flag4&flag5  # 하나라도 만족하지 못하면 False

            else:
                flag1 = False  
                print(flag1, "error : 주민번호 형식 오류('-'포함 14자)")
            if result == True:
                break
            return(jumin)


class Stud():
    def __init__(self):
        pass

    def insert_stud(self):      # 입력기능 메서드
        os.system("cls")
        try:
            conn = pymysql.connect(**config)
            cursor = conn.cursor()

            print("===================학생 추가 입력==================")

            in_id = Filter.studID_filter(self)
            in_name = input('이름을 입력하세요 : ')
            in_jumin = Filter.jumin_filter(self)
            in_front_juminin = in_jumin.split('-')[0]
            in_rear_juminin = in_jumin.split('-')[1]
            in_addr_si = input('주소(시)를 입력하세요 : ')
            in_addr_gu = input('주소(구)를 입력하세요 : ')
            sql = f"insert into stud (studID, name, jumin1, jumin2, addr1, addr2) values('{in_id}','{in_name}','{in_front_juminin}','{in_rear_juminin}','{in_addr_si}','{in_addr_gu}')"
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
            re_chk = input("정말로 수정하시겠습니까?(Y/N) : ")
            if re_chk.upper() == "Y":
                up_name = input("이름을 입력하세요 : ")
                up_jumin = Filter.jumin_filter(self)
                up_front_jumin = up_jumin.split('-')[0]
                up_rear_juminin = up_jumin.split('-')[1]
                up_addr_si = input('주소(시)를 입력하세요 : ')
                up_addr_gu = input('주소(구)를 입력하세요 : ')
                # if re_chk.upper() == "Y":
                sql = f"update stud set studID = '{self.in_id}', name = '{up_name}', jumin1 = '{up_front_jumin}', jumin2 = '{up_rear_juminin}', addr1 = '{up_addr_si}', addr2 = '{up_addr_gu}' where studID = {self.in_id};"
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
            re_chk = input("정말로 삭제하시겠습니까?(Y/N) : ")
            if re_chk.upper() == "Y":
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

if __name__ == "__main__":        
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