###
# Dragon
###

---

## projectフォルダのルートにFrame Dragonライブラリフォルダが必要な理由

Frame Dragonは、C++開発向けのフレームワークとライブラリのセットです。Frame Dragonを使用するには、プロジェクトフォルダのルートにFrame Dragonライブラリフォルダを配置する必要があります。

これは、Frame Dragonのヘッダーファイルやライブラリファイルにアクセスするために必要です。Frame Dragonライブラリフォルダを配置することで、プロジェクト内のソースコードからこれらのファイルに簡単にアクセスできるようになります。

**具体的な手順**

1. Frame Dragonをインストールします。

```
brew install framedragon
```

2. Frame Dragonライブラリフォルダをプロジェクトフォルダのルートに配置します。

```
cd ~/project-folder
curl -sSL https://raw.githubusercontent.com/framedragon/framedragon/master/install.sh | bash
```

上記のコマンドを実行すると、`framedragon`という名前のフォルダがプロジェクトフォルダのルートに作成されます。このフォルダには、Frame Dragonのヘッダーファイルやライブラリファイルが含まれています。

3. プロジェクトのヘッダーファイルにFrame Dragonのヘッダーファイルをインクルードします。

```c++
#include <framedragon/core.hpp>
```

4. プロジェクトにFrame Dragonライブラリをリンクします。

```c++
#include <framedragon/core.hpp>

int main() {
  // Frame Dragonのライブラリを使用するコード
  return 0;
}
```

**補足**

* 上記のコマンドは、Homebrewがインストールされていることを前提としています。Homebrewがインストールされていない場合は、[Homebrewのインストール方法]([無効な URL を削除しました]。
* Frame Dragonライブラリフォルダを配置する場所は、プロジェクトフォルダのルートである必要はありません。ただし、プロジェクト内のソースコードから簡単にアクセスできる場所に配置する必要があります。
* Frame Dragonの詳細については、[Frame Dragonのドキュメント]([無効な URL を削除しました]。


---

## MacにC++用Frame Dragonをインストールする方法

Frame Dragonは、C++開発向けのフレームワークとライブラリのセットです。MacにFrame Dragonをインストールするには、以下の手順に従ってください。

**1. Homebrewのインストール**

Frame Dragonをインストールするには、まずHomebrewと呼ばれるパッケージマネージャーをインストールする必要があります。Homebrewは、Macにソフトウェアを簡単にインストールするためのツールです。

Homebrewをインストールするには、以下のコマンドをターミナルに入力します。

```
/bin/bash -c "$(curl -fsSL https://docs.brew.sh/FAQ)"
```

**2. Frame Dragonのインストール**

Homebrewがインストールされたら、以下のコマンドを使用してFrame Dragonをインストールできます。

```
brew install framedragon
```

**3. フレームワークのインクルード**

Frame Dragonを使用するには、プロジェクトのヘッダーファイルにFrame Dragonのヘッダーファイルをインクルードする必要があります。

```c++
#include <framedragon/core.hpp>
```

**4. ライブラリの使用**

Frame Dragonのライブラリを使用するには、プロジェクトにライブラリをリンクする必要があります。

```c++
#include <framedragon/core.hpp>

int main() {
  // Frame Dragonのライブラリを使用するコード
  return 0;
}
```

**詳細情報**

Frame Dragonの詳細については、[Frame Dragonのドキュメント]([無効な URL を削除しました]。

**補足**

* Frame Dragonは、C++20以降が必要です。
* macOS 10.14以降が必要です。

**参考情報**

* [Homebrew](https://brew.sh/)
* Frame Dragon [無効な URL を削除しました]


---
