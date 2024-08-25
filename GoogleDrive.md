

---

APIキーやOAuth 2.0を使用せずに、Google Driveにファイルをアップロードすることは、直接的には難しいです。Google Drive APIにアクセスするためには、通常これらの認証手段が必要です。

しかし、もし簡単な方法でファイルをGoogle Driveにアップロードしたい場合、Google DriveのウェブインターフェースやGoogle Apps Scriptを使う方法もあります。以下は、Google Apps Scriptを使用して、OAuth 2.0を必要とせずにHTML上からファイルをGoogle Driveにアップロードする方法です。

### 手順

1. **Google Apps Scriptの作成**:
   - Google Drive内で新しいGoogle Apps Scriptプロジェクトを作成します。
   - 以下のコードをGoogle Apps Scriptに貼り付けます。

    ```javascript
    function doGet() {
      return HtmlService.createHtmlOutputFromFile('form.html')
          .setSandboxMode(HtmlService.SandboxMode.IFRAME);
    }

    function uploadFileToDrive(data, fileName) {
      var folder = DriveApp.getFolderById('YOUR_FOLDER_ID');  // フォルダIDを指定
      var contentType = data.substring(5, data.indexOf(';'));
      var bytes = Utilities.base64Decode(data.substr(data.indexOf('base64,') + 7));
      var blob = Utilities.newBlob(bytes, contentType, fileName);
      var file = folder.createFile(blob);
      return file.getUrl();
    }
    ```

   - `YOUR_FOLDER_ID` を、アップロード先のGoogle DriveフォルダIDに置き換えます。

2. **HTMLファイルの作成**:
   - 同じGoogle Apps Scriptプロジェクトで、`form.html`という名前のHTMLファイルを作成し、以下のHTMLコードを追加します。

    ```html
    <form id="myForm">
      <input type="file" id="fileInput" />
      <input type="button" value="Upload File" onclick="uploadFile()" />
    </form>
    <div id="output"></div>

    <script>
      function uploadFile() {
        var fileInput = document.getElementById('fileInput');
        var file = fileInput.files[0];
        var reader = new FileReader();
        
        reader.onload = function(e) {
          var data = e.target.result;
          google.script.run.withSuccessHandler(function(url) {
            document.getElementById('output').innerHTML = 'File uploaded: <a href="' + url + '" target="_blank">View File</a>';
          }).uploadFileToDrive(data, file.name);
        };
        
        reader.readAsDataURL(file);
      }
    </script>
    ```

3. **デプロイ**:
   - 「デプロイ」 > 「新しいデプロイ」 > 「ウェブアプリ」としてデプロイします。
   - 必要に応じてアクセスを「全員（インターネット上の誰でも）」に設定し、「デプロイ」ボタンを押します。

4. **アップロード**:
   - デプロイされたウェブアプリのURLにアクセスし、CSVファイルを選択して「Upload File」ボタンをクリックすると、選択されたファイルが指定のGoogle Driveフォルダにアップロードされます。

### 注意点
- この方法では、Google Apps Scriptを使用するため、OAuth 2.0やAPIキーは必要ありませんが、スクリプト自体がGoogleアカウントに結びついているため、基本的な認証は行われています。
- アップロード先のフォルダを公開する必要がある場合、セキュリティに注意してください。

この方法を使えば、認証手段を簡略化しつつ、HTMLフォームからファイルをGoogle Driveにアップロードできます。

---

HTML上で実験的に実装するために、最小限のセットアップでGoogle Driveにファイルをアップロードする例を示します。以下のコードを使って、Webページ上でボタンをクリックするとCSVファイルが生成され、Google Apps Scriptを通じてGoogle Driveに保存されるようにします。

### 前提条件

1. Google Apps Scriptがセットアップされ、ウェブアプリケーションとしてデプロイされていること。
2. 公開フォルダのIDをGoogle Apps Scriptのコードに設定していること。
3. GASウェブアプリケーションのURLを取得していること。

### Google Apps Script (GAS) のコード

以下のコードをGASに追加してデプロイします。

```javascript
function doPost(e) {
    try {
        var params = JSON.parse(e.postData.contents);
        var folder = DriveApp.getFolderById('YOUR_FOLDER_ID'); // 公開フォルダのIDを指定
        var blob = Utilities.newBlob(params.content, 'text/csv', params.fileName);
        var file = folder.createFile(blob);
        return ContentService.createTextOutput(JSON.stringify({ url: file.getUrl() })).setMimeType(ContentService.MimeType.JSON);
    } catch (error) {
        return ContentService.createTextOutput(JSON.stringify({ error: error.toString() })).setMimeType(ContentService.MimeType.JSON);
    }
}
```

