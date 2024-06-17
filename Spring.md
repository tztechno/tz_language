###
# Spring
### 


---

JavaのSpringフレームワークをMacにインストールし、Visual Studio Code (VSCode)で使用する手順を以下に示します。

### 前提条件

1. **Java Development Kit (JDK)のインストール**
2. **Visual Studio Code (VSCode)のインストール**
3. **Apache MavenまたはGradleのインストール**

### ステップ1: JDKのインストール

まず、JDKがインストールされていることを確認します。インストールされていない場合は、以下の手順でインストールします。

1. **Homebrewのインストール**
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **OpenJDKのインストール**
   ```bash
   brew install openjdk@11
   ```

3. **環境変数の設定**
   ```bash
   echo 'export PATH="/usr/local/opt/openjdk@11/bin:$PATH"' >> ~/.zshrc
   source ~/.zshrc
   ```

### ステップ2: VSCodeのインストール

VSCodeがインストールされていない場合、[公式サイト](https://code.visualstudio.com/)からインストールします。

### ステップ3: Spring Initializrでプロジェクト作成

Spring Initializrを使用して、Springプロジェクトを簡単に作成します。

1. **Spring InitializrのWebサイトにアクセス**
   [Spring Initializr](https://start.spring.io/)にアクセスします。

2. **プロジェクトの設定**
   - Project: Maven Project or Gradle Project
   - Language: Java
   - Spring Boot: 最新バージョンを選択
   - Project Metadata:
     - Group: com.example
     - Artifact: demo
   - Dependencies: Web

3. **プロジェクトの生成**
   「Generate」ボタンをクリックしてプロジェクトを生成し、ZIPファイルをダウンロードします。

4. **プロジェクトの解凍**
   ダウンロードしたZIPファイルを解凍し、適当なディレクトリに配置します。

### ステップ4: VSCodeでプロジェクトを開く

1. **VSCodeを起動**
2. **プロジェクトフォルダを開く**
   - メニューから「File」 > 「Open Folder」を選択し、解凍したプロジェクトフォルダを選択します。

### ステップ5: VSCodeの拡張機能をインストール

VSCodeでJavaとSpring Bootの開発を行うために、以下の拡張機能をインストールします。

1. **Extension Pack for Java**
   - VSCodeの拡張機能パネル（左側の四つのブロックアイコン）を開き、`Extension Pack for Java`を検索してインストールします。

2. **Spring Boot Extension Pack**
   - 同様に、`Spring Boot Extension Pack`を検索してインストールします。

### ステップ6: プロジェクトのビルドと実行

1. **ターミナルを開く**
   - VSCodeのメニューから「Terminal」 > 「New Terminal」を選択します。

2. **プロジェクトのビルド**
   - Mavenプロジェクトの場合
     ```bash
     ./mvnw clean install
     ```
   - Gradleプロジェクトの場合
     ```bash
     ./gradlew build
     ```

3. **Spring Bootアプリケーションの実行**
   - Mavenプロジェクトの場合
     ```bash
     ./mvnw spring-boot:run
     ```
   - Gradleプロジェクトの場合
     ```bash
     ./gradlew bootRun
     ```

ブラウザで`http://localhost:8080`にアクセスして、Spring Bootアプリケーションが正常に起動していることを確認します。

以上で、MacにJavaのSpringフレームワークをインストールし、VSCodeで開発環境を整える手順は完了です。

---

Visual Studio Code (VS Code) でもSpringフレームワークを使用したJavaの開発は可能です。以下に、VS Codeを用いたSpring Bootプロジェクトのセットアップ手順を説明します。

### 1. JDKのインストール
まず、JDKをインストールします。最新のJDKをOracleの公式サイトまたはOpenJDKの公式サイトからダウンロードしてインストールしてください。

インストール確認
```
java -version
```
### 2. VS Codeのインストール
Visual Studio Codeの公式サイトからVS Codeをダウンロードしてインストールします。

### 3. 必要な拡張機能のインストール
VS CodeにはJava開発をサポートする拡張機能があります。以下の拡張機能をインストールしてください。
```
Java Extension Pack
Spring Boot Extension Pack
```
これらの拡張機能はVS CodeのExtensionsタブ（サイドバーの四角いアイコン）から検索してインストールできます。

### 4. Spring Initializrを使用してプロジェクトを作成
Spring Initializrを使用して、Spring Bootプロジェクトのひな形を作成します。

Spring Initializrのサイトにアクセスします。
https://start.spring.io/
必要な設定を行います。
```
Project: Maven Project
Language: Java
Spring Boot: 最新の安定バージョンを選択
Project Metadata:
Group: com.example
Artifact: demo
Dependencies: Spring Webなど必要な依存関係を追加します。
```
設定が完了したら、「Generate」ボタンをクリックして、プロジェクトをダウンロードします。

ダウンロードしたプロジェクトを解凍し、VS Codeで開きます。

### 5. Mavenの設定
プロジェクトをVS Codeで開いた後、必要なMavenの依存関係が自動的にダウンロードされます。pom.xmlファイルに依存関係が記述されています。
```
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <!-- 他の依存関係 -->
</dependencies>
```
### 6. Spring Bootアプリケーションの実行
プロジェクト内にDemoApplication.java（または作成したアプリケーション名のクラス）が生成されます。このクラスには@SpringBootApplicationアノテーションが付いており、Spring Bootアプリケーションのエントリーポイントとなります。

以下のように実行します。

```
@SpringBootApplication
public class DemoApplication {
    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
```
VS CodeのサイドバーにあるRunタブ（再生アイコン）をクリックし、DemoApplicationを選択して実行します。これにより、Spring Bootアプリケーションが起動します。

### 7. 確認
ブラウザを開いて http://localhost:8080 にアクセスし、アプリケーションが正しく起動していることを確認します。

---
