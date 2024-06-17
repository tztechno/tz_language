###
# Crow
###

---

MacでC++のフレームワークであるCrowをインストールする手順は以下の通りです。

1. Homebrewのインストール
まず、MacにHomebrewがインストールされていることを確認します。ターミナルを開き、以下のコマンドを実行します。

```
brew --version
```

Homebrewがインストールされていない場合は、以下のコマンドを実行してインストールします。

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Crowのインストール
Homebrewを使ってCrowをインストールします。ターミナルで以下のコマンドを実行します。

```
brew install crow
```

3. Crowのセットアップ
Crowをプロジェクトで使用するには、以下のステップを実行します。

a. プロジェクトのディレクトリに移動します。

b. `crow_all.h`をインクルードします。
```cpp
#include <crow.h>
```

c. コンパイル時に`-lcrow`フラグを追加します。
```
g++ your_file.cpp -o your_program -lcrow
```

これで、MacでCrowを使ってC++のWebアプリケーションを開発することができます。

サンプルコード:
```cpp
#include <crow.h>

int main()
{
    crow::SimpleApp app;

    CROW_ROUTE(app, "/")([](){
        return "Hello, world!";
    });

    app.port(18080).run();
}
```

上記のコードを実行すると、ローカルホストのポート18080でWebサーバーが起動します。ブラウザで `http://localhost:18080` にアクセスすると、"Hello, world!"が表示されます。

---
