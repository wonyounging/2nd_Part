import sqlite3

try:
    # (1) db 연동 객체
    conn = sqlite3.connect("./workspace_SQLite3/data/sqlite2_db.db") # db 생성 -> 연결

    # (2) sql 실행 객체
    cursor = conn.cursor()

    # (3) table 생성
    sql='create table if not exists item(code integer primary key, name text(30) unique not null, qty integer default 0, unit_price real default 0.0)'
    cursor.execute(sql) # sql문 실행
    
    # # (4) 레코드 추가
    # cursor.execute("insert into item values(1, '선풍기', 1, 150)")
    # cursor.execute("insert into item values(2, '에어콘', 1, 200)")
    # cursor.execute("insert into item values(3, '충전기', 1, 100)")
    # cursor.execute("insert into item values(4, '키보드', 1, 70)")
    # cursor.execute("insert into item values(5, '마우스', 1, 60)")
    # conn.commit() # db 반영

    # (4) 레코드 추가_2차
    while(1):
        print('=====상품 등록 중지 음수 코드 입력=====')
        code = int(input('상품코드 입력 : '))
        if code < 0:
            print('상품 등록 중지')
            break
        
        sql = f"select * from item where code = {code}"
        cursor.execute(sql)
        rows = cursor.fetchall()

        if len(rows) > 0:   # 코드번호 중복 확인
            print('중복된 코드입니다. 다시 입력해주세요.')
            continue
        else:
            name = input('상품명 입력 : ')
            su = int(input('수량 입력 : '))
            dan = int(input('단가 입력 : '))
            sql = f"insert into item values({code}, '{name}', {su}, {dan})"
            cursor.execute(sql)
            print('상품등록을 성공했습니다.')
            conn.commit()
    
    # (5) 레코드 조회
    cursor.execute("select * from item")
    rows = cursor.fetchall() # 조회 레코드 가져오기

    print('code \tname \t\tqty \tunit_price') # 레코드 출력
    for row in rows:
        print (row[0], '\t', row[1], '\t', row[2],'\t', row[3])

    # (6) 상품명 조회
    while(1):
        print('=====상품 조회 중지 음수 코드 입력=====')
        code = int(input("조회할 코드를 입력하세요 : "))
        if code < 0:
            print('상품 조회 중지')
            break
        sql = f"select * from item where code like '%{code}%'"
        cursor.execute(sql) # 조회
        rows = cursor.fetchall()

        if rows: # null = false
            for row in rows:
                print (f'조회결과는 코드 : {row[0]}, 제품명 : {row[1]}, 수량 : {row[2]},  단가 : {int(row[3])}입니다.')
        else:
            print('조회결과 입력한 코드에 맞는 상품이 없습니다.')
        
except Exception as e:
    print('db 연동 error : ', e)
    conn.rollback()
    
finally:
    cursor.close()
    conn.close()