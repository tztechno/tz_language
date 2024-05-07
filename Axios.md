# Axios
### 

---

以下は、Axiosを使用せずにJavaScriptでGETリクエストを送信する例です。この例では、XMLHttpRequestオブジェクトを使用してリクエストを処理します。

```
// 新しいXMLHttpRequestオブジェクトを作成
var xhr = new XMLHttpRequest();

// リクエストを準備
xhr.open('GET', 'https://jsonplaceholder.typicode.com/posts/1', true);

// リクエストが完了したときの処理
xhr.onload = function() {
  // リクエストが成功したかを確認
  if (xhr.status >= 200 && xhr.status < 300) {
    // レスポンスを処理
    console.log('レスポンスデータ:', JSON.parse(xhr.responseText));
  } else {
    // エラーを処理
    console.error('リクエストが失敗しました:', xhr.statusText);
  }
};

// ネットワークエラーの処理
xhr.onerror = function() {
  console.error('ネットワークエラーが発生しました');
};

// リクエストを送信
xhr.send();
```

この例では、XMLHttpRequestオブジェクトを使ってGETリクエストを送信しています。xhr.open()メソッドでリクエストを準備し、xhr.onloadイベントハンドラーでリクエストが完了したときの処理を定義します。レスポンスが成功したかどうかは、xhr.statusをチェックしています。成功した場合は、xhr.responseTextからレスポンスデータを取得します。また、ネットワークエラーの場合はxhr.onerrorで処理します。

---


以下は、Axiosを使用してGETリクエストを送信し、レスポンスを処理する基本的なコード例です。

```
// Axiosをインポート
const axios = require('axios'); // Node.jsの場合

// GETリクエストを送信
axios.get('https://jsonplaceholder.typicode.com/posts/1')
  .then(response => {
    // レスポンスを処理
    console.log('レスポンスデータ:', response.data);
  })
  .catch(error => {
    // エラーを処理
    console.error('エラーが発生しました:', error);
  });
```

上記の例では、axios.get()を使って指定したURLにGETリクエストを送信しています。

その後、.then()メソッドを使用して成功した場合の処理と.catch()メソッドを使用してエラーが発生した場合の処理を定義しています。

このコードはNode.js環境で実行することを想定していますが、ブラウザでも同様に使用できます。ブラウザで使用する場合、requireの代わりに<script>タグでAxiosを読み込む必要があります。

---

Axiosは、JavaScriptのライブラリであり、特にブラウザやNode.jsでのHTTPリクエストの処理に使用されます。主にPromiseベースのAPIを提供し、リクエストの送信やレスポンスの処理を容易にします。

Axiosを使うことで、GET、POST、PUT、DELETEなどのHTTPリクエストを発行できます。また、リクエストのヘッダーやパラメーターを設定し、レスポンスを受け取ることもできます。

さらに、AxiosはHTTPクライアントとしての機能を提供するだけでなく、リクエストのキャンセルや、リクエスト/レスポンスの変換（JSONやFormDataなど）、エラーハンドリングなどの便利な機能も提供します。

Node.jsやブラウザの両方で利用でき、広く採用されているため、多くの開発者にとって標準的なHTTPクライアントの選択肢の一つとなっています。

---
