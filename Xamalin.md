###
# Xamalin
###



---

最新の情報に基づいて、.NET Core CLI で Xamarin.Forms テンプレートを直接利用する方法は現在サポートされていません。Xamarin.Forms テンプレートを利用する場合は、Visual Studio や Visual Studio for Mac を使用するのが一般的です。しかし、代替手段として、手動で Xamarin.Forms プロジェクトをセットアップする方法があります。以下にその手順を示します。

### 手動で Xamarin.Forms プロジェクトをセットアップする手順

1. **プロジェクトの作成**

    Xamarin.Forms プロジェクトを手動で作成します。

    ```bash
    dotnet new console -n MyApp.Console
    cd MyApp.Console
    ```

2. **プロジェクトに Xamarin.Forms パッケージを追加**

    Xamarin.Forms パッケージをプロジェクトに追加します。

    ```bash
    dotnet add package Xamarin.Forms
    ```

3. **プロジェクトを Xamarin.Forms に変更**

    プロジェクトファイル (`MyApp.Console.csproj`) を編集して、Xamarin.Forms を利用するように変更します。以下のように編集します。

    ```xml
    <Project Sdk="Microsoft.NET.Sdk">
      <PropertyGroup>
        <OutputType>Exe</OutputType>
        <TargetFramework>net6.0-android</TargetFramework> <!-- Android などのターゲットを指定 -->
      </PropertyGroup>
    
      <ItemGroup>
        <PackageReference Include="Xamarin.Forms" Version="5.0.0.2291" />
      </ItemGroup>
    </Project>
    ```

    `<TargetFramework>` を適切なプラットフォームに設定します（例: `net6.0-android`、`net6.0-ios`、`net6.0-windows` など）。

4. **MainPage.xaml と Main.cs の作成**

    Xamarin.Forms の構造を手動で作成します。以下は簡単な例です。

    - `MainPage.xaml`:

      ```xml
      <?xml version="1.0" encoding="utf-8" ?>
      <ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
                   xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
                   x:Class="MyApp.Console.MainPage">
          <StackLayout>
              <Label Text="Hello, World!" HorizontalOptions="Center" VerticalOptions="CenterAndExpand" />
          </StackLayout>
      </ContentPage>
      ```

    - `MainPage.xaml.cs`:

      ```csharp
      using Xamarin.Forms;

      namespace MyApp.Console
      {
          public partial class MainPage : ContentPage
          {
              public MainPage()
              {
                  InitializeComponent();
              }
          }
      }
      ```

    - `Program.cs`:

      ```csharp
      using Xamarin.Forms;

      namespace MyApp.Console
      {
          class Program
          {
              static void Main(string[] args)
              {
                  Xamarin.Forms.Forms.Init();
                  MainPage mainPage = new MainPage();
                  Xamarin.Forms.Application.Current.MainPage = mainPage;
                  Xamarin.Forms.Application.Current.Run();
              }
          }
      }
      ```

5. **ビルドと実行**

    ```bash
    dotnet build
    dotnet run
    ```

これで、手動で Xamarin.Forms プロジェクトを作成し、C# を使用して "Hello, World!" を表示する準備が整いました。ただし、実際にモバイルデバイスやエミュレータ上で実行する場合、特定のプラットフォーム（Android、iOS、Windows）に対して適切な設定と依存関係の管理が必要です。

---
```

% dotnet new xamarinforms -n myapp

Welcome to .NET 8.0!
---------------------
SDK Version: 8.0.302

Telemetry
---------
The .NET tools collect usage data in order to help us improve your experience. It is collected by Microsoft and shared with the community. You can opt-out of telemetry by setting the DOTNET_CLI_TELEMETRY_OPTOUT environment variable to '1' or 'true' using your favorite shell.

Read more about .NET CLI Tools telemetry: https://aka.ms/dotnet-cli-telemetry

----------------
Installed an ASP.NET Core HTTPS development certificate.
To trust the certificate, run 'dotnet dev-certs https --trust'
Learn about HTTPS: https://aka.ms/dotnet-https

----------------
Write your first app: https://aka.ms/dotnet-hello-world
Find out what's new: https://aka.ms/dotnet-whats-new
Explore documentation: https://aka.ms/dotnet-docs
Report issues and find source on GitHub: https://github.com/dotnet/core
Use 'dotnet --help' to see available commands or visit: https://aka.ms/dotnet-cli
--------------------------------------------------------------------------------------
An issue was encountered verifying workloads. For more information, run "dotnet workload update".
No templates or subcommands found matching: 'xamarinforms'.

To list installed templates similar to 'xamarinforms', run:
   dotnet new list xamarinforms
To search for the templates on NuGet.org, run:
   dotnet new search xamarinforms


For details on the exit code, refer to https://aka.ms/templating-exit-codes#103


```
---

Visual Studio Code (VS Code) を使用して、Xamarin.Forms を使った C# アプリケーションを作成し、Web に "Hello, World!" を表示する方法を説明します。

### 前提条件

- Visual Studio Code がインストールされていること。
- .NET Core SDK がインストールされていること。

### 手順

#### ステップ 1: Xamarin.Forms プロジェクトの作成

1. **ターミナルを開く**:
   - Visual Studio Code を起動し、ターミナルを開きます。

2. **Xamarin.Forms プロジェクトの作成**:
   - ターミナルで以下のコマンドを実行して、新しい Xamarin.Forms プロジェクトを作成します:
     ```
     dotnet new xamarinforms -n HelloWorldApp
     ```
   - これにより、`HelloWorldApp` という名前の Xamarin.Forms プロジェクトが作成されます。

