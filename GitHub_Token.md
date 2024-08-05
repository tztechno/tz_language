

GitHubのPersonal Access Token (PAT) を取得する手順は以下の通りです。

1. **GitHubにログイン**:
   GitHubのアカウントにログインします。

2. **Settingsに移動**:
   右上のプロフィールアイコンをクリックし、ドロップダウンメニューから "Settings" を選択します。

3. **Developer settings**:
   左側のメニューから "Developer settings" を選択します。

4. **Personal access tokens**:
   左側のメニューから "Personal access tokens" を選択し、次に "Tokens (classic)" を選択します。

5. **Generate new token**:
   "Generate new token" ボタンをクリックします。

6. **Tokenの詳細を入力**:
   - **Note**: Tokenの名前を入力します（例：MyToken）。
   - **Expiration**: Tokenの有効期限を設定します。必要に応じて適切な期限を選択してください。
   - **Scopes**: Tokenに付与する権限を選択します。リポジトリにアクセスするためには、`repo` スコープが必要です。他のスコープは必要に応じて選択します。

7. **Generate token**:
   下部にある "Generate token" ボタンをクリックします。

8. **Tokenを保存**:
   生成されたTokenが表示されるので、これをコピーして安全な場所に保存します。ページを再読み込みするとこのTokenは表示されなくなるため、必ずコピーして保存しておいてください。

取得したTokenを使って、GitHub APIやCLIツール、その他のGitHub関連のツールで認証を行うことができます。Tokenは非常に重要な情報なので、他人と共有しないようにし、必要に応じて期限を設定することでセキュリティを確保してください。
