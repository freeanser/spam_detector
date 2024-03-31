# # app.py

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def home():
    return render_template('home_with_chat.html')  # 修改為包含聊天框的 HTML

@app.route('/predict', methods=['POST'])
def predict():


    # 從名為'spam.csv'的CSV文件讀取數據，使用Pandas庫將其轉換為數據框（DataFrame）
    df = pd.read_csv('spam.csv', encoding="latin-1")

    # 從數據框中選擇只包含 'v1' 和 'v2' 列的子集
    df = df[['v1', 'v2']]

    # 將 'v2' 列的名稱更改為 'message'
    df.rename(columns={'v2': 'message'}, inplace=True)

    # 創建一個新的列 'label'，將 'v1' 列中的標籤 'ham' 映射為 0，'spam' 映射為 1
    df['label'] = df['v1'].map({'ham': 0, 'spam': 1})
    
    # 分別將 'message' 列指定給 X（特徵變量）和 'label' 列指定給 y（目標變量）
    X = df['message']
    y = df['label']

    # 使用 Scikit-Learn 的 CountVectorizer 將文本數據轉換為詞袋模型（向量表示）
    cv = CountVectorizer()
    X = cv.fit_transform(X)

    # 使用 train_test_split 函數將數據集分為訓練集和測試集
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # 使用 Scikit-Learn 的 Multinomial Naive Bayes 分類器 clf，並使用訓練集進行模型訓練。
    clf = MultinomialNB()
    clf.fit(X_train, y_train)

    if request.method == 'POST':
        message = request.form['message']
        data = [message]

        # 將用戶輸入的消息轉換為機器學習模型可以理解的格式，使用先前創建的CountVectorizer。
        vect = cv.transform(data).toarray()

        # 使用訓練好的Multinomial Naive Bayes模型進行預測，得到預測結果。
        my_prediction = clf.predict(vect)

        # 使用SocketIO發送預測結果給客戶端
        socketio.emit('response', {'prediction': int(my_prediction[0])})  

        return jsonify({'prediction': int(my_prediction[0])})

# 新增 Socket.IO 事件處理函數
@socketio.on('user_prediction')
def handle_user_prediction(data):
    prediction = data['prediction']
    message = data['message']
    # 在這裡處理用戶的預測，你可以將結果發送給所有連接的客戶端，例如：
    socketio.emit('broadcast_result', {'prediction': prediction, 'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
