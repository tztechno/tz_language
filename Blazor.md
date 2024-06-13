###
# Blazor
###


---

Blazor WebAssembly アプリケーション（`myapp`）と ASP.NET Core API を連携させるためには、以下の手順を実行する必要があります。

### 手順概要

1. **ASP.NET Core API の作成と設定**
   - ASP.NET Core で RESTful API を作成します。これには、GET や POST メソッドを含むエンドポイントが必要です。
   - CORS (Cross-Origin Resource Sharing) を設定して、Blazor WebAssembly アプリケーションから API にアクセスできるようにします。

2. **Blazor WebAssembly アプリケーションから API へのアクセス**
   - Blazor WebAssembly アプリケーション内で、HttpClient を使用して API にリクエストを送信します。
   - API からの応答を処理し、必要な情報を画面に表示します。

### 詳細な手順

#### 1. ASP.NET Core API の作成と設定

まず、ASP.NET Core で API を作成します。以下は、簡単な例です。

- **Startup.cs**:
  ```csharp
  using Microsoft.AspNetCore.Builder;
  using Microsoft.AspNetCore.Hosting;
  using Microsoft.Extensions.Configuration;
  using Microsoft.Extensions.DependencyInjection;
  using Microsoft.Extensions.Hosting;

  namespace MyApi
  {
      public class Startup
      {
          public Startup(IConfiguration configuration)
          {
              Configuration = configuration;
          }

          public IConfiguration Configuration { get; }

          public void ConfigureServices(IServiceCollection services)
          {
              services.AddControllers();
              services.AddCors(options =>
              {
                  options.AddPolicy("CorsPolicy",
                      builder => builder
                          .AllowAnyOrigin()
                          .AllowAnyMethod()
                          .AllowAnyHeader());
              });
          }

          public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
          {
              if (env.IsDevelopment())
              {
                  app.UseDeveloperExceptionPage();
              }

              app.UseRouting();

              app.UseCors("CorsPolicy");

              app.UseEndpoints(endpoints =>
              {
                  endpoints.MapControllers();
              });
          }
      }
  }
  ```

- **CalculateController.cs**:
  ```csharp
  using Microsoft.AspNetCore.Mvc;

  namespace MyApi.Controllers
  {
      [ApiController]
      [Route("api/[controller]")]
      public class CalculateController : ControllerBase
      {
          [HttpPost]
          public IActionResult Post([FromBody] CalculationRequest request)
          {
              // Perform calculations
              int result = CalculateLucasNumber(request.N);

              // Return result
              return Ok(new
              {
                  Result = result,
                  ProcessTime = 100 // Example process time in milliseconds
              });
          }

          private int CalculateLucasNumber(int n)
          {
              // Implement your calculation logic here
              // This is just a placeholder example
              if (n == 0)
                  return 2;
              else if (n == 1)
                  return 1;
              else
                  return CalculateLucasNumber(n - 1) + CalculateLucasNumber(n - 2);
          }

          public class CalculationRequest
          {
              public int N { get; set; }
          }
      }
  }
  ```

#### 2. Blazor WebAssembly アプリケーションから API へのアクセス

Blazor WebAssembly アプリケーションからは、`HttpClient` を使用して API にリクエストを送信します。例えば、`FetchData.razor` で以下のように実装できます。

- **FetchData.razor**:
  ```razor
  @page "/fetchdata"
  @using System.Net.Http
  @inject HttpClient Http

  <h3>Fetch Data</h3>

  <input type="number" @bind="n" placeholder="Enter a number" />
  <button @onclick="Calculate">Calculate</button>

  <div>
      @if (result != null)
      {
          <p>Lucas Number L@n = @result.Result</p>
          <p>Time: @((double)result.ProcessTime / 1000) sec</p>
      }
  </div>

  @code {
      int n;
      dynamic result;

      private async Task Calculate()
      {
          var response = await Http.PostAsJsonAsync("http://localhost:5000/api/calculate", new { n });
          response.EnsureSuccessStatusCode();
          result = await response.Content.ReadFromJsonAsync<object>();
      }
  }
  ```

この例では、`FetchData.razor` が `http://localhost:5000/api/calculate` に対して POST リクエストを送信し、計算結果を取得して表示します。実際のアプリケーションでは、URLやリクエスト・レスポンスの形式を適切に調整してください。

### 注意点

