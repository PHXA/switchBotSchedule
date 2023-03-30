# 概要

定期的に決められた時間にSwitchBotの指を作動させるプログラム

# 使い方

clone後、env.exampleを.envとしてコピーし、TOKENとDEVICE_IDを任意のものに変更する。

TOKENは[こちら](https://blog.switchbot.jp/announcement/api-v1-1/)を参考に取得する。

実行したい時間はmain.pyの中の55行目のリストを変更する。

以下のコマンドを実行する。

```Python:main.py
python main.py
```