import os
import sys
import re
from re import search, findall, match, sub
#
class change():
    def __init__(self, func, new_menu):
        self.func = func
        self.new_menu = new_menu

    def save_filter(self):
        chk = input('기존의 파일(corpus)에 덮어쓰시겠습니까?(Y/N) : ')
        chk = chk.upper()
        
        if chk == "Y":
            if self.func == 'corpus':
                new_name = 'corpus'
            elif self.func == 'user_dic':
                new_name = 'user_dic'
            else:
                new_name = 'ner_train'
        else:
            new_name = input("저장할 corpus 파일명 입력 : ")
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
                print('ner_train 기능')
                origin = open('./ChatBot/models/ner/ner_train.txt', mode= 'r', encoding = 'UTF8')
                copy = origin.readlines()
                num =0 
                for i in copy :
                    print(i)
                    if num > 3 :
                        break
                    if not(search(';', i)) and search('짜장면', i):   # search 는 문자열의 중간에 '짜장면'이 위치할 때도 성공함 
                        num +=1
                        new_line = i.replace('짜장면', self.new_menu)
                        print(i)
                        # copy.append(new_line)
                    else:
                        pass
                print(num)
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
        print('corpus 추가 : 1 | user_dic 추가 : 2 | ner_train 추가 : 3 | 종료 : 0')
        category = int(input('기능 선택 : '))
        if category == 1:
            os.system('cls')
            print('=========== corpus 기능 ===========')
            new_menu = input("새로운 메뉴 입력 : ")
            ch = change('corpus', new_menu)
            ch.chage_file()
        elif category == 2:
            os.system('cls')
            print('=========== user_dic 기능 ===========')
            new_menu = input("새로운 메뉴 입력 : ")
            ch = change('user_dic', new_menu)
            ch.chage_file()
        elif category == 3:
            os.system('cls')
            print('=========== ner_train 기능 ===========')
            new_menu = input("새로운 메뉴 입력 : ")
            ch = change('ner_train', new_menu)
            ch.chage_file()
        elif category == 0:
            print('종료')
            os.system('pause')
            sys.exit(0)
        else:
            print('올바른 기능을 선택해주세요.')
            os.system('pause')