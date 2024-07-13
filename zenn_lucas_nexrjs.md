## はじめに

ルーカス数の計算を行う簡単なWebアプリを作ります。
フロント側でUIより数値入力します。バック側でルーカス数の計算を行い、計算結果と計算時間をフロントに返すというAjax通信を使った簡単なアプリを
NEXT.js（言語TypeScript）で作成します。完成したらVercelにDeployします。


## 技術スタック

#### Next.js
  
 ```bash
cd myapp
npx create-next-app@latest .
``` 
インストール時に言語TypeScriptを指定しておき、フロント側でtsxファイルとして、バック側でtsファイルとしてTypeScriptを使用します。
tsxファイルは、TypeScriptとReactを組み合わせて使用するためのファイル形式です。
  
#### Ajax
Async/Awaitを使ったAjax通信をセットします。async/awaitは、JavaScriptで非同期処理をより簡潔かつに書くための構文です。
これにより、従来のコールバック関数やプロミス（Promise）を使用したコードよりも、同期的なコードのように書けるようになります。

#### Vercel
Vercelはフロントエンド開発者向けのクラウドプラットフォームで、静的サイトやサーバーレス機能を簡単にデプロイ、管理できるサービスです
Next.jsはVercelによって開発されているので、特にNext.jsアプリケーションのデプロイは簡単に成立します。



## フロントエンドの構築

#### Ajax通信の実装
元々async/awaitを用いたAjax通信を想定したjsのscriptが準備されていたので、これをtypescriptに翻訳します。
  ```
<!DOCTYPE html>
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
## デプロイ

ローカルで作成したpjホルダをGitHubの専用リポジトリにpushします。
Vercelでは自分のGithubが登録済みなので、pjのリポジトリを選ぶだけでDeployが成立します。


## 今後の展望
Vercelの環境を使って、しばらくNext.jsを使うWebアプリの開発を続けようかと考えています。
何か進捗があれば、記事を書くかもしれません。