3. **プロジェクトに移動**:
   - 作成したプロジェクトのディレクトリに移動します:
     ```
     cd HelloWorldApp
     ```

#### ステップ 2: MainPage.xaml の編集

1. **MainPage.xaml を編集**:
   - Visual Studio Code を使って、`MainPage.xaml` を開きます。
   - 以下のように XAML を編集して、"Hello, World!" のメッセージを表示するようにします:
     ```xml
     <?xml version="1.0" encoding="utf-8" ?>
     <ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
                  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
                  x:Class="HelloWorldApp.MainPage">
         <StackLayout>
             <Label Text="Hello, World!" HorizontalOptions="Center" VerticalOptions="CenterAndExpand" />
         </StackLayout>
     </ContentPage>
     ```

#### ステップ 3: Web プロジェクトの作成と実行

1. **Blazor WebAssembly プロジェクトの作成**:
   - 同じターミナルで、以下のコマンドを実行して Blazor WebAssembly プロジェクトを作成します:
     ```
     dotnet new blazorwasm -n HelloWorldWeb
     ```
   - これにより、`HelloWorldWeb` という名前の Blazor WebAssembly プロジェクトが作成されます。

2. **プロジェクトに移動**:
   - 作成した Web プロジェクトのディレクトリに移動します:
     ```
     cd HelloWorldWeb
     ```

3. **Xamarin.Forms プロジェクトへの参照追加**:
   - Blazor WebAssembly プロジェクトに Xamarin.Forms プロジェクトへの参照を追加します:
     ```
     dotnet add reference ../HelloWorldApp/HelloWorldApp.csproj
     ```

4. **プロジェクトのビルドと実行**:
   - 以下のコマンドで Blazor WebAssembly プロジェクトをビルドします:
     ```
     dotnet build
     ```
   - そして、以下のコマンドでプロジェクトを実行します:
     ```
     dotnet run
     ```
   - ブラウザで `https://localhost:5001` を開くと、"Hello, World!" のメッセージが表示されます。

### 注意点

- **Visual Studio Code の利用**: Visual Studio Code を使って、ターミナルで .NET Core コマンドを実行しています。
- **Blazor WebAssembly**: Xamarin.Forms のプロジェクトを Blazor WebAssembly プロジェクトに統合しています。これにより、Xamarin.Forms のコンポーネントを使って Web アプリケーションを構築できます。
- **デバッグとテスト**: VS Code ではデバッグとテストを効果的に行うための拡張機能が利用できます。

これで、Visual Studio Code を使って Xamarin.Forms と Blazor WebAssembly を組み合わせて "Hello, World!" を Web に表示する準備が整いました。

---

Xamarin.Formsを使用して、C#で「Hello, World!」というメッセージをWebに表示する方法を日本語で説明します。

### ステップ1: Xamarin.Forms プロジェクトの作成

1. **Visual Studioのインストール**:
   - Visual Studioをインストールし、.NETのモバイル開発ワークロードを有効にします。

2. **Xamarin.Forms プロジェクトの作成**:
   - Visual Studioを開きます。
   - `ファイル` > `新規作成` > `プロジェクト...` を選択します。
   - `モバイル` カテゴリーの中から `モバイル アプリ (Xamarin.Forms)` テンプレートを選択します。
   - プロジェクトの名前を入力（例: `HelloWorldApp`）、`作成` をクリックします。
   - テンプレートは `空 (Blank)` を選び、コード共有戦略は `.NET Standard` を選択します。
   - `作成` をクリックします。

### ステップ2: MainPage.xaml の編集

1. **MainPage.xaml を開く**:
   - Solution Explorerで、`HelloWorldApp`（またはプロジェクト名）の下にある `MainPage.xaml` を見つけます。

2. **XAML の編集**:
   - `MainPage.xaml` の内容を以下のように置き換えます:
     ```xml
     <?xml version="1.0" encoding="utf-8" ?>
     <ContentPage xmlns="http://xamarin.com/schemas/2014/forms"
                  xmlns:x="http://schemas.microsoft.com/winfx/2009/xaml"
                  x:Class="HelloWorldApp.MainPage">
         <StackLayout>
             <Label Text="こんにちは、世界！" HorizontalOptions="Center" VerticalOptions="CenterAndExpand" />
         </StackLayout>
     </ContentPage>
     ```

### ステップ3: ビルドと実行

1. **起動プロジェクトの設定**:
   - ソリューションを右クリックし、`起動プロジェクトの設定...` を選択します。
   - `複数の起動プロジェクト` を選択し、`HelloWorldApp` を `起動` に設定し、`HelloWorldApp.Server` も `起動` に設定します。

2. **プロジェクトの実行**:
   - `F5` キーを押すか、`開始` ボタンをクリックして、アプリケーションをビルドして実行します。
   - Visual Studio がアプリケーションを起動します。初めての場合は、準備に少し時間がかかる場合があります。

3. **結果の確認**:
   - アプリケーションが起動すると、画面の中央に「こんにちは、世界！」と表示されます。

### 注意点:

- **Blazor WebAssembly**: Xamarin.Forms は Blazor WebAssembly を介してWebにデプロイできます。プロジェクトを作成する際に、Blazor WebAssembly オプションを選択してください。
- **デバッグ**: デバッグは他の Xamarin.Forms プロジェクトと同様に動作します。ブレークポイントを設定したり、変数を確認したりすることができます。
- **公開**: 本番環境へのデプロイや他者との共有のために、Blazor WebAssembly のデプロイ方法に従う必要があります。

この手順は、Visual Studioを使用した場合の開発を想定しています。他のIDEやツールセットを使用する場合は、手順が若干異なる場合がありますが、基本的なコンセプトは同様です。

---
