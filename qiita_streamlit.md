
# streamlit app を初めて開発・公開した件
### 

### 1. streamlitとは
StreamlitはPythonのウェブアプリケーションを構築するためのフレームワークの一つです。
Pythonのコード内に直接書かれたコマンドでウェブアプリケーションを構築するため、HTMLやCSSなどのファイルを扱う必要がありません。
さらに、作ったアプリをStreamlit Sharingと呼ばれるサービスを介して、無料でデプロイ・公開できるのが大きな魅力です。

### 2. プロジェクトの目的:
以前、kaggleのtarotカードのデータを用いてpythonで作成していた占いゲームを、Streamlit用に焼き直すことにした。
内容は、3枚のカードをランダムに選び、カードとカードの意味する内容を表示するという、単純なものです。

https://www.kaggle.com/code/stpeteishii/tarot-reading

### 3. 開発過程:
まずはlocalで開発して動作確認まで行いました。

python -m venv .venv
source .venv/bin/activate
pip install streamlit

フォルダ内は
app.py
requirements.txt
data類
.venvホルダ

ターミナルで以下を起動しlocalhostで動作確認。
streamlit run app.py

スクリプトを.venvと共にgithubにpushする。

Streamlit Community Cloud アカウントを作成後、
Streamlit Sharingにgithubの該当リポジトリを登録して、本番環境で動作を確認します。
しかし、ここでエラーが発生します。localでは動いたのに、、、、、、

AttributeError: module 'cv2.dnn' has no attribute 'DictValue' のエラーが発生しています。

これがなかなか解決しないので、原因を理解しないまま、元コードについて、cv2でなくPILを使うことにして、pushやり直し。
PILを使ったコードではlocal,本番完環境共に問題は起きませんでした。

### 4. コードの解説:

```
import streamlit as st
import pandas as pd
import os
import random
from PIL import Image

data_dir = './cards'
files = os.listdir(data_dir)
data = pd.read_json('./tarot-images.json', orient='records')
data = pd.json_normalize(data['cards'])
data1 = data[['name', 'img', 'fortune_telling']][data['arcana'] == 'Major Arcana']

def predict():
    rand3 = random.sample(range(22), k=3)
    fortune = []
    name = []
    file = []
    for i in rand3:
        fortune.append(data1.loc[i, 'fortune_telling'][0])
        name.append(data1.loc[i, 'name'])
        file.append(data1.loc[i, 'img'])
    times = ['Past', 'Present', 'Future']
    images = []
    for i in range(3):
        img = Image.open(os.path.join(data_dir, file[i]))
        images.append(img)
    return times, fortune, name, images

st.title("Tarot Reading!")

if st.button("Predict Your Fortune"):
    times, fortune, name, images = predict()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(images[0], caption=name[0], use_column_width=True)
        st.write(f'Your {times[0]} is {name[0]}.')
        st.write(f'{fortune[0]}.')
    with col2:
        st.image(images[1], caption=name[1], use_column_width=True)
        st.write(f'Your {times[1]} is {name[1]}.')
        st.write(f'{fortune[1]}.')
    with col3:
        st.image(images[2], caption=name[2], use_column_width=True)
        st.write(f'Your {times[2]} is {name[2]}.')
        st.write(f'{fortune[2]}.')

```

### 5. デモやデモ動画:
https://app-tarrot-reading-mlnessbppgllzg2dns5pfc.streamlit.app/
https://github.com/tztechno/streamlit-tarrot-reading/tree/master

### 6. 今後の展望:
機械学習でトレーニング済みのモデルを使ったアプリも作ってみたいです。
cv2は使う場面は多くありそうなので、解決方法は見つけておく必要がありますね。

### 7. 参考文献やリソース:
https://streamlit.io/
https://docs.streamlit.io/
https://share.streamlit.io/

