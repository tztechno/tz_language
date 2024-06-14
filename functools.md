###
# functools
###

---

`functools`モジュールは、Pythonで高階関数や呼び出し可能なオブジェクトに対する操作を提供します。以下に`functools`が提供する主要な関数とユーティリティの概要をまとめます。

### 1. `functools.reduce()`
- **目的:** 2引数の関数をイテラブルの各要素に累積的に適用し、単一の値に減らします。
- **構文:** `functools.reduce(function, iterable[, initializer])`
- **例:**
  ```python
  from functools import reduce
  result = reduce(lambda x, y: x + y, [1, 2, 3, 4])  # resultは10
  ```

### 2. `functools.partial()`
- **目的:** 関数の一部の引数を固定し、新しい関数を生成します。
- **構文:** `functools.partial(func, /, *args, **keywords)`
- **例:**
  ```python
  from functools import partial
  def multiply(x, y):
      return x * y
  double = partial(multiply, 2)
  result = double(5)  # resultは10
  ```

### 3. `functools.wraps()`
- **目的:** ラッパー関数のメタデータを元の関数に一致させるためのデコレータです。
- **構文:** `functools.wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)`
- **例:**
  ```python
  from functools import wraps
  def decorator(func):
      @wraps(func)
      def wrapper(*args, **kwargs):
          print("関数が呼ばれる前に何かが起こっています。")
          return func(*args, **kwargs)
      return wrapper

  @decorator
  def say_hello():
      print("こんにちは！")
  ```

### 4. `functools.lru_cache()`
- **目的:** 関数の結果をキャッシュするデコレータを提供します（Least Recently Usedキャッシュ）。
- **構文:** `functools.lru_cache(maxsize=128, typed=False)`
- **例:**
  ```python
  from functools import lru_cache

  @lru_cache(maxsize=100)
  def fib(n):
      if n < 2:
          return n
      return fib(n-1) + fib(n-2)
  ```

### 5. `functools.total_ordering()`
- **目的:** 欠けている比較メソッドを補完するクラスデコレータです。
- **構文:** `functools.total_ordering(cls)`
- **例:**
  ```python
  from functools import total_ordering

  @total_ordering
  class Person:
      def __init__(self, name, age):
          self.name = name
          self.age = age

      def __eq__(self, other):
          return self.age == other.age

      def __lt__(self, other):
          return self.age < other.age
  ```

### 6. `functools.singledispatch()`
- **目的:** 関数をシングルディスパッチジェネリック関数に変換するデコレータです。
- **構文:** `functools.singledispatch(func)`
- **例:**
  ```python
  from functools import singledispatch

  @singledispatch
  def fun(arg):
      print("デフォルト:", arg)

  @fun.register(int)
  def _(arg):
      print("整数:", arg)

  @fun.register(list)
  def _(arg):
      print("リスト:", arg)
  ```

### 7. `functools.cmp_to_key()`
- **目的:** 比較関数を`sorted()`のためのキー関数に変換します。
- **構文:** `functools.cmp_to_key(func)`
- **例:**
  ```python
  from functools import cmp_to_key

  def compare(a, b):
      return (a > b) - (a < b)

  sorted_list = sorted([4, 2, 5, 1, 3], key=cmp_to_key(compare))
  ```

これらは、Pythonで関数の操作、最適化、およびデコレーションに役立つ`functools`モジュールが提供する主要なユーティリティです。

---
