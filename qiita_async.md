

比較に不要なエラー対応部分を削り、両者のPOST方法に焦点を当てたスクリプトは以下のようになります。

**1. 最初のスクリプト：**

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
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = `Lucas Number L${n} = ${data.result}`;
            document.getElementById('time').innerText = `Time: ${(data.process_time / 1e9).toFixed(3)} sec`;
        });
    }
</script>
```

**2. 二番目のスクリプト：**

```javascript
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

この比較では、両者ともに`fetch` APIを使用してPOSTリクエストを送信していますが、次の点に違いがあります：

1. **同期・非同期処理の書き方**:
    - 最初のスクリプトは`fetch`の後に`.then`を使ってレスポンスを処理しています（Promiseチェーン）。
    - 二番目のスクリプトは`async`/`await`構文を使って非同期処理をよりシンプルに書いています。

2. **HTML要素のID**:
    - 最初のスクリプトでは、入力フィールドのIDが`inputN`、結果表示フィールドのIDが`result`と`time`です。
    - 二番目のスクリプトでは、入力フィールドのIDが`number`、結果表示フィールドのIDが`result`です。

3. **APIエンドポイント**:
    - 最初のスクリプトは`'calculate'`エンドポイントにPOSTリクエストを送信しています。
    - 二番目のスクリプトは`'/check'`エンドポイントにPOSTリクエストを送信しています。

このようにして、両スクリプトのPOSTリクエストの構造と方法を比較できます。
