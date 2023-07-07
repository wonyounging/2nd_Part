import re
from re import search, findall, match, sub
#
origin = open('./ChatBot/models/ner/ner_train.txt', mode= 'r', encoding = 'UTF8') # 'ccc.txt'는 corpus.txt 파일의 복제품임
copy = origin.readlines()                              # 읽어서 txt2리스트로 생성 

# 사용자로부터 새로운 메뉴를 입력 받음
new_menu = input('신메뉴 입력 : ')

result = []
current_group = []
# ;으로 시작하고 다음 ;이 나오기 전끼리 묶음
for line in copy:
    # line = line.strip()
    if line.startswith(';'):
        if current_group:
            result.append(current_group)
        current_group = [line]
    else:
        current_group.append(line)
# print(len(result))
# print(result)
# print(result[0])

use_data = []
# ;으로 분리된 데이터에서 짜장면이 포함된 데이터만 추출
for i in result:
    flag = 'F'
    # print(i)
    # print('='*100)
    for j in i:
        # print('*'*10)
        if "짜장면" in j:
            # print(j)
            # print(i)
            flag = 'T'
            # use_data.append(i)
            # print('='*100)
    if flag == 'T':
        use_data.append(i)

# print('*'*100)
# print(use_data)

new_data = []
add_data = []
# 짜장면이 포함된 데이터에서 짜장면을 사용자가 입력한 메뉴로 변경
for i in use_data:
    # print('~'*100)
    # print(i)
    for j in i:
        new_data = j.replace('짜장면', new_menu)
        add_data.append(new_data)
print(add_data)
# print(type(add_data))    @
add_data.pop()
copy.append('\n')
copy.extend(add_data)
####
print('='*100)


# new_f = open('./ChatBot/models/ner/tttttttt.txt', mode= 'w', encoding = 'UTF8')
# new_f.writelines(copy)
# new_f.close()