- CORS を適切に設定していない場合、ブラウザが API へのアクセスをブロックする可能性があります。API サーバー側で CORS ポリシーを設定して、Blazor WebAssembly アプリケーションのオリジンを許可するようにしてください。
- リクエストとレスポンスの形式やエラーハンドリングなど、実際のアプリケーションに合わせて適切に調整してください。

これらの手順に従うことで、Blazor WebAssembly アプリケーションとサーバーサイドの ASP.NET Core API を連携させる準備が整います。

---

`ajax.html` を使用して、Blazor WebAssembly アプリケーションから計算を実行し、結果を取得する方法を説明します。

### Backend の準備

1. **ASP.NET Core Backend の作成**

   Backend として、ASP.NET Core を使用して Lucas 数の計算を行います。以下は、簡単なサンプルです。

   ```csharp
   // Startup.cs

   using Microsoft.AspNetCore.Builder;
   using Microsoft.AspNetCore.Hosting;
   using Microsoft.Extensions.DependencyInjection;
   using Microsoft.Extensions.Hosting;
   using System.Diagnostics;
   using System.Threading.Tasks;

   namespace LucasNumberCalculatorBackend
   {
       public class Startup
       {
           public void ConfigureServices(IServiceCollection services)
           {
               services.AddControllers();
           }

           public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
           {
               if (env.IsDevelopment())
               {
                   app.UseDeveloperExceptionPage();
               }

               app.UseRouting();

               app.UseEndpoints(endpoints =>
               {
                   endpoints.MapControllers();
               });
           }
       }
   }
   ```

2. **Lucas 数の計算と時間計測**

   Lucas 数を計算し、処理時間を返すコントローラーを作成します。

   ```csharp
   // Controllers/CalculateController.cs

   using Microsoft.AspNetCore.Mvc;
   using System;
   using System.Diagnostics;
   using System.Threading.Tasks;

   namespace LucasNumberCalculatorBackend.Controllers
   {
       [Route("[controller]")]
       [ApiController]
       public class CalculateController : ControllerBase
       {
           [HttpPost]
           public async Task<IActionResult> CalculateLucasNumber([FromBody] CalculateRequest request)
           {
               int n = request.N;

               // 計算開始時間を記録
               Stopwatch stopwatch = Stopwatch.StartNew();

               // Lucas 数を計算する（ここでは簡易的な実装）
               long result = CalculateLucas(n);

               // 計算時間をミリ秒で取得
               long elapsedMilliseconds = stopwatch.ElapsedMilliseconds;

               // 結果と計算時間を返す
               var response = new
               {
                   result,
                   process_time = elapsedMilliseconds
               };

               return Ok(response);
           }

           private long CalculateLucas(int n)
           {
               if (n == 0)
                   return 2;
               else if (n == 1)
                   return 1;

               long a = 2;
               long b = 1;
               long c = 0;

               for (int i = 2; i <= n; i++)
               {
                   c = a + b;
                   a = b;
                   b = c;
               }

               return c;
           }
       }

       public class CalculateRequest
       {
           public int N { get; set; }
       }
   }
   ```

   - `CalculateLucas` メソッドでは、Lucas 数を計算しています。
   - `CalculateLucasNumber` アクションメソッドでは、POST リクエストを受け取り、計算結果と処理時間を JSON 形式で返します。

### Frontend の準備

`ajax.html` ファイルを使用して、Blazor WebAssembly アプリケーションから計算リクエストを送信し、結果を受け取る JavaScript を実装します。

```html
<!DOCTYPE html>
<html>
<head>
    <title>Lucas Number Calculator</title>
</head>
<body>
    <p>AJAX Lucas Number</p>
    <input type="number" id="inputN" placeholder="Enter a number">
    <button onclick="sendRequest()">Calculate</button>
    <div id="result"></div>
    <div id="time"></div>

    <script>
        function sendRequest() {
            const n = document.getElementById('inputN').value;
            fetch('/calculate', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ N: parseInt(n) })
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json();
            })
            .then(data => {
                document.getElementById('result').innerText = `Lucas Number L${n} = ${data.result}`;
                document.getElementById('time').innerText = `Time: ${(data.process_time / 1000).toFixed(3)} sec`;
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    </script>
</body>
</html>
```

### 動作の確認

1. **ASP.NET Core アプリケーションの起動**

   ASP.NET Core アプリケーションを起動し、`http://localhost:5000` でアクセス可能にします。

2. **ブラウザで `ajax.html` を開く**

   ブラウザで `ajax.html` を開き、数値を入力して「Calculate」ボタンをクリックすると、Blazor WebAssembly アプリケーションに対して計算リクエストが送信され、結果が表示されます。

