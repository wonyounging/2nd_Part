import sys
sys.path.append("C:/workspace2/ChatBot")
from utils.Preprocess import Preprocess
from models.intent.IntentModel import IntentModel

p = Preprocess(word2index_dic='./ChatBot/train_tools/dict/chatbot_dict.bin', userdic='./ChatBot/utils/user_dic.txt')

intent = IntentModel(model_name='./ChatBot/models/intent/intent_model.h5', proprocess=p)

query = "오늘 오후 6시에 김밥 주문이요."
predict = intent.predict_class(query)
predict_label = intent.labels[predict]

print(query)
print("의도 예측 클래스 : ", predict)
print("의도 예측 레이블 : ", predict_label)