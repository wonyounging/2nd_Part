import tensorflow as tf
import pandas as pd
from tensorflow.keras.models import Model, load_model
from tensorflow.keras import preprocessing
import random

# 데이터 읽어오기
train_file = "./ChatBot/data/Chatbot_data-master/ChatbotData.csv"
data = pd.read_csv(train_file, delimiter=',', encoding='ansi')
features = data['Q'].tolist()
labels = data['label'].tolist()

# 단어 인덱스 시퀀스 벡터
corpus = [preprocessing.text.text_to_word_sequence(text) for text in features]
tokenizer = preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(corpus)
sequences = tokenizer.texts_to_sequences(corpus)
word_index = tokenizer.word_index

MAX_SEQ_LEN = 15
padded_seqs = preprocessing.sequence.pad_sequences(sequences, maxlen=MAX_SEQ_LEN, padding='post')

# 테스트용 데이터셋 생성
ds = tf.data.Dataset.from_tensor_slices((padded_seqs, labels))
ds = ds.shuffle(len(features))
test_ds = ds.take(2000).batch(20)

# 감정 분류 CNN 모델 불러오기
model_v2 = load_model('./ChatBot/model/cnn_model_v2.h5')
model_v2.summary()
model_v2.evaluate(test_ds, verbose=2)

model_v3 = load_model('./ChatBot/model/cnn_model_v3.h5')
model_v3.summary()
model_v3.evaluate(test_ds, verbose=2)

print('데이터셋의 갯수 : ', len(corpus))
random_int = random.randint(0,11823)
print('테스트용 데이터셋 {}번째'.format(random_int))

# 테스트용 데이터셋의 10212번째 데이터 출력
print("단어 시퀀스 : ", corpus[random_int])
print("단어 인덱스 시퀀스 : ", padded_seqs[random_int])
print("문장 분류(정답) : ", labels[random_int])

# 테스트용 데이터셋의 10212번째 데이터 감정 예측
picks = [random_int]
predict_v2 = model_v2.predict(padded_seqs[picks])
predict_class_v2 = tf.math.argmax(predict_v2, axis=1)
print("v2 감정 예측 점수 : ", predict_v2)
print("v2 감정 예측 클래스 : ", predict_class_v2.numpy())

predict_v3 = model_v3.predict(padded_seqs[picks])
predict_class_v3 = tf.math.argmax(predict_v3, axis=1)
print("v3 감정 예측 점수 : ", predict_v3)
print("v3 감정 예측 클래스 : ", predict_class_v3.numpy())