### HTMLおよびJavaScriptコード

次に、以下のHTMLおよびJavaScriptコードを使って実験的に実装します。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSV Upload to Google Drive</title>
</head>
<body>
    <h1>CSV Upload to Google Drive</h1>
    <button id="saveCsvButton">Save CSV to Google Drive</button>

    <script>
        document.getElementById('saveCsvButton').addEventListener('click', function () {
            const progressData = {
                'Region1': '50%',
                'Region2': '75%',
                'Region3': '100%'
            };

            const csvContent = Object.entries(progressData).map(([region, progress]) => `${region},${progress}`).join('\n');
            const fileName = `Progress_${new Date().toISOString().replace(/[:.]/g, '-')}.csv`;

            fetch('YOUR_GAS_WEB_APP_URL', {
                method: 'POST',
                body: JSON.stringify({ content: csvContent, fileName }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.url) {
                    console.log('File uploaded successfully:', data.url);
                } else {
                    console.error('Error uploading file:', data.error);
                }
            })
            .catch(error => console.error('Error uploading file:', error));
        });
    </script>
</body>
</html>
```

### 説明

1. **HTML**:
    - シンプルなボタンを用意し、クリックするとJavaScriptの処理が開始されます。

2. **JavaScript**:
    - `progressData`オブジェクトにサンプルデータを用意しています。
    - `csvContent`変数にCSV形式の文字列を作成します。
    - `fetch`を使ってGASウェブアプリケーションのURLにPOSTリクエストを送信し、生成したCSVデータとファイル名を送ります。
    - レスポンスを受け取り、成功した場合にはコンソールにアップロードされたファイルのURLを表示し、失敗した場合にはエラーメッセージを表示します。

これにより、HTMLページ上のボタンをクリックするだけで、CSVファイルをGoogle Driveに直接アップロードすることができます。

---

ファイル出力ボタンを直接Google Driveに送信するリクエストに変換することは可能です。これには、ユーザーがボタンをクリックしたときに生成されるファイルの内容をGoogle Apps ScriptにPOSTリクエストとして送信する必要があります。以下は、その実装例です。

### Google Apps Script (GAS) のセットアップ

前述の通り、Google Apps Scriptでファイルを受け取りGoogle Driveに保存するサービスを作成します。

#### GASコードの作成

1. **Google DriveでGoogle Apps Scriptプロジェクトを作成**:
    - Google Driveで「新規」->「その他」->「Google Apps Script」を選択します。

2. **GASコードを作成**:
    ```javascript
    function doPost(e) {
        try {
            // POSTリクエストからデータを取得
            var params = JSON.parse(e.postData.contents);

            // 公開フォルダのIDを指定
            var folder = DriveApp.getFolderById('YOUR_FOLDER_ID'); 
            
            // Blobを作成し、ファイルとしてフォルダに保存
            var blob = Utilities.newBlob(params.content, 'text/csv', params.fileName);
            var file = folder.createFile(blob);

            // ファイルのURLをレスポンスとして返す
            return ContentService.createTextOutput(JSON.stringify({ url: file.getUrl() })).setMimeType(ContentService.MimeType.JSON);
        } catch (error) {
            // エラーハンドリング
            return ContentService.createTextOutput(JSON.stringify({ error: error.toString() })).setMimeType(ContentService.MimeType.JSON);
        }
    }
    ```

3. **GASプロジェクトをデプロイ**:
    - 「デプロイ」->「ウェブアプリケーションとしてデプロイ」を選択。
    - 新しいプロジェクトバージョンを作成。
    - 「実行するアプリケーションを次のユーザーとして実行」は「自分」。
    - 「アクセス権」は「全員（匿名ユーザーを含む）」を選択。
    - デプロイし、ウェブアプリケーションのURLをコピー。

### フロントエンドからのリクエスト

次に、ユーザーの端末上で動作するWebアプリケーションからGASに対してリクエストを送信するコードを作成します。

```jsx
import React, { useState } from 'react';
import Papa from 'papaparse';

