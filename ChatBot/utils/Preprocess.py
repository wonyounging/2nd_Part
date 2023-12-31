from konlpy.tag import Komoran
import pickle

class Preprocess:
    def __init__(self, word2index_dic='', userdic=None):   # 생성자
        # 단어 인덱스 사전 불러오기
        if(word2index_dic != ''):
            f = open(word2index_dic, 'rb')
            self.word_index = pickle.load(f)
            f.close()
        else:
            self.word_index = None
        
        
        # 형태소 분석기 초기화
        self.komoran = Komoran(userdic=userdic)

        # 제외할 품사
        # 관계언, 기호, 어미, 접미사 제거
        self.exclusion_tags = [
            'JKS', 'JKC', 'JKG', 'JKO', 'JKB', 'JKV', 'JKQ', 'JX', 'JC',
            'SF', 'SP', 'SS', 'SE', 'SO',
            'EP', 'EF', 'EC', 'ETN', 'ETM',
            'XSN', 'XSV', 'XSA'
        ]

    def pos(self, sentence):    # 형태소 분석기 POS 태거
        return(self.komoran.pos(sentence))
    
    def get_keywords(self, pos, without_tag=False):  # 불용어 제거 후 필요한 품사 정보만 가져오기
        f = lambda x: x in self.exclusion_tags
        word_list = []
        for p in pos:
            if f(p[1]) is False:
                word_list.append(p if without_tag is False else p[0])
        return word_list

    def get_wordidx_sequence(self, keywords):
        if self.word_index is None:
            return []
        w2i = []
        for word in keywords:
            try:
                w2i.append(self.word_index[word])
            except KeyError:
                # 해당 단어가 사전에 없는 경우 OOV 처리
                w2i.append(self.word_index['OOV'])
        return w2i