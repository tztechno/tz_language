###
# Drupal
###

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