このようにして、Blazor WebAssembly アプリケーションと ASP.NET Core Backend を連携させて、Lucas 数の計算と計算時間の取得を行うことができます。

---

Blazor WebAssembly アプリケーション (ここでは `MyApp` という名前のプロジェクトとして想定します) の一般的なファイル階層を示します。これは、プロジェクトの基本的な構成に基づいています。Blazor WebAssembly プロジェクトは、クライアントサイドで動作し、ASP.NET Core サーバーではなく、静的ファイルホスティングサーバーにデプロイされることが一般的です。

以下は、`MyApp` プロジェクトのファイル階層の例です。

```
MyApp/
│
├── wwwroot/             <-- 静的リソースを配置するディレクトリ
│   ├── index.html       <-- アプリケーションのエントリーポイント
│   ├── favicon.ico      <-- ファビコン (お好みで)
│   └── css/
│       └── app.css      <-- アプリケーション用の CSS ファイル
│
├── Pages/               <-- Blazor ページやコンポーネントを配置するディレクトリ
│   ├── Index.razor      <-- ホームページのコンポーネント
│   ├── Counter.razor    <-- カウンターのコンポーネント (例)
│   └── FetchData.razor  <-- データの取得や表示を行うコンポーネント (例)
│
├── Shared/              <-- 共有コンポーネントを配置するディレクトリ
│   └── MainLayout.razor <-- メインレイアウト用のコンポーネント
│
├── _Imports.razor       <-- コンポーネントの名前空間をインポートするファイル
├── App.razor            <-- アプリケーションのルートとなるコンポーネント
├── App.razor.csproj     <-- プロジェクトファイル (Visual Studio で生成される場合)
├── Program.cs           <-- Blazor アプリケーションのエントリーポイント
└── Startup.cs           <-- アプリケーションの構成とサービスの設定
```

この構成では、主要なファイルとディレクトリは次のようになっています：

- **`wwwroot/`**: このディレクトリには静的リソースが配置されます。例えば、`index.html` はアプリケーションのエントリーポイントとして機能します。また、CSS ファイルやイメージファイルなどもここに配置します。

- **`Pages/`**: Blazor のページやコンポーネントが配置されるディレクトリです。例えば、`Index.razor` はホームページのコンポーネント、`Counter.razor` はカウンターの例です。FetchData.razor のようなデータの取得や表示を行うコンポーネントもここに作成します。

- **`Shared/`**: 共有コンポーネントが配置されるディレクトリです。例えば、`MainLayout.razor` はアプリケーション全体のメインレイアウトを定義するために使用されます。

- **`_Imports.razor`**: コンポーネントで使用する名前空間をインポートするファイルです。例えば、`@using MyApp.Pages` のように、ページやコンポーネントの名前空間をここでインポートします。

- **`App.razor`**: アプリケーションのルートとなるコンポーネントです。ここでルーティングやメインレイアウトを設定し、アプリケーション全体の挙動を定義します。

- **`Program.cs`**: Blazor アプリケーションのエントリーポイントです。ここでアプリケーションの起動と設定を行います。

- **`Startup.cs`**: アプリケーションの構成とサービスの設定を行うクラスです。依存性の注入やルーティングの設定などをここで行います。

これらのファイルとディレクトリ構造を使って、Blazor WebAssembly アプリケーションを構築し、各コンポーネントやページの役割に応じて適切なファイルにコードを配置していきます。

---

Blazor アプリケーションのルートに `ajax.html` を置いた場合、それを表示するにはいくつかの方法があります。Blazor は基本的にサーバーサイドで動作するため、静的な HTML ファイルをそのままブラウザで表示することはできませんが、いくつかのアプローチで表示することができます。

### 方法1: 静的ファイルを直接参照する方法

1. **Blazor WebAssembly (クライアントサイド) の場合**:

   Blazor WebAssembly の場合、静的ファイルは `wwwroot` フォルダに配置します。ただし、`wwwroot` フォルダがなくてもルートに配置することはできますが、その場合のファイルパスは異なります。

   - `wwwroot` フォルダがない場合は、プロジェクトのルートに `ajax.html` を置きます。

   - ブラウザで直接ファイルにアクセスする場合、例えば `http://localhost:5000/ajax.html` のように、Blazor アプリケーションのルートからのパスでアクセスします。

