# File-Manipulator

### 概要
Linux file systemに格納されているデータにアクセスして操作するプログラムです。
CLIからファイルを実行するときに、引数として、全４種類のコマンドを設定することができます。

### 使用技術
<img src="https://qiita-user-contents.imgix.net/https%3A%2F%2Fimg.shields.io%2Fbadge%2F-Python-F2C63C.svg%3Flogo%3Dpython%26style%3Dfor-the-badge?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&w=1400&fit=max&s=5d7d909c2f70c6c8a0fc0477bd1a56ae">

### コマンド一覧
CLIにてファイルを実行するとき、
```
python <fileName.py>
```
に加え、以下の引数を設定して実行することで、各コマンドを使用することができます。

1. reverse
```
reverse inputpath outputpath
```
inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成

2. copy
```
copy inputpath outputpath
```
inputpath にあるファイルのコピーを作成し、outputpath として保存

3. duplicate-contents
```
duplicate-contents inputpath n
```
inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製

4. replace-string
```
inputpath replacedString newString
```
inputpath にあるファイルの内容から文字列 replacedString を検索し、replacedString の全てを newString に置き換える