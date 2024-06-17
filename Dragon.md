###
# Dragon
###

---
4o

C++のフレームワークである「Dragon」をMacにインストールする手順について説明します。「Dragon Framework」は、軽量で高性能なC++フレームワークで、主にゲーム開発などに使用されます。以下に、一般的な手順を示します。

### 1. Homebrewのインストール
HomebrewはMac用のパッケージマネージャです。インストールされていない場合は、ターミナルを開いて以下のコマンドを実行してインストールします。

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### 2. 必要な依存パッケージのインストール
Dragon Frameworkを使用するために必要な依存パッケージをインストールします。これには、CMakeなどが含まれます。

```bash
brew install cmake
```

### 3. Dragon Frameworkのソースコードをダウンロード
Dragon FrameworkのソースコードをGitHubなどからダウンロードします。以下は、GitHubからクローンする例です。

```bash
git clone https://github.com/dragonframework/dragon.git
```

### 4. ビルドとインストール
クローンしたディレクトリに移動し、CMakeを使用してビルドします。

```bash
cd dragon
mkdir build
cd build
cmake ..
make
sudo make install
```

### 5. 環境変数の設定
ビルドとインストールが完了したら、必要に応じて環境変数を設定します。通常、`~/.bash_profile`や`~/.zshrc`ファイルにパスを追加します。

```bash
export DRAGON_HOME=/usr/local/dragon
export PATH=$DRAGON_HOME/bin:$PATH
```

これを反映させるために、ターミナルを再起動するか、以下のコマンドを実行します。

```bash
source ~/.bash_profile
# もしくは
source ~/.zshrc
```

### 6. 動作確認
正しくインストールされたかどうかを確認するために、以下のコマンドを実行します。

```bash
dragon --version
```

これでDragon Frameworkが正しくインストールされていれば、バージョン情報が表示されます。

以上が、MacにC++のDragon Frameworkをインストールする手順です。具体的な詳細や最新情報については、Dragon Frameworkの公式ドキュメントやリポジトリのREADMEを参照してください。

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
