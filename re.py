###
# re
###

---

`re`モジュールはPythonの標準ライブラリの一部で、正規表現を使って文字列の検索、置換、分割などを行うための機能を提供します。以下は `re` モジュールの基本的な使い方です。

### 1. インポート
まず、`re` モジュールをインポートします。
```python
import re
```

### 2. 基本的な機能
#### a. `re.search()`
文字列全体を対象に、正規表現にマッチする部分を検索します。
```python
pattern = r'\d+'  # 一つ以上の数字にマッチするパターン
text = 'The price is 100 dollars'
match = re.search(pattern, text)

if match:
    print(match.group())  # 出力: 100
```

#### b. `re.match()`
文字列の先頭が正規表現にマッチするかを調べます。
```python
pattern = r'\d+'
text = '100 dollars'
match = re.match(pattern, text)

if match:
    print(match.group())  # 出力: 100
```

#### c. `re.findall()`
文字列全体から正規表現にマッチするすべての部分をリストとして返します。
```python
pattern = r'\d+'
text = 'The prices are 100, 200, and 300 dollars'
matches = re.findall(pattern, text)

print(matches)  # 出力: ['100', '200', '300']
```

#### d. `re.sub()`
正規表現にマッチする部分を置換します。
```python
pattern = r'\d+'
replacement = 'XXX'
text = 'The prices are 100, 200, and 300 dollars'
new_text = re.sub(pattern, replacement, text)

print(new_text)  # 出力: The prices are XXX, XXX, and XXX dollars
```

### 3. コンパイル済み正規表現オブジェクト
頻繁に使うパターンはコンパイルしておくと便利です。
```python
pattern = re.compile(r'\d+')
text = 'The prices are 100, 200, and 300 dollars'

# search() メソッド
match = pattern.search(text)
if match:
    print(match.group())  # 出力: 100

# findall() メソッド
matches = pattern.findall(text)
print(matches)  # 出力: ['100', '200', '300']

# sub() メソッド
new_text = pattern.sub('XXX', text)
print(new_text)  # 出力: The prices are XXX, XXX, and XXX dollars
```

### 4. 正規表現の特別な文字
正規表現にはいくつかの特別な文字（メタキャラクター）があります。例えば：
- `.`: 任意の1文字
- `^`: 行の先頭
- `$`: 行の末尾
- `*`: 0回以上の繰り返し
- `+`: 1回以上の繰り返し
- `?`: 0回または1回の繰り返し
- `{n}`: n回の繰り返し
- `[ ]`: 文字クラス（例：`[a-z]`は小文字のアルファベットにマッチ）

### 5. フラグ
正規表現にはいくつかのフラグがあります。例えば：
- `re.IGNORECASE` (または `re.I`): 大文字小文字を区別しない
- `re.MULTILINE` (または `re.M`): 複数行モード
- `re.DOTALL` (または `re.S`): ドット `.` が改行文字にもマッチするようにする

```python
pattern = re.compile(r'price', re.IGNORECASE)
text = 'The Price is 100 dollars'
matches = pattern.findall(text)

print(matches)  # 出力: ['Price']
```

これが `re` モジュールの基本的な使い方です。さらに詳しい情報は、Pythonの公式ドキュメントを参照してください。

---
