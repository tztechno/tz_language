

---

GASが手動で動いたとしても、function doGet() を加えておかなければ、Webアプリとして成立しない

忘れがち

---

はい、このスクリプトがウェブアプリから直接起動できない主な理由がいくつかあります：

1. 関数名の不一致:
   ウェブアプリのフロントエンド（HTML/JavaScript）から呼び出そうとしている関数名（`summarize()`）と、実際のGoogle Apps Scriptの関数名（`summarizeCsvDataToSheet()`）が一致していません。

2. ウェブアプリの設定:
   このスクリプトをウェブアプリとして公開し、適切なエンドポイントを設定する必要があります。現在のコードでは、ウェブアプリとしての設定が行われていないようです。

3. 認証とアクセス権限:
   スクリプトがDriveAppやSpreadsheetAppにアクセスしているため、適切な認証と権限設定が必要です。ウェブアプリとして実行する場合、これらのサービスへのアクセス権限が正しく設定されていない可能性があります。

4. クロスオリジン制約:
   ウェブアプリからこのスクリプトを呼び出す場合、クロスオリジンリソース共有（CORS）の設定が必要になる可能性があります。

5. 非同期処理の扱い:
   現在のフロントエンドコードは、非同期処理を想定していますが、バックエンドのGoogle Apps Scriptは同期的に書かれています。ウェブアプリとして使用する場合、非同期処理への対応が必要になります。

これらの問題を解決するには、以下の手順を踏む必要があります：

1. スクリプトをウェブアプリとして公開し、適切なエンドポイントを設定する。
2. `doGet()` または `doPost()` 関数を追加して、HTTPリクエストを処理できるようにする。
3. 認証と権限の設定を確認し、必要に応じて調整する。
4. フロントエンドのコードを修正して、正しいエンドポイントを呼び出すようにする。
5. 必要に応じて、CORSの設定を行う。

例えば、以下のように `doGet()` 関数を追加することで、ウェブアプリとして機能させることができます：

```javascript
function doGet() {
  try {
    summarizeCsvDataToSheet();
    return ContentService.createTextOutput('処理が完了しました。');
  } catch (error) {
    return ContentService.createTextOutput('エラーが発生しました: ' + error.toString());
  }
}
```

そして、フロントエンドの `summarize()` 関数を、このウェブアプリのURLを呼び出すように修正する必要があります。これらの変更を行うことで、ボタンからスクリプトを起動できるようになるはずです。

---

HTMLファイルをGASの外部に置く場合でも、`doGet` 関数はWebアプリとして動作させるために必要です。ただし、HTMLファイルが外部にある場合、GAS内の `HtmlService.createHtmlOutputFromFile('index')` は使えないため、別の方法でHTMLをロードする必要があります。

以下の方法で、外部のHTMLファイルを使用することができます。

### 1. 外部のHTMLを取得して表示
外部のHTMLファイルをWebアプリで表示するには、URLからHTMLを取得し、その内容をWebアプリとして出力します。

```javascript
function doGet(e) {
  // 外部のHTMLファイルのURL
  var url = 'https://example.com/path/to/your.html';
  
  // URLからHTMLの内容を取得
  var response = UrlFetchApp.fetch(url);
  var htmlContent = response.getContentText();
  
  // HTMLをWebアプリとして出力
  return HtmlService.createHtmlOutput(htmlContent);
}
```

### 2. `doGet` 関数の役割
`doGet` 関数は、GASでWebアプリを公開するときに、最初のリクエストを処理し、レスポンスとしてHTMLを返す役割を果たします。このため、外部のHTMLファイルを使用する場合でも、`doGet` 関数自体が「邪魔」になることはなく、むしろ必要なものです。

### まとめ
`doGet` 関数はWebアプリとしてのエントリーポイントなので、削除することはできません。外部のHTMLファイルを使用する場合でも、この関数を使って適切にHTMLを取得・表示することが必要です。

---
