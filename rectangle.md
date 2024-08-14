

---

`cv2.rectangle` は、OpenCVライブラリで画像に長方形を描画するための関数です。この関数の一般的な書式は以下の通りです。

```python
cv2.rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None)
```

### 引数の説明
- **img**: 長方形を描画する対象の画像（NumPy配列）。
- **pt1**: 長方形の左上の頂点の座標 `(x1, y1)`。
- **pt2**: 長方形の右下の頂点の座標 `(x2, y2)`。
- **color**: 長方形の色。BGR形式のタプル `(B, G, R)` で指定します。例えば、青は `(255, 0, 0)`、緑は `(0, 255, 0)`、赤は `(0, 0, 255)`。
- **thickness**: 長方形の枠線の太さ。負の値を指定すると、長方形が塗りつぶされます（デフォルトは1）。
- **lineType**: 枠線の種類。`cv2.LINE_8`（デフォルト）、`cv2.LINE_AA`（アンチエイリアス）、`cv2.LINE_4`、`cv2.LINE_8`、`cv2.LINE_4`などがあります。
- **shift**: 座標値を指定する際の小数点以下の桁数（デフォルトは0）。

### 使用例
```python
import cv2

# 空の画像を作成
img = cv2.imread('image.jpg')

# 長方形を描画
cv2.rectangle(img, (50, 50), (200, 200), (0, 255, 0), 3)

# 画像を表示
cv2.imshow('Rectangle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

この例では、画像 `image.jpg` に緑色の枠線（太さ3ピクセル）で `(50, 50)` から `(200, 200)` の座標範囲に長方形が描かれます。

---
