#069일차-실습-0-2-보충예제-문제-2-해답
import datetime
from datetime import datetime, date
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('display.notebook_repr_html', True)
pd.set_option('display.max_columns', 7)
pd.set_option('display.max_rows', 10)
pd.set_option('display.width', 250)
# 
from re import match
#
def jumin_chk(jumin) :
    year = 0
    year_st ='평년'
    # print(jumin) #  
    ####====####
    if (int(jumin[7]) == 1 or int(jumin[7]) == 2 ) and (21 <= int(jumin[0:2]) <= 99) :
        year = int(jumin[0:2]) + 1900
    elif (int(jumin[7]) == 3 or int(jumin[7]) == 4) and (0 <= int(jumin[0:2]) <= 20) :
        year = int(jumin[0:2]) + 2000
    elif  21 <= int(jumin[0:2]) <= 99 :
        year = int(jumin[0:2]) + 1900
    else :
        year = int(jumin[0:2]) + 2000
    #--윤년체크 시작
    month = [31,28,31,30,31,30,31,31,30,31,30,31]
    if year % 4 == 0 :
        if year % 100 == 0 :
            if year % 400 == 0:
                year_st = '윤년'
            else:
                year_st = '평년'
        else:
            year_st = '윤년'
    else:
        year_st = '평년'
    #
    if year_st == '평년' :
        month[1] = 28 # 평년에 해당하는 2월의 일 수
    else :
        month[1] = 29 # 윤년에 해당하는 2월의 일 수
    #print(month)
    #--윤년체크 끝
    #
    flag1_txt, flag2_txt, flag3_txt, flag4_txt = '', '', '', ''
    result = match('[0-9]{6}-[1-4][0-9]{6}', jumin)
    if len(jumin[0:]) > 14 :
        flag1 = False  
        flag1_txt = '주민번호 길이오류/'
    else:
        flag1 = True
    #
    if 1 <= int(jumin[2:4]) <= 12 :
        flag2 = True
    else:
        flag2 = False
        flag2_txt = '주민번호 앞자리 월 오류/'
    #
    if len(jumin[7:]) > 7 :
        flag3 = False
        flag3_txt = '주민번호 뒷자리 길이오류/'
    else:
        flag3 = True
    #
    if flag2 == True and year_st == '평년':
        if month[int(jumin[2:4])-1] < int(jumin[4:6]):
            flag4 = False
            flag4_txt = '주민번호 앞자리 월 오류/'
        else:
            flag4 = True
           
    if flag2 == True and year_st == '윤년':
        if month[int(jumin[2:4])-1] < int(jumin[4:6]):
            flag4 = False
            flag4_txt = '주민번호 앞자리 월 오류/'
        else:
            flag4 = True
    #
    # 함수의 역할을 끝내고 리턴할 값을 만듬
    return_txt = ''
    if result and flag1 and flag2 and flag3 and flag4 :
        return jumin+'-->'+ year_st +'이면서','정상적인 주민번호'
    else :
        return_txt += flag1_txt + flag2_txt + flag3_txt + flag4_txt
        return jumin+'-->'+ year_st +'이면서','비정상적인 주민번호 : '+ return_txt
#
jumin_ls = [
    '200229-3234567',
    '190229-4234567',
    '720229-1234567',
    '730229-2234567',
    '190229-5234567',
    '191629-5234567',
    '191229-523456789'
]
#
for i in range(len(jumin_ls)) :
    jumin_out =''
    jumin_out = jumin_chk(jumin_ls[i])  # 200229-3234567 --> 윤년 이면서 정상적인 주민번호
    print(jumin_out)