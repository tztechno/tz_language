###
# ASP.NET MVC
###


---

ASP.NET MVCをMacにインストールする手順は以下の通りです。ASP.NETは通常、Windows環境での開発が一般的ですが、.NET Coreの登場により、MacでもASP.NET Core MVCアプリケーションを開発することが可能になりました。

### 1. Homebrewのインストール
Homebrewがインストールされていない場合、以下のコマンドを使用してインストールします。

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. .NET SDKのインストール
Homebrewを使用して、.NET SDKをインストールします。

```bash
brew install dotnet-sdk
```

これで、最新の.NET SDKがインストールされます。

### 3. インストールの確認
インストールが成功したかどうかを確認するために、以下のコマンドを実行します。

```bash
dotnet --version
```

これで、インストールされた.NET SDKのバージョンが表示されるはずです。

### 4. 新しいASP.NET Core MVCプロジェクトの作成
新しいASP.NET Core MVCプロジェクトを作成するには、以下のコマンドを使用します。

```bash
dotnet new mvc -o MyMvcApp
```

これにより、「MyMvcApp」という名前の新しいディレクトリが作成され、その中にASP.NET Core MVCプロジェクトが生成されます。

### 5. プロジェクトのビルドと実行
作成したプロジェクトディレクトリに移動し、プロジェクトをビルドして実行します。

```bash
cd MyMvcApp
dotnet build
dotnet run
```

`dotnet run`コマンドを実行すると、Kestrelサーバーが起動し、アプリケーションがホストされます。デフォルトでは、http://localhost:5000でアプリケーションにアクセスできます。

### 6. Visual Studio Codeのインストール（オプション）
より良い開発体験のために、Visual Studio Codeをインストールすることをお勧めします。以下のコマンドでHomebrewを使用してインストールできます。

```bash
brew install --cask visual-studio-code
```

### 7. Visual Studio Codeでプロジェクトを開く
Visual Studio Codeを起動し、先ほど作成したプロジェクトディレクトリを開きます。Visual Studio CodeにはC#拡張機能をインストールすることで、.NET開発に必要なIntelliSenseやデバッグ機能が提供されます。

```bash
code MyMvcApp
```

### 8. 必要な拡張機能のインストール
Visual Studio CodeでC#開発を行うために、C#拡張機能をインストールします。Visual Studio Codeを開き、拡張機能マーケットプレースから「C#」を検索し、インストールします。

これで、Mac上でASP.NET Core MVCの開発を始めるための準備が整いました。もし問題が発生した場合は、公式ドキュメントやコミュニティフォーラムを参照してください。

---
