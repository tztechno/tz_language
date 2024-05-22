###
# Spring
### 

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
