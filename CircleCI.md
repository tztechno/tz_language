# CircleCI
### 
https://github.com/marketplace/circleci

---

(base) shun_ishii@shunnoMacBook-puro js_fetchEarthquakeData % circleci local execute -c .circleci/config.yml
CircleCI would like to collect CLI usage data for product improvement purposes.

Participation is voluntary, and your choice can be changed at any time through the command `cli telemetry enable` and `cli telemetry disable`.
For more information, please see our privacy policy at https://circleci.com/legal/privacy/.

Enable telemetry? Yes
2024/05/09 21:40:18 
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                                       ┃
┃  circleci local execute                                                                               ┃
┃                                                                                                       ┃
┃                                                                                                       ┃
┃                                                                                                       ┃
┃                                                                                                       ┃
┃  Usage:                                                                                               ┃
┃         circleci local execute <job-name> [flags]                                                     ┃
┃                                                                                                       ┃
┃  Local Flags:                                                                                         ┃
┃                                                                                                       ┃
┃       --branch string                git branch                                                       ┃
┃       --build-agent-version string   The version of the build agent image you want to use. This can b ┃
┃ e                                                                                                     ┃
┃ configured by writing in $HOME/.circleci/build_agent_settings.json: '{"LatestSha256":"<version-of-bui ┃
┃ ld-                                                                                                   ┃
┃ agent>"}'                                                                                             ┃
┃       --checkout-key string          git checkout key (default "~/.ssh/id_rsa")                       ┃
┃   -c, --config string                config file (default ".circleci/config.yml")                     ┃
┃       --docker-socket-path string    path to the host's docker socket (default "/var/run/docker.sock" ┃
┃ )                                                                                                     ┃
┃   -e, --env -e VAR=VAL               set environment variables, e.g. -e VAR=VAL                       ┃
┃   -h, --help                         help for execute                                                 ┃
┃       --index int                    node index of parallelism                                        ┃
┃       --node-total int               total number of parallel nodes (default 1)                       ┃
┃       --org-id string                organization id, used when a config depends on private orbs      ┃
┃ belonging to that org                                                                                 ┃
┃   -o, --org-slug string              organization slug (for example: github/example-org), used when a ┃
┃ config depends on private orbs belonging to that org                                                  ┃
┃       --repo-url string              git URL                                                          ┃
┃       --revision string              git revision                                                     ┃
┃       --skip-checkout                use local path as-is (default true)                              ┃
┃       --temp-dir string              path to local directory to store temporary config files          ┃
┃   -v, --volume stringArray           volume bind-mounting                                             ┃
┃                                                                                                       ┃
┃  Global Flags:                                                                                        ┃
┃                                                                                                       ┃
┃       --host string         URL to your CircleCI host, also CIRCLECI_CLI_HOST (default                ┃
┃ "https://circleci.com")                                                                               ┃
┃       --skip-update-check   Skip the check for updates check run before every command.                ┃
┃       --token string        your token for using CircleCI, also CIRCLECI_CLI_TOKEN                    ┃
┃                                                                                                       ┃
┃                                                                                                       ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛


---

### CircleCI について
世界最高のソフトウェア チームは、CircleCI を使用して自信を持って高品質のコードを提供します。

### すぐに始めましょう
CircleCI の無料プランでは、既存のどの無料プランよりも多くのビルド時間が提供されます。最大 6,000 ビルド分/月、一度に 30 ジョブ。

### CI/CD プロバイダーの中で最もカスタマイズ可能な環境
ジョブごとにオペレーティング システム、CPU、GPU、メモリ、イメージをカスタマイズするための幅広い選択肢。 Docker、Windows、Linux、Arm、macOS 用にビルドすることも、ランナーを使用して独自のコンピューティング上にビルドすることもできます。

### 市場で最速のビルド時間
CircleCI でのビルド時間は、競合他社よりも平均 70% 高速です。

