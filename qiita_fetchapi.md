# fetch APIを使用したPOSTリクエスト

## はじめに

AJAXは、JavaScriptを使用して非同期的にサーバーと通信する技術の総称です。その代表的な技術であるfetch APIを使用したPOSTリクエストの例を2つ紹介し、それぞれの違いについて解説します。

## 基本的なfetch APIを使用したPOSTリクエスト

```javascript
<script>
    function sendRequest() {
        const n = document.getElementById('inputN').value;
        fetch('calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ n: parseInt(n) })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            document.getElementById('result').innerText = `Lucas Number L${n} = ${data.result}`;
            document.getElementById('time').innerText = `Time: ${(data.process_time / 1e9).toFixed(3)} sec`;
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
            document.getElementById('result').innerText = 'Error: ' + error.message;
        });
    }
</script>
```

## async/awaitを使用したfetch APIによるPOSTリクエスト

```javascript
<script>
    async function checkNumber() {
        try {
            const number = document.getElementById("number").value;
            const response = await fetch("/check", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ value: parseInt(number) })
            });

            if (!response.ok) {
                throw new Error('Network response was not ok');
            }

            const result = await response.json();
            document.getElementById("result").innerText = `Lucas Number: ${result.result}, Calculation Time: ${result.duration.toFixed(6)} seconds`;
        } catch (error) {
            console.error('There was a problem with the fetch operation:', error);
            document.getElementById("result").innerText = 'Error: ' + error.message;
        }
    }
</script>
```

## 両者の違いについて

1. **同期・非同期処理の書き方**
    - **基本的なfetch API**: `fetch`の後に`.then`を使ってレスポンスを処理しています（Promiseチェーン）。
    - **async/await**: `async`/`await`構文を使って非同期処理をよりシンプルに書いています。

2. **HTML要素のID**
    - **基本的なfetch API**: 入力フィールドのIDが`inputN`、結果表示フィールドのIDが`result`と`time`です。
    - **async/await**: 入力フィールドのIDが`number`、結果表示フィールドのIDが`result`です。

3. **APIエンドポイント**
    - **基本的なfetch API**: `'calculate'`エンドポイントにPOSTリクエストを送信しています。
    - **async/await**: `'/check'`エンドポイントにPOSTリクエストを送信しています。

4. **エラーハンドリング**
    - **基本的なfetch API**: `.then()`メソッド内でエラーチェックを行い、`.catch()`メソッドでエラーをキャッチします。
    - **async/await**: `try`/`catch`構文を使用してエラーハンドリングを行います。エラーが発生した場合も、同期処理と同様に扱えます。

## async/awaitの汎用性について

**汎用性の高さ**

1. **可読性の向上**: async/awaitは非同期処理を同期処理のように書くことができ、コードの可読性が大幅に向上します。特に複数の非同期処理を連続して行う場合、ネストが深くならず、メンテナンスが容易になります。

2. **エラーハンドリングの簡潔さ**: try/catchブロックを使用することで、従来のPromiseチェーンよりもエラーハンドリングがシンプルになります。非同期処理中に発生した例外も同期処理と同様に扱えるため、エラーハンドリングが統一的に行えます。

3. **同期/非同期の混在に強い**: async/awaitは、同期処理と非同期処理を直感的に混在させることができるため、複雑な処理を簡潔に記述できます。

4. **デバッグのしやすさ**: 非同期処理が直線的に記述されるため、ステップ実行やブレークポイントの設定が容易で、デバッグ作業が効率的に行えます。

## 終わりに

このように、fetch APIを使ったPOSTリクエストには複数の書き方があります。特にasync/awaitは汎用性が高く、コードの可読性とメンテナンス性を向上させるため、推奨される方法です。上記のスクリプトを参考に、それぞれのプロジェクトや要件に応じて適切な方法を選択してください。


