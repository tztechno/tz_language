###
# Kitura
###

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