const App = ({ progressData }) => {
    const handleSaveCSV = () => {
        const csvContent = Papa.unparse(
            Object.entries(progressData).map(([region, progress]) => ({
                region,
                progress,
            }))
        );

        const fileName = `Progress_${new Date().toISOString().replace(/[:.]/g, '-')}.csv`;

        fetch('YOUR_GAS_WEB_APP_URL', {
            method: 'POST',
            body: JSON.stringify({ content: csvContent, fileName }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            if (data.url) {
                console.log('File uploaded successfully:', data.url);
            } else {
                console.error('Error uploading file:', data.error);
            }
        })
        .catch(error => console.error('Error uploading file:', error));
    };

    return (
        <div>
            <button onClick={handleSaveCSV}>Save CSV to Google Drive</button>
        </div>
    );
};

export default App;
```

### 説明

1. **`handleSaveCSV`関数**:
    - `progressData`をCSV形式に変換します。
    - 変換したCSVデータとファイル名を含むオブジェクトをJSONとしてGASウェブアプリケーションのURLにPOSTリクエストとして送信します。

2. **GASウェブアプリケーション**:
    - POSTリクエストを受け取り、JSONデータを解析します。
    - 解析されたデータを使ってBlobを作成し、指定された公開フォルダーにファイルとして保存します。
    - 保存されたファイルのURLをレスポンスとして返します。

これにより、ユーザーが「Save CSV to Google Drive」ボタンをクリックすると、CSVデータが生成され、直接Google Driveに送信されて保存されます。


---

ユーザーの端末で開かれているWebアプリから直接Google Driveの公開フォルダーにファイルをアップロードするためには、Google Apps Script（GAS）を使ってバックエンドサービスを提供し、そこにファイルを送信するのが現実的なアプローチです。以下の手順で、GASを利用してこのフローを実現する方法を具体的に説明します。

### 1. Google Apps Script (GAS) のセットアップ

まず、Google Apps Scriptを使ってファイルを受け取ってGoogle Driveに保存するサービスを作成します。

#### GASコードの作成

1. **Google DriveでGoogle Apps Scriptプロジェクトを作成**:
    - Google Driveで「新規」->「その他」->「Google Apps Script」を選択します。

2. **GASコードを作成**:
    ```javascript
    function doPost(e) {
        try {
            // POSTリクエストからデータを取得
            var params = JSON.parse(e.postData.contents);

            // 公開フォルダのIDを指定
            var folder = DriveApp.getFolderById('YOUR_FOLDER_ID'); 
            
            // Blobを作成し、ファイルとしてフォルダに保存
            var blob = Utilities.newBlob(params.content, 'text/csv', params.fileName);
            var file = folder.createFile(blob);

            // ファイルのURLをレスポンスとして返す
            return ContentService.createTextOutput(JSON.stringify({ url: file.getUrl() })).setMimeType(ContentService.MimeType.JSON);
        } catch (error) {
            // エラーハンドリング
            return ContentService.createTextOutput(JSON.stringify({ error: error.toString() })).setMimeType(ContentService.MimeType.JSON);
        }
    }
    ```

3. **GASプロジェクトをデプロイ**:
    - 「デプロイ」->「ウェブアプリケーションとしてデプロイ」を選択。
    - 新しいプロジェクトバージョンを作成。
    - 「実行するアプリケーションを次のユーザーとして実行」は「自分」。
    - 「アクセス権」は「全員（匿名ユーザーを含む）」を選択。
    - デプロイし、ウェブアプリケーションのURLをコピー。

### 2. フロントエンド（Webアプリ）からリクエストを送信

次に、ユーザーの端末上で動作するWebアプリケーションからGASに対してリクエストを送信するコードを作成します。

```jsx
import React from 'react';
import Papa from 'papaparse';

const handleSaveCSV = (progressData) => {
    const csvContent = Papa.unparse(
        Object.entries(progressData).map(([region, progress]) => ({
            region,
            progress,
        }))
    );

    const fileName = `Progress_${new Date().toISOString().replace(/[:.]/g, '-')}.csv`;

    fetch('YOUR_GAS_WEB_APP_URL', {
        method: 'POST',
        body: JSON.stringify({ content: csvContent, fileName }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.url) {
            console.log('File uploaded successfully:', data.url);
        } else {
            console.error('Error uploading file:', data.error);
        }
    })
    .catch(error => console.error('Error uploading file:', error));
};

const App = ({ progressData }) => (
    <div>
        <button onClick={() => handleSaveCSV(progressData)}>Save CSV to Google Drive</button>
    </div>
);

export default App;
```

### 解説

1. **GASの`doPost`関数**:
    - フロントエンドからのPOSTリクエストを受け取り、JSON形式のデータを解析します。
    - 解析されたデータを使ってBlob（バイナリラージオブジェクト）を作成し、指定された公開フォルダーにファイルとして保存します。
    - ファイルのURLをJSONレスポンスとして返します。

2. **フロントエンドの`handleSaveCSV`関数**:
    - `progressData`をCSV形式に変換し、GASウェブアプリケーションのURLに対してPOSTリクエストを送信します。
    - レスポンスとして返されたファイルのURLをログに表示します。

この方法により、ユーザーの端末上で生成されたファイルを公開フォルダーに直接アップロードすることができます。GASがバックエンドサービスとして動作し、認証を簡略化してくれます。

---

Webアプリ上で生成したファイルをGoogle Driveの公開フォルダーに送信する場合、Google Apps Scriptを使用して認証を簡略化する方法が有効です。以下にその手順を詳しく説明します。

### Google Apps Scriptのセットアップ

1. **Google Apps Scriptプロジェクトを作成する**
    - Google Driveで「新規」->「その他」->「Google Apps Script」を選択します。

2. **スクリプトを作成する**
    ```javascript
    function doPost(e) {
        try {
            var params = JSON.parse(e.postData.contents);
            var folder = DriveApp.getFolderById('YOUR_FOLDER_ID'); // 公開フォルダのIDを指定
            var blob = Utilities.newBlob(params.content, 'text/csv', params.fileName);
            var file = folder.createFile(blob);
            return ContentService.createTextOutput(JSON.stringify({ url: file.getUrl() })).setMimeType(ContentService.MimeType.JSON);
        } catch (f) {
            return ContentService.createTextOutput(JSON.stringify({ error: f.toString() })).setMimeType(ContentService.MimeType.JSON);
        }
    }
    ```

3. **デプロイする**
    - 「デプロイ」->「ウェブアプリケーションとしてデプロイ」を選択し、新しいプロジェクトバージョンを作成してデプロイします。
    - 「実行するアプリケーションを次のユーザーとして実行」は「自分」、アクセス権は「全員（匿名ユーザーを含む）」を選択します。
    - ウェブアプリケーションのURLをコピーします。

### Webアプリからのリクエスト

次に、WebアプリからGoogle Apps Scriptを呼び出してファイルをアップロードします。

```jsx
import React from 'react';
import Papa from 'papaparse';

const handleSaveCSV = (progressData) => {
    const csvContent = Papa.unparse(
        Object.entries(progressData).map(([region, progress]) => ({
            region,
            progress,
        }))
    );

    const fileName = `Progress_${new Date().toISOString().replace(/[:.]/g, '-')}.csv`;

    fetch('YOUR_WEB_APP_URL', {
        method: 'POST',
        body: JSON.stringify({ content: csvContent, fileName }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.url) {
            console.log('File uploaded successfully:', data.url);
        } else {
            console.error('Error uploading file:', data.error);
        }
    })
    .catch(error => console.error('Error uploading file:', error));
};

const App = ({ progressData }) => (
    <div>
        <button onClick={() => handleSaveCSV(progressData)}>Save CSV to Google Drive</button>
    </div>
);

export default App;
```

### 注意点

1. **公開フォルダーの設定**
    - Google Driveのフォルダーが「リンクを知っている全員が閲覧可能」に設定されていることを確認してください。

2. **セキュリティ**
    - ウェブアプリケーションは全員に公開されるため、不正なアクセスを防ぐための対策を講じることを検討してください。例えば、リクエストにシークレットキーを含め、そのキーを検証するようにするなどの方法があります。

この方法により、WebアプリケーションからGoogle Driveの公開フォルダーにファイルを直接アップロードすることができます。

---

公開設定されているGoogle Driveフォルダーにファイルをアップロードする場合でも、ファイルのアップロードには認証が必要です。公開設定は、フォルダーやファイルの共有設定であって、APIを通じてファイルをアップロードするための認証とは異なります。

Google Drive APIを使用する場合、APIを呼び出してファイルを作成、更新、削除するためには、ユーザーの許可と適切な認証が常に必要です。したがって、認証フローを省略することはできません。

ただし、Google Apps Scriptを使用して公開されたGoogle Driveフォルダーにファイルをアップロードする簡易的な方法を考えることもできます。以下に、Google Apps ScriptとGoogle Sheetsを使ってファイルをアップロードする例を示します。

### Google Apps Scriptによるアップロード
1. **Google Apps Scriptプロジェクトを作成**:
    - Google Driveで「新規」->「その他」->「Google Apps Script」を選択します。

2. **スクリプトを作成**:
    ```javascript
    function doGet(e) {
        return ContentService.createTextOutput("Google Apps Script is working");
    }

    function uploadFile(content, fileName) {
        var folder = DriveApp.getFolderById('YOUR_FOLDER_ID'); // 公開フォルダのIDを指定
        var blob = Utilities.newBlob(content, 'text/csv', fileName);
        var file = folder.createFile(blob);
        return file.getUrl();
    }
    ```

3. **デプロイ**:
    - 「デプロイ」->「ウェブアプリケーションとしてデプロイ」を選択し、新しいプロジェクトバージョンを作成してデプロイします。
    - ウェブアプリケーションのURLをコピーします。

### JavaScriptからのリクエスト
次に、JavaScriptからGoogle Apps Scriptを呼び出してファイルをアップロードします。

```jsx
import React, { useState } from 'react';
import Papa from 'papaparse';

const handleSaveCSV = () => {
    const csvContent = Papa.unparse(
        Object.entries(progressData).map(([region, progress]) => ({
            region,
            progress,
        }))
    );

    const fileName = `Progress_${new Date().toISOString().replace(/[:.]/g, '-')}.csv`;

    fetch('YOUR_WEB_APP_URL', {
        method: 'POST',
        body: JSON.stringify({ content: csvContent, fileName }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => console.log('File uploaded successfully:', data))
    .catch(error => console.error('Error uploading file:', error));
};

const App = () => (
    <div>
        <button onClick={handleSaveCSV}>Save CSV to Google Drive</button>
    </div>
);

export default App;
```

このコードは次の手順で動作します：

1. CSVデータを作成し、Google Apps ScriptのエンドポイントにPOSTリクエストを送信します。
2. Google Apps Scriptがファイルを公開フォルダーに保存し、ファイルのURLを返します。

この方法を使用すると、認証フローを簡略化しつつ、ファイルを公開フォルダーにアップロードできます。

---

直接Google Driveに保存するには、Google Drive APIを使用する必要があります。以下に、Google Drive APIを使用してファイルをアップロードする方法の概要とコード例を示します。

### 準備
1. **Google API Consoleでプロジェクトを作成**
2. **Drive APIを有効にする**
3. **OAuth 2.0 クライアントIDを作成**し、クライアントIDとクライアントシークレットを取得

### 必要なライブラリのインストール
まず、必要なライブラリをインストールします。
```bash
npm install gapi-script
```

### 認証フローのセットアップ
以下のコード例は、ReactアプリケーションでGoogle Driveにファイルをアップロードする方法を示しています。

```jsx
import React from 'react';
import { gapi } from 'gapi-script';
import Papa from 'papaparse';

const CLIENT_ID = 'YOUR_CLIENT_ID';
const API_KEY = 'YOUR_API_KEY';
const SCOPES = 'https://www.googleapis.com/auth/drive.file';

const handleSaveCSV = () => {
    const csvContent = Papa.unparse(
        Object.entries(progressData).map(([region, progress]) => ({
            region,
            progress,
        }))
    );

    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });

    const onSuccess = (googleUser) => {
        const auth = gapi.auth2.getAuthInstance();
        const accessToken = auth.currentUser.get().getAuthResponse().access_token;

        const form = new FormData();
        form.append('metadata', new Blob([JSON.stringify({
            name: `Progress_${new Date().toISOString().replace(/[:.]/g, '-')}.csv`,
            mimeType: 'text/csv'
        })], { type: 'application/json' }));
        form.append('file', blob);

        fetch('https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart', {
            method: 'POST',
            headers: new Headers({ 'Authorization': 'Bearer ' + accessToken }),
            body: form,
        }).then(response => response.json())
          .then(data => console.log(data))
          .catch(error => console.error('Error uploading file:', error));
    };

    gapi.load('client:auth2', () => {
        gapi.client.init({
            apiKey: API_KEY,
            clientId: CLIENT_ID,
            discoveryDocs: ['https://www.googleapis.com/discovery/v1/apis/drive/v3/rest'],
            scope: SCOPES,
        }).then(() => {
            const auth = gapi.auth2.getAuthInstance();
            if (!auth.isSignedIn.get()) {
                auth.signIn().then(onSuccess);
            } else {
                onSuccess();
            }
        });
    });
};

const App = () => (
    <div>
        <button onClick={handleSaveCSV}>Save CSV to Google Drive</button>
    </div>
);

export default App;
```

このコードは以下の手順で動作します：

1. Google APIクライアントライブラリをロードし、クライアントを初期化します。
2. ユーザーが認証されていない場合は、認証を求めます。
3. 認証が成功した後、Google Driveにファイルをアップロードします。

クライアントIDとAPIキーを自分のプロジェクトのものに置き換えてください。また、Google API ConsoleでDrive APIとOAuth 2.0を設定する必要があります。

この方法で、CSVファイルをGoogle Driveに直接保存することができます。

---
