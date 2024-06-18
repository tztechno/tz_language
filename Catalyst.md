###
# Catalyst
###

---

PerlのWebフレームワークであるCatalystを使用して、指定のHTMLをホストする方法について説明します。

### Catalystのセットアップ

まず、Catalystをセットアップします。Perlのバージョンは5.14以上を推奨します。

1. **Catalystのインストール**:

   Catalystをインストールするには、CPANモジュールを使用します。ターミナルで以下のコマンドを実行します。

   ```bash
   cpan Catalyst::Runtime
   ```

   Catalystが正常にインストールされると、`catalyst` コマンドが使用可能になります。

2. **新しいCatalystアプリケーションの作成**:

   新しいCatalystアプリケーションを作成します。

   ```bash
   catalyst.pl MyApp
   cd MyApp
   ```

   ここで `MyApp` はアプリケーションの名前です。ディレクトリに移動してから、依存関係をインストールします。

   ```bash
   cpanm Catalyst::Devel
   ```

### 指定のHTMLをホストする方法

次に、Catalystアプリケーションを設定して指定のHTMLファイルをホストする手順を示します。

1. **HTMLファイルの配置**:

   Catalystの `root` ディレクトリにHTMLファイルを配置します。通常、`MyApp/root` ディレクトリがルートディレクトリとなります。

   ```bash
   mkdir root/static   # 静的ファイル用ディレクトリを作成
   cp path/to/your/index.html root/static/index.html
   ```

   ここで `path/to/your/index.html` は、ホストしたいHTMLファイルのパスです。

2. **Catalystアクションの作成**:

   Catalystで静的ファイルをサーブするために、`MyApp/lib/MyApp/Controller/Root.pm` などの適切なコントローラーファイルにアクションを追加します。

   ```perl
   package MyApp::Controller::Root;

   use Moose;
   use namespace::autoclean;

   BEGIN { extends 'Catalyst::Controller' }

   # ルートパスへのアクセスでindex.htmlを表示するアクション
   sub index :Path('/') Args(0) {
       my ($self, $c) = @_;
       $c->serve_static_file('index.html');
   }

   __PACKAGE__->meta->make_immutable;

   1;
   ```

   この例では、ルートパス (`/`) にアクセスがあった場合に `index.html` を表示するアクションを定義しています。

3. **サーバーの起動**:

   Catalystアプリケーションをビルドしてサーバーを起動します。

   ```bash
   perl Makefile.PL
   make
   ./script/myapp_server.pl
   ```

   `myapp_server.pl` の部分は、実際に生成されたスクリプトの名前になります。

4. **アクセス**:

   ブラウザで `http://localhost:3000` にアクセスすると、指定したHTMLファイルが表示されるはずです。

### 注意点

- Catalystでは、静的ファイルを `serve_static_file` メソッドを使用して簡単にサーブすることができますが、より複雑なアプリケーションの場合はルーティングやテンプレートエンジンなどの機能も活用することができます。

- セキュリティの観点から、公開するHTMLファイルには注意してください。必要に応じてアクセス制御やその他のセキュリティ対策を施すことが推奨されます。

これで、PerlのCatalystフレームワークを使用して指定のHTMLをホストする方法が理解できたかと思います。


---
