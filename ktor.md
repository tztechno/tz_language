###
# ktor
###

---

Ktorは、Kotlin用のフレームワークで、サーバーやクライアントのアプリケーションを構築するためのものです。Ktorをインストールして使用するには、以下の手順に従います。

### 前提条件
1. Kotlinをインストールしていること。
2. IntelliJ IDEAなどのKotlin対応のIDEがインストールされていること。

### ステップ1: プロジェクトの作成
IntelliJ IDEAを使用して新しいKtorプロジェクトを作成します。

1. **IntelliJ IDEA**を開きます。
2. **New Project**を選択します。
3. **Kotlin**を選び、**Ktor**テンプレートを選択します。
4. 必要なプロジェクト情報を入力し、**Next**をクリックします。
5. 使用したいKtorの機能（Engineや、Serialization、Routingなど）を選択します。
6. **Finish**をクリックしてプロジェクトを作成します。

### ステップ2: Ktor依存関係の追加
`build.gradle.kts`ファイルに必要なKtorの依存関係を追加します。プロジェクト作成時にKtorを選択していれば自動的に追加されますが、手動で設定する場合の例を以下に示します。

```kotlin
plugins {
    kotlin("jvm") version "1.8.0"
    id("io.ktor.plugin") version "2.3.0"
}

group = "com.example"
version = "1.0.0"

application {
    mainClass.set("com.example.ApplicationKt")
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("io.ktor:ktor-server-core:2.3.0")
    implementation("io.ktor:ktor-server-netty:2.3.0")
    implementation("ch.qos.logback:logback-classic:1.2.3")
    testImplementation("io.ktor:ktor-server-tests:2.3.0")
    testImplementation("org.jetbrains.kotlin:kotlin-test-junit:1.8.0")
}
```

### ステップ3: サンプルアプリケーションの作成
以下はシンプルなKtorサーバーアプリケーションの例です。

`src/main/kotlin/com/example/Application.kt`に以下のコードを追加します。

```kotlin
package com.example

import io.ktor.application.*
import io.ktor.http.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*

fun main() {
    embeddedServer(Netty, port = 8080) {
        routing {
            get("/") {
                call.respondText("Hello, Ktor!", ContentType.Text.Plain)
            }
        }
    }.start(wait = true)
}
```

### ステップ4: アプリケーションの実行
IntelliJ IDEAでプロジェクトを開いた状態で、以下の手順を行います。

1. **Gradleタブ**を開きます（通常、右側のウィンドウにあります）。
2. プロジェクト名の下の**Tasks** > **application**を展開します。
3. **run**タスクをダブルクリックします。

または、メイン関数を右クリックして**Run 'ApplicationKt'**を選択します。

ブラウザで[http://localhost:8080] (http://localhost:8080) にアクセスすると、"Hello, Ktor!"というメッセージが表示されるはずです。

### まとめ
これで、Ktorを使用して簡単なサーバーアプリケーションをセットアップし、実行する方法を学びました。Ktorの詳細な機能や設定については、公式ドキュメントを参照してください。

---
