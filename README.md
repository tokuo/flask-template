## What's this?
Flaskの雛形

## configuration-file
### python-version
`runtime.txt`にて記述 <br>
python３系のみを想定しています。

### Necessary packages
`requirements.txt`にて記述 <br>
pipenvによってPipfileが生成されます。

### app-configuration-file
`config.py` にて記述 <br>
ご自由に変更してください。

## Setup environment-variable
```
$ export PYTHONPATH=`pwd`
flask app コマンドを利用する場合は以下環境変数も設定してください。
$ export FLASK_APP=index.py
```

## Start this app
複数通りの実行方法があります。

### (1-way) Start this app locally on virtual environment
#### Install package-manager
```
$ pip install -U pipenv
```
(注) pipがpython２系のものの場合、期待通りに動作しない可能性があります。

#### Create virtual-envirnment(pipenv)
```
$ pipenv install
```

#### Start this app by pipenv
```
$ pipenv run python index.py
環境変数 FLASK_APP を設定している場合は以下のコマンドでも大丈夫です。
$ pipenv run flask run
```

#### Remove virtual-envirnment(pipenv)
```
$ pipenv --rm
$ # rm ./Pipfile*
```

### (2-way) Start this app normally
#### Install the packages
```
ローカルインストール
$ pip install -U -r requirements.txt -t ./

グローバルインストール
$ pip install -U -r requirements.txt

```

#### Start this app
```
$ python index.py
```

#### Remove the packages
```
ローカルインストールしていた場合
$ rm -rf ./<インストール時に生成されたディレクトリ群>

グローバルインストールしていた場合
$ pip uninstall -r requirements.txt
```

## Test all unit-tests by pipenv
TODO test_runner.sh は改良の余地あり <br>
TODO pipenvでの環境が整っているかどうかを判断する機能をスクリプト内に入れる。<br>
TODO 現状下記コマンドではpipenv環境でのみの実行だが、test_runnerを書き換えればpipenvを利用せずにテストを実行できます。
```
$ ./test_runner.sh
```

## Development Note
### Test
標準のテストパッケージunittestだけではうまくパスの取り扱いできないので、pytestを採用 <br>
コードでは標準パッケージunittestを極力利用。あくまでpytestはコマンド実行時でのみ利用 <br>
pytestを採用した理由として、pycharmでサポートされていることと、パスの扱いに問題がなかったので採用 <br>
単体テストを作成する際、命名はファイル名、メソッド名共に「test_」をつけないと実行されない(class名は除く)ので、絶対に付与してください。

### Templates
htmlファイル等を配置するtemplateフォルダは「templates」でなければならない <br>
（「template」では認識されない）

### Others
ネットワークセグメントにてPyPIに接続できない場合があるので、いくつか対応策を記述<br>
・あらかじめパッケージをダウンロードし、それごと本番環境にデプロイし、ローカルインストール <br>　
　（パッケージをgithubにpushするのはよろしくないので、ci/cdツール上でダウンロードすることを推奨）
```
ダウンロード
$ pip download -d vendor -r requirements.txt

ローカルインストール
$ pip install vendor/<インストールしたいパッケージ名>-<パッケージバージョン>-*.whl

削除
$ pip uninstall <インストールしたパッケージ名>
$ rm -rf vendor
```
・必要なパッケージが既にインストールされているdockerイメージを用意 <br>
・pip installできるように、PyPIと接続ができるプロキシサーバを用意
