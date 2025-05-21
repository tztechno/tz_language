

数式と、それをプログラミング（特にPython）でどう表現・計算するかの対応例をいくつか示してみますね。

---

# 数式 ⇔ Pythonコード（SymPyやNumPyでの表現）

---

## 1. 関数の定義と微分

### 数式

$$
f(x) = x^3 + 2x + 1
$$

$$
f'(x) = \frac{d}{dx} f(x) = 3x^2 + 2
$$

### Python (SymPy)

```python
from sympy import symbols, diff

x = symbols('x')
f = x**3 + 2*x + 1
f_prime = diff(f, x)
print(f_prime)  # 出力: 3*x**2 + 2
```

---

## 2. 積分

### 数式

$$
I = \int_0^1 (3x^2 + 2) \, dx = \left[x^3 + 2x\right]_0^1 = 1 + 2 = 3
$$

### Python (SymPy)

```python
from sympy import integrate

I = integrate(3*x**2 + 2, (x, 0, 1))
print(I)  # 出力: 3
```

---

## 3. 連立方程式の解

### 数式

$$
\begin{cases}
2x + y = 5 \\
x - y = 1
\end{cases}
$$

### Python (SymPy)

```python
from sympy import symbols, Eq, solve

x, y = symbols('x y')
eq1 = Eq(2*x + y, 5)
eq2 = Eq(x - y, 1)
sol = solve((eq1, eq2), (x, y))
print(sol)  # 出力: {x: 2, y: 1}
```

---

## 4. 行列の掛け算

### 数式

$$
A = \begin{bmatrix}1 & 2 \\ 3 & 4\end{bmatrix}, \quad
B = \begin{bmatrix}5 & 6 \\ 7 & 8\end{bmatrix}
$$

$$
AB = \begin{bmatrix}1\cdot 5 + 2 \cdot 7 & 1\cdot 6 + 2 \cdot 8 \\ 3\cdot 5 + 4 \cdot 7 & 3\cdot 6 + 4 \cdot 8\end{bmatrix}
= \begin{bmatrix}19 & 22 \\ 43 & 50\end{bmatrix}
$$

### Python (NumPy)

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
C = np.dot(A, B)
print(C)
# 出力:
# [[19 22]
#  [43 50]]
```

---

## 5. 微分方程式の数値解法

### 数式

$$
\frac{dy}{dt} = -2y, \quad y(0) = 1
$$

### Python (SciPy)

```python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

def dydt(t, y):
    return -2*y

sol = solve_ivp(dydt, [0, 5], [1], t_eval=np.linspace(0, 5, 100))

plt.plot(sol.t, sol.y[0])
plt.xlabel('t')
plt.ylabel('y(t)')
plt.title('dy/dt = -2y の解')
plt.show()
```

---

# まとめ

| 数学的対象 | Pythonの例                   | ライブラリ |
| ----- | -------------------------- | ----- |
| 関数の微分 | `diff(f, x)`               | SymPy |
| 積分    | `integrate(expr, (x,a,b))` | SymPy |
| 方程式解  | `solve((eq1, eq2), (x,y))` | SymPy |
| 行列計算  | `np.dot(A, B)`             | NumPy |
| 微分方程式 | `solve_ivp()`              | SciPy |

---

こんな感じで、数学の各要素がプログラムでどう表現されるかイメージできましたか？
もっと具体的に知りたい分野や数式があれば、ぜひ教えてください！