2. **Blazor Server (サーバーサイド) の場合**:

   Blazor Server の場合、静的ファイルをそのまま表示することはできませんが、Blazor アプリケーション内でファイルを参照する方法があります。

   - 例えば、Blazor Server アプリケーション内の Razor ページで `<iframe>` を使用して、`ajax.html` を表示することができます。

     ```html
     <iframe src="/ajax.html" width="100%" height="600"></iframe>
     ```

     この場合、`src` 属性のパスはアプリケーションのルートからの相対パスになります。

### 方法2: API 経由で表示する方法

もう一つの方法として、Blazor アプリケーションで C# コードを使用して、`ajax.html` の内容を取得して表示する方法があります。これには以下の手順が必要です。

1. **Blazor WebAssembly (クライアントサイド) の場合**:

   - `HttpClient` を使用して、サーバーから `ajax.html` を取得し、その内容を Blazor のコンポーネントで表示します。

     ```csharp
     @page "/ajax"
     @inject HttpClient Http

     <h3>Ajax Content</h3>
     <div>
         @content
     </div>

     @code {
         string content;

         protected override async Task OnInitializedAsync()
         {
             content = await Http.GetStringAsync("/ajax.html");
         }
     }
     ```

   - `OnInitializedAsync` メソッドで、`HttpClient` を使用して `ajax.html` の内容を取得し、`content` 変数に格納します。その後、Blazor のコンポーネント内で `content` を表示します。

2. **Blazor Server (サーバーサイド) の場合**:

   - 同様に、Blazor Server でも `HttpClient` を使用してサーバーから `ajax.html` の内容を取得し、コンポーネントで表示することができます。

Blazor では、静的な HTML ファイルをそのまま表示する場合よりも、データの取得や処理が必要な場合に API を介して処理する方が一般的です。以上の方法を参考に、Blazor アプリケーションで `ajax.html` を表示する方法を選択してください。

---

Blazor アプリケーションの中で、静的な HTML ファイル (`ajax.html` など) をホストする方法について説明します。Blazor は基本的にサーバーサイドの Web アプリケーションですが、静的コンテンツを追加することも可能です。

### 静的ファイルの追加とホスティング方法

Blazor プロジェクトに静的な HTML ファイルを追加して、それをホストする手順を以下に示します。

1. **静的ファイルの追加**

   まず、Blazor プロジェクトに `ajax.html` ファイルを追加します。

   - Visual Studio を使用している場合、プロジェクトのルートまたは任意の場所に `ajax.html` ファイルを追加します。右クリックでメニューから `追加` > `新しいアイテム` を選択し、`HTML ページ` を選んで作成します。

   - .NET CLI を使用している場合は、コマンドラインから以下のコマンドを実行します。

     ```bash
     dotnet new file -n ajax.html
     ```

     これにより、`ajax.html` ファイルがプロジェクトに追加されます。

2. **静的ファイルのホスティング設定**

   Blazor は通常、サーバーサイドで動作しますが、静的ファイルをホストする方法はいくつかあります。

   - **Blazor WebAssembly (クライアントサイド)**:
     Blazor WebAssembly では、静的ファイルはクライアントに配信されます。`wwwroot` フォルダにファイルを配置すると、それらは自動的に公開されます。

     1. `wwwroot` フォルダがプロジェクトにない場合は、作成します。

     2. `wwwroot` フォルダに `ajax.html` ファイルを移動またはコピーします。

     3. ブラウザで `http://localhost:{ポート番号}/ajax.html` を開くと、Blazor アプリケーションのルートから `ajax.html` ファイルにアクセスできます。

   - **Blazor Server (サーバーサイド)**:
     Blazor Server アプリケーションでは、静的ファイルを公開するために、`wwwroot` フォルダの使用が推奨されます。しかし、Blazor Server の場合、サーバーサイドの機能を使用して静的ファイルを提供する必要があります。

     例えば、`Pages` フォルダにカスタムの Razor ページを作成し、そこから静的ファイルをレンダリングする方法があります。

### 静的ファイルの利用に関する注意点

- Blazor アプリケーションで静的ファイルを使用する場合、セキュリティの観点から注意が必要です。特に、悪意のあるコードが埋め込まれるリスクがあるため、信頼できるソースからのみ静的ファイルを取得するようにしてください。
- 開発と本番環境での設定は異なる場合があります。本番環境では静的ファイルのセキュリティやパフォーマンスを最適化するための設定が必要です。

