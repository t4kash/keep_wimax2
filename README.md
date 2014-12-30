# NAD11の接続をWiMAX2+に強制的に切り替えるスクリプト

## Synopsis
NAD11がWiMAXになっていたら、一度ノーリミットノードに切り替えてからハイスピードモードに戻してWiMAX2+に接続させるようにするスクリプトです。
LAN内に常時起動しているpythonが動作する環境(LinuxやMac等)が必要です。


## Installation
pythonが必要です。  
pip等でMechanizeをインストールしてください。  
```
pip install mechanize
cd [working_directory]
git clone https://github.com/t4kash/keep_wimax2.git
```

keep_wimax2.pyファイル内のパスワードを変更してください。

定期的に実行するためにcronにスクリプトを設定します。  
例(毎時00分と30分に実行)
```
crontab -e

下記を追加して保存
0,30 * * * * [working_directory]/keep_wimax2/keep_wimax2.py >> [working_directory]/keep_wimax2/cron.log 2>&1
```

## License
MIT License
