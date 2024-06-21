###
# pip
###

---
---

pipとcondaはPythonのパッケージ管理システムであり、それぞれ異なる用途で使用されます。以下に、それぞれの基本的な使い方と、簡単な説明を示します。

### pip (Pythonのパッケージ管理システム)

**pip**はPythonの標準的なパッケージ管理システムで、Pythonパッケージのインストール、アップグレード、アンインストールを行います。以下は基本的なコマンドです：

- **インストール**: Pythonがインストールされている場合、通常はpipもインストールされています。
- **パッケージのインストール**: `pip install <package_name>`
  ```bash
  pip install requests  # requestsパッケージのインストール例
  ```
- **パッケージのアップグレード**: `pip install --upgrade <package_name>`
  ```bash
  pip install --upgrade requests  # requestsパッケージのアップグレード例
  ```
- **パッケージのアンインストール**: `pip uninstall <package_name>`
  ```bash
  pip uninstall requests  # requestsパッケージのアンインストール例
  ```
- **インストールされているパッケージの一覧表示**: `pip list`
  ```bash
  pip list  # インストールされているパッケージの一覧表示
  ```

### conda (Pythonパッケージおよび環境管理システム)

**conda**は、Pythonパッケージの管理とともに、仮想環境の作成・管理も行えるパッケージ管理システムです。AnacondaやMinicondaを通じて提供されています。

- **インストール**: AnacondaまたはMinicondaをインストールすることで、condaが利用できます。
- **パッケージのインストール**: `conda install <package_name>`
  ```bash
  conda install numpy  # numpyパッケージのインストール例
  ```
- **パッケージのアップグレード**: `conda update <package_name>`
  ```bash
  conda update numpy  # numpyパッケージのアップグレード例
  ```
- **パッケージのアンインストール**: `conda remove <package_name>`
  ```bash
  conda remove numpy  # numpyパッケージのアンインストール例
  ```
- **仮想環境の作成**: `conda create --name <env_name> python=<version>`
  ```bash
  conda create --name myenv python=3.8  # Python 3.8を使った仮想環境の作成例
  ```
- **仮想環境のアクティベート**: `conda activate <env_name>`
  ```bash
  conda activate myenv  # "myenv"という名前の仮想環境をアクティベートする例
  ```
- **仮想環境のディアクティベート**: `conda deactivate`
  ```bash
  conda deactivate  # 現在の仮想環境をディアクティベートする例
  ```
- **仮想環境の一覧表示**: `conda env list`
  ```bash
  conda env list  # 作成されているすべての仮想環境の一覧表示
  ```

これらのコマンドを使って、pipやcondaを通じてPythonのパッケージを管理し、環境を効果的に構築・管理できます。特にcondaを使うことで、パッケージの依存関係や異なるバージョンのPythonの共存が容易になります。

---
