import sys
sys.path.append("C:/workspace2/ChatBot")
from utils.Preprocess import Preprocess
from models.ner.NerModel import NerModel

p = Preprocess(word2index_dic='./ChatBot/train_tools/dict/chatbot_dict.bin', userdic='./ChatBot/utils/user_dic.txt')

ner = NerModel(model_name='./ChatBot/models/ner/ner_model_02.h5', proprocess=p)
query = "오늘 오전 13시 2분에 우럭회 주문하고 싶어요."
predicts = ner.predict(query)
print(predicts)