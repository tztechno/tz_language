###
# Kitura 終了
###


---

Kituraプロジェクトの終了は、2020年9月30日にIBMによって発表されました。IBMは、Kituraの開発とメンテナンスを終了し、コミュニティにプロジェクトを移管すると述べました。

主な理由は以下の通りです：

1. IBMがサーバーサイドSwiftの開発に注力しないことを決定したため。
2. Swift Package Managerの進化により、Kituraの一部の機能が不要になったため。
3. コミュニティの関心がVaporなどの他のWebフレームワークに移ってきたため。

IBMは、Kituraユーザーに対し、プロジェクトの移行を検討するよう提案しました。Kituraの代替として、Vapor、Kitura-NIO、SwiftNIOなどが挙げられています。

Kituraは長年にわたってSwiftのサーバーサイド開発を牽引してきましたが、2020年末をもってその役目を終えることになりました。今後は、他のWebフレームワークやSwiftサーバーサイドプロジェクトに注目が集まることが期待されています。

---

Kitura を使用して準備した HTML をルーティングする方法を説明します。HTML ファイルを静的ファイルとして提供する場合と、HTML を動的に生成して返す場合の2つの方法があります。

### 方法1: 静的ファイルとして HTML を提供する

1. **プロジェクトのセットアップ**

   まず、プロジェクトのルートディレクトリに `Public` ディレクトリを作成し、その中に HTML ファイルを配置します。

   ```plaintext
   /HelloWeb
   ├── Package.swift
   ├── Sources
   │   └── HelloWeb
   │       └── main.swift
   └── Public
       └── index.html
   ```

   ここでは `Public` ディレクトリに `index.html` を配置する例を示しています。

2. **ルーティングの設定**

   `main.swift` ファイルで、Kitura を使用して `index.html` をルーティングします。

   ```swift
   // main.swift
   import Kitura
   import KituraStatic

   let router = Router()

   // 静的ファイルの提供
   router.all("/", middleware: StaticFileServer())

   Kitura.addHTTPServer(onPort: 8080, with: router)
   Kitura.run()
   ```

   上記の例では、`StaticFileServer()` ミドルウェアを使用して全てのルート (`/`) に対して `Public` ディレクトリ内の静的ファイルを提供しています。

3. **ビルドと実行**

   ターミナルで以下のコマンドを実行して、プロジェクトをビルドし、サーバーを起動します。

   ```bash
   swift build
   swift run
   ```

   ウェブブラウザで `http://localhost:8080` を開くと、`index.html` ファイルが表示されるはずです。

### 方法2: ルーターで HTML を動的に生成する

もう一つの方法として、Kitura を使用して動的に HTML を生成する方法があります。この方法では、ルーター内で HTML を生成し、それをクライアントに返します。

1. **HTML を動的に生成する**

   `main.swift` ファイルで、ルーティングと HTML の動的生成を設定します。

   ```swift
   // main.swift
   import Kitura

   let router = Router()

   // ルートにアクセスした時に動的にHTMLを生成して返す
   router.get("/") { request, response, next in
       response.send("<html><body><h1>Hello, world!</h1></body></html>")
       next()
   }

   Kitura.addHTTPServer(onPort: 8080, with: router)
   Kitura.run()
   ```

   上記の例では、`router.get("/")` でルート (`/`) にアクセスした際に動的に HTML を生成しています。

2. **ビルドと実行**

   同様に、ターミナルで以下のコマンドを実行して、プロジェクトをビルドし、サーバーを起動します。

   ```bash
   swift build
   swift run
   ```

   ウェブブラウザで `http://localhost:8080` を開くと、動的に生成された HTML が表示されるはずです。

これらの方法を参考にして、Kitura を使用して準備した HTML をルーティングする方法を選択してください。静的ファイルとして提供する場合は `StaticFileServer()` を使用し、動的に生成する場合はルーティング内で HTML を生成して `response.send()` を使用します。

---

Swift の Web フレームワークである Kitura を macOS にインストールする手順を説明します。Kitura は IBM によって開発されたフレームワークで、Swift でのサーバーサイドアプリケーション開発をサポートしています。

### 前提条件
1. **Swift のインストール**: macOS に Swift がインストールされている必要があります。Swift の公式サイト（[Swift.org](https://swift.org/download/)）からインストーラーをダウンロードしてインストールしてください。

### Kitura のインストール手順

1. **Homebrew のインストール (オプション)**:
   Kitura をインストールするためには、Homebrew を使うと便利です。Homebrew をインストールしていない場合は、ターミナルで以下のコマンドを実行してインストールします。

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Kitura のインストール**:
   ターミナルを開き、以下のコマンドを実行して Kitura をインストールします。

   ```bash
   brew install kitura
   ```

   Homebrew を使わずにインストールしたい場合は、以下の手順に従ってください。

   - **Swift Package Manager (SPM) を使ったインストール**:
     ターミナルを開き、適当なディレクトリで新しい Swift プロジェクトを初期化します。

     ```bash
     mkdir MyKituraApp
     cd MyKituraApp
     swift package init --type executable
     ```

     `Package.swift` ファイルをテキストエディタで開き、 `dependencies` に Kitura のパッケージを追加します。

     ```swift
     // swift-tools-version:5.5
     import PackageDescription

     let package = Package(
         name: "MyKituraApp",
         dependencies: [
             .package(url: "https://github.com/Kitura/Kitura.git", from: "2.9.0")
         ],
         targets: [
             .target(
                 name: "MyKituraApp",
                 dependencies: ["Kitura"]
             )
         ]
     )
     ```

     ターミナルで以下のコマンドを実行して依存関係を解決し、プロジェクトをビルドします。

     ```bash
     swift build
     ```

3. **Kitura アプリケーションの作成**:
   Kitura プロジェクトが準備できたら、次のステップは Kitura アプリケーションを作成することです。詳細なチュートリアルやサンプルコードは、Kitura の公式ドキュメント（[Kitura.io](https://www.kitura.io/)）で確認できます。

### プロジェクトの実行

Kitura アプリケーションを実行するには、ターミナルで次のコマンドを使用します。

```bash
swift run
```

デフォルトでは、ポート 8080 でサーバーが起動します。ブラウザで `http://localhost:8080` にアクセスして、Kitura アプリケーションが正しく動作していることを確認できます。

以上で、macOS に Kitura をインストールしてプロジェクトを作成する手順が完了です。

---
