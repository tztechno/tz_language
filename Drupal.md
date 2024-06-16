###
# Drupal
###

---
4o

Drupalをインストールするための手順は、いくつかのステップに分かれています。以下に、一般的なインストール方法を示します。

### 1. システム要件の確認
Drupalのインストール前に、以下の要件を満たしていることを確認します：
- **Webサーバー**: Apache, Nginxなど
- **PHP**: Drupal 9の場合、PHP 7.3以降
- **データベース**: MySQL、MariaDB、PostgreSQL、SQLite

### 2. 必要なパッケージのインストール
以下は、Ubuntuを使用している場合の例です。他のLinuxディストリビューションやWindowsでも類似の手順を実行します。

```bash
sudo apt update
sudo apt install apache2
sudo apt install mysql-server
sudo apt install php libapache2-mod-php php-mysql php-xml php-gd php-mbstring php-curl php-zip
```

### 3. データベースの設定
データベースを作成し、ユーザーを設定します。

```bash
sudo mysql -u root -p
```

以下のSQLコマンドを実行します：

```sql
CREATE DATABASE drupal;
CREATE USER 'drupaluser'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON drupal.* TO 'drupaluser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 4. Drupalのダウンロード
公式サイトからDrupalをダウンロードして解凍します。

```bash
cd /var/www/html
sudo wget https://www.drupal.org/download-latest/tar.gz
sudo tar -xzvf tar.gz
sudo mv drupal-x.x.x drupal
```

### 5. ファイルの権限設定
Drupalディレクトリに適切な権限を設定します。

```bash
sudo chown -R www-data:www-data /var/www/html/drupal
sudo chmod -R 755 /var/www/html/drupal
```

### 6. Apacheの設定
新しい仮想ホスト設定ファイルを作成します。

```bash
sudo nano /etc/apache2/sites-available/drupal.conf
```

以下の内容をファイルに追加します：

```apache
<VirtualHost *:80>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/html/drupal
    <Directory /var/www/html/drupal>
        Options Indexes FollowSymLinks
        AllowOverride All
        Require all granted
    </Directory>
    ErrorLog ${APACHE_LOG_DIR}/drupal_error.log
    CustomLog ${APACHE_LOG_DIR}/drupal_access.log combined
</VirtualHost>
```

設定ファイルを有効にしてApacheを再起動します：

```bash
sudo a2ensite drupal.conf
sudo a2enmod rewrite
sudo systemctl restart apache2
```

### 7. Drupalのインストール
ブラウザを開き、`http://your_server_ip/drupal`にアクセスします。インストール画面が表示されるので、指示に従ってインストールを進めます。

1. **言語の選択**: 使用する言語を選択します。
2. **インストールプロファイルの選択**: 標準インストールを選択します。
3. **データベースの設定**: 前述のデータベース情報を入力します。
4. **サイト情報の設定**: サイト名、管理者アカウント情報などを入力します。

### 8. インストール完了
インストールが完了したら、サイトにアクセスして正常に動作するか確認します。

これでDrupalのインストールは完了です。問題が発生した場合は、公式ドキュメントやサポートフォーラムを参照してください。


---

- aptが使えない?
- dupalがinstallできない?
- mysqlがinstallできない?

---
```
% sudo apt update
```
The operation couldn’t be completed. Unable to locate a Java Runtime that supports apt.
Please visit http://www.java.com for information on installing Java.

---
```
% java --version
java 21 2023-09-19 LTS
Java(TM) SE Runtime Environment (build 21+35-LTS-2513)
Java HotSpot(TM) 64-Bit Server VM (build 21+35-LTS-2513, mixed mode, sharing)
```
javaはinstallされている

---

PHPとDrupalの環境をインストールする方法はいくつかありますが、最も一般的な方法の一つは以下の手順です。

Webサーバーのセットアップ: ApacheやNginxなどのWebサーバーをインストールします。これらのサーバーは、Drupalを実行するために必要です。Apacheをインストールする場合は、次のコマンドを使用します。
```
sudo apt update
sudo apt install apache2
```
PHPのインストール: DrupalはPHPで動作しますので、PHPをインストールする必要があります。以下のコマンドでPHPをインストールします。
```
sudo apt install php php-mysql php-gd php-mbstring php-xml
```
MySQLデータベースのセットアップ: Drupalはデータベースを使用していますので、MySQLやMariaDBなどのデータベースをインストールし、データベースを作成します。
```
sudo apt install mysql-server
```
そして、MySQLにrootパスワードを設定し、Drupal用のデータベースとユーザーを作成します。

```
mysql -u root -p
CREATE DATABASE drupal_database;
CREATE USER 'drupal_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON drupal_database.* TO 'drupal_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```
Drupalのダウンロードと設定: Drupalの公式ウェブサイトから最新のDrupalバージョンをダウンロードし、Webサーバーのドキュメントルートに展開します。
```
sudo apt install wget unzip
cd /var/www/html
sudo wget https://www.drupal.org/download-latest/zip
sudo unzip latest.zip
sudo mv drupal-*/* .
sudo mv drupal-*/.htaccess .
sudo rm -rf drupal-* latest.zip
```
ファイルのパーミッションの設定: Drupalがファイルを書き込めるように、適切なパーミッションを設定します。
```
sudo chown -R www-data:www-data /var/www/html/
sudo chmod -R 755 /var/www/html/
```
Webインタフェースの設定: ブラウザでWebインタフェースを介してDrupalのインストールを続けるために、http://localhost またはサーバーのIPアドレスにアクセスします。Drupalのセットアップウィザードが表示されますので、指示に従ってください。

---

Drupal は、PHPで書かれたオープンソースのコンテンツ管理システム（CMS）です。

Drupal を使用することで、ユーザーはウェブサイトを作成、管理、編集することができます。

Drupal は柔軟性が高く、多様な種類のウェブサイトやアプリケーションを構築するために使用されます。

PHP が Drupal のバックエンドで使用されることが一般的であり、Drupal ウェブサイトは PHP スクリプトに基づいて構築されています。

---
