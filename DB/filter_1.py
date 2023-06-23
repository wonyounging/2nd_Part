#069일차-실습-0-2-보충예제-문제-1-해답
import datetime
from datetime import datetime, date
from re import findall, match, sub
#jumin = '202229-3234567'
jumin = input('주민등록번호를 입력하세요(하이픈 포함)')
print('입력한 주민등록번호는 : ', jumin, '입니다')
flag = {}
if int(jumin[7]) == 1 or int(jumin[7]) == 2: year = int(jumin[0:2]) + 1900
if int(jumin[7]) == 3 or int(jumin[7]) == 4: year = int(jumin[0:2]) + 2000
#
if year % 4 ==0 :
    if year % 100 == 0 :
        if year % 400 == 0:
            year = '윤년'
            month = [31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            year = '평년'
            month = [31,28,31,30,31,30,31,31,30,31,30,31]
    else:
        year = '윤년'
        month = [31,29,31,30,31,30,31,31,30,31,30,31]
else:
    year = '평년'
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
   
#
result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
if len(jumin[0:]) > 14 :
    flag['flag1'] = '년도의 자리수 또는 뒷자리의 첫 숫자오류'
    flag1 = False
else:
    flag['flag1'] = '*'
    flag1 = True
#
if 1 <= int(jumin[2:4]) <= 12 :  # 월의 숫자를 필터링
    flag['flag2'] = '*'
    flag2 = True
else:
    flag['flag2'] = '앞자리의 월 오류'
    flag2 = False
#
if len(jumin[7:]) > 7 :
    flag['flag3'] = '뒷자리의 글자수 오류'
    flag3 = False
else:
    flag['flag3'] = '*'
    flag3 = True
#
 
if 1 <= int(jumin[4:6]) <= month[(int(jumin[2:4]))-1] :  # 일의 숫자가 1 이상이면서 month 리스트의 해당 인덱스 요소의 숫자 이하인지 필터링
    flag['flag4'] = '*'
    flag4 = True
else:
    flag4 = False
    flag['flag4'] = '앞자리중 월에 대한 일자 오류'
#
 
###
if result and flag1 and flag2 and flag3 and flag4 and flag4 :
    print('****주민번호 필터링 성공 ')
else :
    print('잘못된 주민번호')
    print('flag[flag1] : ', flag['flag1'])
    print('flag[flag2] : ', flag['flag2'])
    print('flag[flag3] : ', flag['flag3'])
    print('flag[flag4] : ', flag['flag4'])