### 最高レベルのコンプライアンスと認証
CircleCI は、FedRAMP 認定を受け、SOC 2 Type II に準拠している唯一の CI/CD プラットフォームです。監査ログ、制限されたコンテキスト、LDAP などの組み込み機能により、コードを完全に制御できます。

### ソフトウェア開発プロセス全体の可視性の向上
CircleCI の Insights ダッシュボードでは、ワークフローのステータス、期間、クレジット消費、コストを無料で確認できます。

### SSHデバッグ
任意のジョブに CircleCI に安全にアクセスして、ビルドとテストをリアルタイムでデバッグします。

### 自動テスト分割
同じジョブの並列インスタンス間でテストを自動的に分割することで、フィードバック ループを短縮します。

### GitHub チェックをサポートするようになりました
CircleCI ワークフローと関連ジョブのステータスをすべて GitHub UI 内で確認できます。新規および既存のアカウントの CircleCI 組織設定でこの機能を有効にします。

---


CircleCIの無料プランは、多くの一般的なCI/CDタスクをカバーする十分な機能を提供していますが、いくつかの制限があります。一般的な制限は以下の通りです：

### 並行実行数の制限: 
同時に実行できるジョブ（またはビルド）の数に制限があります。無料プランでは、通常、1つのビルドにつき1つのジョブのみが実行されます。これにより、並行して実行されるビルドやジョブの数が制限されます。
### ビルド時間の制限: 
個々のビルドに対する最大実行時間があります。無料プランでは、通常、ビルドの最大実行時間が1時間に制限されています。これを超えるとビルドがタイムアウトします。
### ビルドの保存期間の制限: 
完了したビルドの履歴やアーティファクトの保存期間に制限があります。無料プランでは、通常、最後の30日間のビルドデータのみが保持されます。それ以降のデータは削除される場合があります。
### 追加機能の制限: 
一部の高度な機能やプラグインは、有料プランのサブスクリプションが必要な場合があります。たとえば、高度なキャッシュ管理、ワークフローの設定、追加のストレージオプションなどが含まれます。

これらの制限は、一般的な小規模または中規模のプロジェクトには適していますが、より大規模で複雑なプロジェクトや高度なニーズを持つプロジェクトには、有料プランが必要になる場合があります。

---

CircleCIをプロジェクトに導入する方法は、基本的に次のステップになります：

### CircleCIにサインアップする: 
まず、CircleCIのウェブサイトにアクセスして、GitHubやBitbucketなどのアカウントを使用してサインアップします。必要に応じて、無料プランまたは有料プランを選択します。
### リポジトリを選択する: 
サインアップ後、CircleCIのダッシュボードにアクセスして、導入したいプロジェクトのリポジトリを選択します。CircleCIはGitHub、Bitbucket、GitLabなどの主要なバージョン管理プラットフォームと統合しています。
### 設定ファイルを追加する: 
選択したリポジトリに、CircleCIの設定ファイル（通常は .circleci/config.yml）を追加します。この設定ファイルには、ビルド、テスト、デプロイなどのジョブの定義が含まれます。CircleCIのウェブサイトやドキュメントから、設定ファイルの作成方法や書き方を学ぶことができます。
### ビルドをトリガーする: 
設定ファイルがリポジトリに追加されると、CircleCIは自動的にビルドをトリガーし、ジョブを実行します。ビルドのステータスや結果は、CircleCIのウェブインターフェースや通知（Slackなど）を通じて確認できます。
### 必要に応じてカスタマイズする: 
プロジェクトのニーズに合わせて、ビルドやデプロイのフローをカスタマイズすることができます。CircleCIの設定ファイルやドキュメントを参照して、追加のステップやアクションを定義することができます。

これらのステップに従うことで、CircleCIをプロジェクトに導入し、自動化されたCI/CDパイプラインを構築することができます。

---

はい、CircleCIを使用して定期的にデータを取得し、リポジトリに保存するような作業も可能です。これは、定期的なジョブをスケジュールし、データの取得や処理を行うことで実現できます。

具体的には、次の手順で作業を実行できます：