静的な HTML ファイルを Blazor アプリケーションに統合する方法として、上記の手順を参考にしてください。

---

このエラーは、ブラウザが `localhost` に対して安全な接続を確立できない場合に表示されるものです。一般的に、以下のような理由が考えられます。

### 可能性のある原因と対処方法

1. **HTTPS 接続が必要な設定の場合**:
   - 最近のブラウザでは、特にセキュリティ要件が厳しい状況では HTTPS 接続が必須となることがあります。しかし、開発中のローカル環境では自己署名証明書や開発者向けの証明書を使用して安全な接続を確立することができます。

2. **ASP.NET Core アプリケーションの HTTPS 設定**:
   - Blazor WebAssembly アプリケーションを実行する場合、デフォルトでは HTTPS 接続が有効になっていることがあります。デバッグ時には `dotnet run` を使用すると、自動的に HTTPS が設定されますが、自己署名証明書が使用されます。
   - ブラウザで開発用の自己署名証明書を信頼するように設定するか、開発用途であれば HTTPS の要件を緩める方法もあります。

### 対処方法

以下の手順を試してみてください。

1. **HTTPS を使用する設定の場合**:
   - Visual Studio で開発している場合、デフォルトで HTTPS が有効になっていることがあります。この場合、ブラウザが自己署名証明書を信頼できるように設定します。
   - Visual Studio の場合、プロジェクトのプロパティで `SSL を使用` にチェックを入れて、使用するポートを確認します。

2. **HTTP を使用する設定の場合**:
   - 開発環境でセキュリティが問題にならない場合、HTTP 接続を使用することもできます。これは開発中に限定され、実稼働環境では推奨されません。

3. **ブラウザの設定変更**:
   - ブラウザのセキュリティ設定で、ローカルホストや自己署名証明書を信頼するように設定を変更します。
   - 一時的に安全でない接続を許可する場合、ブラウザのエラーメッセージに表示されているリンクや詳細をクリックし、詳細設定を変更します。

4. **ブラウザのエラーメッセージの確認**:
   - ブラウザのエラーメッセージには、具体的な原因や許可するための手順が示されることがあります。メッセージをよく読んで、必要な設定や対応を行います。

ブラウザのエラーメッセージや開発環境の設定に応じて、適切な対処方法を選択してください。特に開発中のローカル環境では、セキュリティの設定を緩和することが一時的な解決策となる場合がありますが、実際の運用では適切なセキュリティ設定を行うことが重要です。

---

Blazor を使用して C# で Web アプリケーションを作成し、"Hello, World!" を表示する手順を説明します。

### 手順

1. **Blazor プロジェクトの作成**

   Blazor プロジェクトを作成するためには、.NET CLI を使用します。以下の手順に従ってください。

   - **コマンドラインでプロジェクトを作成**:
     Blazor WebAssembly プロジェクトを作成する場合、以下のコマンドを使用します。

     ```bash
     dotnet new blazorwasm -n HelloWorldBlazorApp
     cd HelloWorldBlazorApp
     ```

     これにより、`HelloWorldBlazorApp` という名前の Blazor WebAssembly プロジェクトが作成されます。

2. **プロジェクトのビルドと実行**

   - **ビルド**:
     ```bash
     dotnet build
     ```

   - **実行**:
     ```bash
     dotnet run
     ```

     ブラウザで `https://localhost:5001` を開くと、Blazor アプリケーションが表示されます。

3. **Hello, World! を表示する**

   - **ページの作成**:
     `Pages` フォルダ内に新しい Razor ページを作成します。例えば、`Index.razor` を作成します。

     ```razor
     @page "/"
     <h1>Hello, World! from Blazor</h1>
     ```

   - **表示**:
     ブラウザで `https://localhost:5001` を開き、"Hello, World! from Blazor" というメッセージが表示されます。

### 注意点

- Blazor は、WebAssembly を使用してブラウザ上で動作する C# のフレームワークです。これにより、サーバサイドで C# を使用してクライアントサイドの Web アプリケーションを構築できます。
- Blazor WebAssembly はクライアント側で動作するため、Web ブラウザを通じてユーザに直接表示されます。
- 上記の手順では、最小限の "Hello, World!" を表示するだけの例を示しています。Blazor では、より複雑なアプリケーションを構築するための多くの機能やコンポーネントが提供されています。

これで、Blazor を使用して C# で Web アプリケーションを構築し、ブラウザ上で "Hello, World!" を表示する方法がわかりました。

---
