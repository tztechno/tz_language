
---



---



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
