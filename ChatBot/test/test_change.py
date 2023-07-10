import os
import sys
import re
from re import search, findall, match, sub
#
class Change():
    def __init__(self, func, new_menu):
        self.func = func
        self.new_menu = new_menu

    def save_filter(self):
        chk = input(f'기존의 파일({self.func})에 덮어쓰시겠습니까?(Y/N) : ')
        chk = chk.upper()
        
        if chk == "Y":
            if self.func == 'corpus':
                new_name = 'corpus'
            elif self.func == 'user_dic':
                new_name = 'user_dic'
            else:
                new_name = 'ner_train'
        else:
            new_name = input(f"저장할 {self.func} 파일명 입력 : ")
        return new_name

    def chage_file(self):
        # corpus 추가
        if self.func == 'corpus':
            try :
                origin = open('./ChatBot/train_tools/dict/corpus.txt', mode= 'r', encoding = 'UTF8')
                copy = origin.readlines()
                num =0
                for i in copy :
                    if num > len(copy) :
                        break
                    if not(search(';', i)) and search('짜장면', i):   # search 는 문자열의 중간에 '짜장면'이 위치할 때도 성공함 
                        num +=1
                        new_line = i.replace('짜장면', self.new_menu)
                        copy.append(new_line)
                    else:
                        pass

            except Exception as e :
                print("오류 발생 : ",e)

            finally :
                origin.close()
                new_name = self.save_filter()          
                new_f = open('./ChatBot/train_tools/dict/{}.txt'.format(new_name), mode= 'w', encoding = 'UTF8')
                new_f.writelines(copy)
                new_f.close()

        # user_dic 추가
        elif self.func == 'user_dic':
            try:
                origin = open('./ChatBot/utils/user_dic.txt', mode= 'r', encoding = 'UTF8')
                copy = origin.readlines()
                user_dic_struct = '{}\tNNG\n'.format(self.new_menu)   # user_dic의 내용 형식
                copy.append(user_dic_struct)

            except Exception as e :
                print("오류 발생 : ",e)

            finally :
                origin.close()
                new_name = self.save_filter()             
                new_f = open('./ChatBot/utils/{}.txt'.format(new_name), mode= 'w', encoding = 'UTF8')
                new_f.writelines(copy)
                new_f.close()

        # ner_train 추가
        elif self.func == 'ner_train':
            try:
                origin = open('./ChatBot/models/ner/ner_train.txt', mode= 'r', encoding = 'UTF8')
                copy = origin.readlines()

                temp_result = []    # ;과 ;사이의 데이터 묶음들이 저장될 임시 리스트
                temp_group = []     # ;과 ;사이의 데이터들이 누적되어 저장될 임시 리스트
                # ;으로 시작하고 다음 ;이 나오기 전끼리 묶음
                for line in copy:
                    if line.startswith(';'):
                        if temp_group:
                            temp_result.append(temp_group)
                        temp_group = [line]
                    else:
                        temp_group.append(line)

                use_data = []       # 특정 단어만이 포함된 묶음들만 들어갈 임시 리스트
                # ;으로 분리된 데이터에서 짜장면이 포함된 데이터만 추출
                for i in temp_result:
                    flag = 'F'
                    for j in i:
                        if "짜장면" in j:
                            flag = 'T'
                    if flag == 'T':
                        use_data.append(i)  # 짜장면이라는 단어가 들어가있는 묶음이 append

                new_data = []   # 사용자가 입력한 음식명으로 변경될 임시 리스트
                add_data = []   # 변경된 데이터들이 기존의 copy에 extend될 리스트
                # 짜장면이 포함된 데이터에서 짜장면을 사용자가 입력한 메뉴로 변경
                for i in use_data:
                    for j in i:
                        new_data = j.replace('짜장면', self.new_menu)
                        add_data.append(new_data)
                add_data.pop()
                copy.append('\n')
                copy.extend(add_data)

            except Exception as e :
                print("오류 발생 : ",e)

            finally :
                origin.close()
                new_name = self.save_filter()             
                new_f = open('./ChatBot/models/ner/{}.txt'.format(new_name), mode= 'w', encoding = 'UTF8')
                new_f.writelines(copy)
                new_f.close()

        else:
            print('else')

if __name__ == "__main__":
    os.system('cls')
    while(1):
        os.system('cls')
        print('corpus 추가 : 1 | user_dic 추가 : 2 | ner_train 추가 : 3 | 통합 추가 : 4 | 종료 : 0')
        category = int(input('기능 선택 : '))
        if category == 1:
            os.system('cls')
            print('=========== corpus 기능 ===========')
            new_menu = input("새로운 메뉴 입력 : ")
            ch = Change('corpus', new_menu)
            ch.chage_file()
            os.system('pause')
        elif category == 2:
            os.system('cls')
            print('=========== user_dic 기능 ===========')
            new_menu = input("새로운 메뉴 입력 : ")
            ch = Change('user_dic', new_menu)
            ch.chage_file()
            os.system('pause')
        elif category == 3:
            os.system('cls')
            print('=========== ner_train 기능 ===========')
            new_menu = input("새로운 메뉴 입력 : ")
            ch = Change('ner_train', new_menu)
            ch.chage_file()
            os.system('pause')
        elif category == 4:
            os.system('cls')
            print('=========== 통합 기능 ===========')
            new_menu = input("새로운 메뉴 입력 : ")
            ch_c = Change('corpus', new_menu)
            ch_c.chage_file()
            ch_u = Change('user_dic', new_menu)
            ch_u.chage_file()
            ch_n = Change('ner_train', new_menu)
            ch_n.chage_file()
            os.system('pause')
        elif category == 0:
            print('종료')
            os.system('pause')
            sys.exit(0)
        else:
            print('올바른 기능을 선택해주세요.')
            os.system('pause')