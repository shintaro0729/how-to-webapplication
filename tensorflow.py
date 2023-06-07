import streamlit as st
import numpy as np
import pandas as pd

###tensorflowのインストール

##タイトル・テキストの追加
#タイトルの追加
st.title("Tensorflowのインストール")
#テキストを追加する
st.write("Tensorflowのインストール")

##文字列の書き方
#マジックコマンド
#コードの表示はバックコーテーション
"""
# ターミナルを開く
## まずはPython仮想環境を作る
今回はtf2という名前のPython仮想環境を作成
```python
conda create -n tf2
```
condaコマンドの更新を聞かれた場合
```python
conda apudate -n base -c defaults conda
```
## Python仮想環境を有効にする
今回はtf2という名前のPython仮想環境を有効にする
```python
conda activate tf2
```
ターミナルで行の先頭が「base」から「tf2」に変更されていればOK
Anacondaでは仮想環境ごとにインストールするパッケージのバージョン等を切り替えできる
## Tensorflowのインストール
```python
conda install tensorflow
```
今回は最新版をインストールしたが、下記のコードを実行すればバージョン指定ができる
```python
conda install tensorflow==2.4
```
## Tensorflowのインポート
Pythonの仮想環境でPythonの実行環境を起動する
```python
python
```
ターミナルに「>>>」が表示されれば、Pythonの実行環境が起動できた
```python
import tensorflow
```
ターミナルに「>>>」が表示されれば、Tensorflowがインストールできた
## Pythonの実行環境を抜ける
```python
exit()
```
"""
