# KeyBert
### 


---


KeyBERTで使えるモデルは、以下の2種類があります。

### BERT
### RoBERTa

BERTは、Google AIによって開発された事前学習済み言語モデルです。自然言語処理タスク全般で高い性能を発揮することが知られており、KeyBERTでもデフォルトのモデルとして採用されています。

RoBERTaは、Facebook AI Researchによって開発された事前学習済み言語モデルです。BERTと同様に、自然言語処理タスク全般で高い性能を発揮することが知られています。RoBERTaは、BERTよりも長い文章を処理することができ、KeyBERTでは、長い文章を扱う場合に有効です。

どちらのモデルを使うかは、処理する文章の長さや、求められる精度によって異なります。

以下は、各モデルの特徴と、KeyBERTでの使用例です。

### BERT

特徴: 自然言語処理タスク全般で高い性能を発揮する。
使用例: 短い文章の要約、質問応答、文書分類など。

### RoBERTa

特徴: BERTよりも長い文章を処理することができる。
使用例: 長い文書の要約、質問応答、文書分類など。
KeyBERTでモデルを選択するには、以下のコマンドを使用します。

```
from keybert import KeyBERT

# BERTモデルを使用する
model = KeyBERT(model_name="bert-base-uncased")

# RoBERTaモデルを使用する
model = KeyBERT(model_name="roberta-base-uncased")
モデルを選択したら、以下のコマンドを使用して、文書のキーワードを抽出することができます。

documents = ["文書1", "文書2", ...]

keywords = model.extract_keywords(documents, top_n=10)

for document, keywords in keywords.items():
    print(f"文書: {document}")
    for keyword, score in keywords:
        print(f"  - {keyword}: {score}")

```

上記のコードを実行すると、各文書のトップ10のキーワードとそのスコアが表示されます。

### KeyBERTでモデルを選択する際のヒント

処理する文章の長さ: 短い文章の場合はBERT、長い文章の場合はRoBERTaを選択する。
求められる精度: より高い精度が必要な場合はRoBERTaを選択する。
計算量: RoBERTaはBERTよりも計算量が多いため、計算量に制約がある場合はBERTを選択する。

---

KeyBERTは、テキストデータから重要なキーワードやフレーズを抽出するためのPythonライブラリです。このツールは、BertやDistilBertなどのトランスフォーマーベースの言語モデルを使用して、テキスト内の重要なトピックや概念を捉えるためのキーワードを抽出します。

KeyBERTは、次元削減やクラスタリングなどの手法を使用して、トランスフォーマーモデルが生成したテキストの埋め込みを解釈し、重要なキーワードを特定します。これにより、テキストからの要約や検索クエリの生成など、さまざまなNLPタスクで使用できます。

このライブラリは、Pythonで使用でき、テキストデータの前処理や後処理に関する多くの機能も提供しています。KeyBERTは、テキストマイニング、情報検索、要約、および関連する他のNLPタスクで広く使用されています。

---