CircleCIの設定ファイル（通常は.circleci/config.yml）に、定期的なスケジュールで実行されるジョブを定義します。これには、スケジュールされたジョブのトリガー、実行するステップやコマンド、取得したデータをリポジトリに保存する手順が含まれます。

スケジュールされたジョブ内で、データの取得や処理を行います。たとえば、APIからデータを取得して処理するPythonスクリプトを実行したり、データをダウンロードして加工するシェルスクリプトを実行したりすることができます。

処理されたデータをリポジトリに保存します。これには、ファイルの追加やコミット、プッシュなどのGit操作が含まれます。CircleCIのジョブは、リポジトリにアクセスしてこれらの操作を実行できます。

リポジトリに保存されたデータは、必要に応じて他のプロセスやアプリケーションからアクセスできるようになります。これにより、定期的なデータの更新やバックアップが実現できます。

このようにして、CircleCIを使用して定期的なデータの取得とリポジトリへの保存を自動化することができます。

---


CircleCIは、アプリケーションをデプロイするためのCI/CDツールであり、アプリケーションをデプロイする場所として、以下のようなオプションを提供しています：

### クラウドプロバイダー: 
CircleCIは、AWS、Google Cloud Platform、Microsoft Azureなどのクラウドプロバイダーにアプリケーションをデプロイすることができます。

これらのプロバイダーには、EC2インスタンス、Lambda関数、App Engine、Cloud Functionsなど、さまざまなデプロイメントオプションがあります。
### PaaSサービス: 
CircleCIは、Heroku、Netlify、VercelなどのPaaSサービスにアプリケーションをデプロイすることもサポートしています。

これらのサービスは、アプリケーションのデプロイメントを簡略化し、管理を容易にするためのプラットフォームを提供しています。
### Dockerコンテナ: 
CircleCIはDockerコンテナをサポートしており、Dockerイメージをビルドしてコンテナレジストリにプッシュし、任意のデプロイ先でコンテナを実行することができます。

これにより、デプロイメントプロセスが標準化され、環境の依存関係の問題が回避されます。
### カスタムスクリプト: 
CircleCIは、任意のカスタムスクリプトやコマンドを実行することも可能です。これにより、特定のデプロイ先に固有のデプロイメントプロセスを実行することができます。

CircleCIは、これらのオプションを組み合わせて、開発者や組織のニーズに合った柔軟なデプロイメントプロセスを設定することができます。


---

CircleCIは、継続的インテグレーション（CI）および継続的デリバリー（CD）のためのクラウドベースのプラットフォームです。開発者は、GitHubやBitbucketなどのリポジトリと統合して、アプリケーションのビルド、テスト、デプロイを自動化することができます。

CircleCIの主な特徴は以下の通りです：

### 柔軟性と拡張性: 
CircleCIはさまざまなプログラミング言語やフレームワークに対応しています。また、Dockerコンテナを使用して環境をカスタマイズすることができるため、ほとんどの開発環境に対応しています。
### 高速なビルド: 
CircleCIは並列ビルドをサポートしており、複数のジョブを同時に実行することでビルド時間を短縮することができます。また、キャッシュ機能を使用して依存関係をキャッシュし、ビルドの高速化を図ることもできます。
### ワークフローの柔軟性: 
CircleCIでは、ワークフローを柔軟に定義することができます。複数のジョブやステップを含む複雑なワークフローを設定し、依存関係を定義することができます。
### 統合と通知: 
CircleCIは、GitHubやSlackなどのツールとの統合をサポートしています。ビルドの状態や結果をリアルタイムで通知し、開発チームとのコミュニケーションを円滑にします。
### セキュリティと信頼性: 
CircleCIはセキュリティを重視しており、ビルド環境のセキュリティを確保するための機能を提供しています。また、99.9%のアップタイムを保証しており、信頼性の高いサービスを提供しています。

CircleCIは、開発者がアプリケーションの品質を維持し、迅速かつ効率的に開発プロセスを進めるための強力なツールとして利用されています。

---

