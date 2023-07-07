# corpus.txt에 추가메뉴(촐랭이밥 등의 기존에 없는 메뉴)로 구성된 문장 생성하기-1단계(미완성임)
'''
코드 설명1 :
이 코드는 corpus.txt에 파일 안에 존재하지 않는 새로운 메뉴를 포함하는 말뭉치 요소를
추가하기 위한 작업 파이프 라인 중에 한 부분입니다
교재에는 언급되어 있지 않지만 현업에서는 데이터 맹글링 과정에서 많이 사용하는 로직입니다
'''
import re
from re import search, findall, match, sub
#
try :
    txt1 = open('./ChatBot/train_tools/dict/corpus.txt', mode= 'r', encoding = 'UTF8') # 'ccc.txt'는 corpus.txt 파일의 복제품임
    txt2 = txt1.readlines()                              # 읽어서 txt2리스트로 생성 
    print(len(txt2))   # 길이확인 
    print(type(txt2))  # 속성확인 
    
    new_menu = input("새로운 메뉴 입력 : ")
    num =0
    for i in txt2 :
        if num > len(txt2) :
            break
        #print(re.match('짜장면', i))   # match 는 문자열의 처음에 '짜장면'이 위치할 때만 성공함 
        if not(search(';', i)) and search('짜장면', i):   # search 는 문자열의 중간에 '짜장면'이 위치할 때도 성공함 
            num +=1
            print(i)

            new_line = i.replace('짜장면', new_menu)
            txt2.append(new_line)
            print(new_line)
        else:
            pass
    print('num-->',num)
    print(len(txt2))
    print(type(txt2))
    #
    '''
    코드설명-2 :
    위의 코드를 실행하면
    0000    짜장면 주문 하고싶어요         2
    0000    짜장면 먹고싶어요               2
    ...
    ...
    0000    ;11시 6분 짜장면 지금 음식 받 을 수 있 나요     0
    0000    ;18시 36분 짜장면 하 ㄹ 수 있 을까요 ?  0
    num--> 766
    와 같은 결과가 도출됨
    '''
    '''
    코드설명-3 : 
    이후 기술된 내용은 084일차-실습-2의 <문제> 및 <요구사항>입니다.
    이 코드를 받은 학습자가 개인적으로
    완성해야 할 작업 파이프라인은 다음과 같습니다.
    가. 도출된 766라인의 말뭉치 라인들 중에 ;로 시작하는 라인을 인정할지 여부를 결정하여야 함
    나. 가.에서 결정된 라인들을 각 라인별로 '짜장면'을 신규 메뉴명인 '촐랭이밥'으로 변경하여
         input01.txt파일로 생성함
    다. 나.에서 생성된 input01.txt 파일을 corpus.txt에 append 시킴,
        이 과정에서 append되는 corpus.txt를 기존의 파일과 구별되게 corpus02.txt로 명명할것
    라. corpus02.txt을 입력으로 해서 모델을 만들 때 신규 메뉴명이 올바르게 처리되는지 분석할것
    '''
    '''
    코드설명-4 :
    이후 기술된 내용은 084일차-실습-3의 <문제> 및 <요구사항>입니다.
    코드설명-2이후에 계속해야 할 작업 파이프라인은 다음과 같습니다.
    코드설명-3까지 완성한 로직을 다른 user_dic.tsv 파일이나 ner_train.txt파일의 내용을
    보완하는 것으로 응용하세요.
    '''
except Exception as e :
    print("오류 발생 : ",e)
finally :
    txt1.close()
    # 쓰기모드로 열어서 추가된 내용 저장
    new_f = open('./ChatBot/train_tools/dict/corpus02.txt', mode= 'w', encoding = 'UTF8')
    new_f.writelines(txt2)
    new_f.close()