import sys
sys.path.append("C:/workspace2/ChatBot")
from utils.Preprocess import Preprocess

# sent = "내일 오전 10시에 탕수육 주문하고 싶어"
sent1 = "내일 오전 10시에 짬뽕 주문하고 싶어ㅋㅋ"
sent2 = "내일 오전 19시에 간짜장 주문할 수 있을까요"
sent3 = "내일 오후 23시에 깐풍기 주문할 수 있을까요"
sent4 = "내일 오후 24시에 우라회 주문할 수 있을까요"
sent5 = "내일 오후 25시에 우라늄회 주문할 수 있을까요"
sent = []
sent.extend([sent1, sent2, sent3, sent4, sent5])
# print(sent)
# 전처리 객체 생성
p = Preprocess(userdic='./ChatBot/utils/user_dic.txt')

for i in range(5):
    # 형태소 분석기 실행
    print(f'{i+1}번째 문장 실행결과')
    pos = p.pos(sent[i])
    print(pos)

    # 품사 태그와 같이 키워드 출력
    ret = p.get_keywords(pos, without_tag=False)
    print(ret)

    # 품사 태그 없이 키워드 출력
    ret = p.get_keywords(pos, without_tag=True)
    print(ret)
    print('='*200+'\n')