## はじめに

* プロジェクトの目的
  フロント側でUIより数値入力します。バック側でルーカス数の計算を行い、計算結果と計算時間をフロントに返すというAjax通信を使った簡単なアプリを
  NEXT.JS（言語TypeScript）上に作成します。完成したらGitHubを介してVercelにDeployします。


## 技術スタックの紹介

* Next.js
  インストール時に言語TypeScriptを指定します。
 ```bash
cd myapp
npx create-next-app@latest .
``` 
* TypeScript
  フロント側でtsxファイルとして、バック側でtsファイルとしてTypeScriptを使用します。
* Ajax通信の実装方法
  Async/Awaitを使ったAjax通信をセットします。
*Vercel
VercelはNEXTJSの開発元である。GitHub Pagesが静的htmlしか公開できないのに対し、NEXTJSなどで作ったサーバーを必要とするWebアプリを無料で公開できる。
Streamlitと同様、GitHubにアップした上で、連携するだけで簡単にDeployが成立する。

ルーカス数列計算機能の実装

## フロントエンドの構築

Ajax通信の実装
* クライアントサイドの実装
* 元々index.htmlとして準備していたもので、Async／Awaitを使ったAjax通信を想定。
  ```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lucas Number</title>
    <script>
        async function checkNumber() {
            const number = document.getElementById("number").value;
            const response = await fetch("/check", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ value: parseInt(number) })
            });
            const result = await response.json();
            document.getElementById("result").innerText = `Lucas Number: ${result.result}, Calculation Time: ${result.duration.toFixed(6)} seconds`;
        }
    </script>
</head>

<body>
    <h1>Lucas Number</h1>
    <input type="number" id="number" placeholder="Enter a number">
    <button onclick="checkNumber()">Check</button>
    <p id="result"></p>
</body>

</html>

  ```
* index.tsx（front側）
  ```
import { useState } from 'react';

const Home = () => {
    const [number, setNumber] = useState<number | undefined>(undefined);
    const [result, setResult] = useState<string>('');

    const checkNumber = async () => {
        if (number !== undefined) {
            const response = await fetch('/api/check', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ value: number })
            });
            const data = await response.json();
            setResult(`Lucas Number: ${data.result}, Calculation Time: ${data.duration.toFixed(6)} seconds`);
        }
    };

    return (
        <div>
            <h1>Lucas Number</h1>
            <input
                type="number"
                value={number !== undefined ? number : ''}
                onChange={(e) => setNumber(parseInt(e.target.value))}
                placeholder="Enter a number"
            />
            <button onClick={checkNumber}>Check</button>
            <p id="result">{result}</p>
        </div>
    );
};

export default Home;

  ```
##  サーバーサイドの実装（API Routes）
check.ts
```
import { NextApiRequest, NextApiResponse } from 'next';

// Lucas数を計算する関数
const calculateLucasNumber = (n: number): number => {
    if (n === 0) return 2;
    if (n === 1) return 1;
    let a = 2, b = 1, c = 0;
    for (let i = 2; i <= n; i++) {
        c = a + b;
        a = b;
        b = c;
    }
    return c;
};

// 計算時間の測定
export default (req: NextApiRequest, res: NextApiResponse) => {
    const start = process.hrtime();
    const { value } = req.body;
    const result = calculateLucasNumber(value);
    const end = process.hrtime(start);
    const duration = end[0] + end[1] / 1e9; // seconds
    res.status(200).json({ result, duration });
};

```
## Vercelへのデプロイ手順
* デプロイのプロセス
ローカルで作成したpjホルダをGitHubの専用リポジトリにpush
Vercelでは自分のGithubが登録済みなので、pjのリポジトリを選ぶだけ


苦労した点や学んだこと
今後の展望
まとめ
