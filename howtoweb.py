import streamlit as st
import numpy as np
import pandas as pd

###webアプリの公開

##タイトル・テキストの追加
#タイトルの追加
st.title("webアプリの公開")
#テキストを追加する
st.write("webアプリの公開")

##文字列の書き方
#マジックコマンド
#コードの表示はバックコーテーション
"""
# webアプリの公開手順

## githubを開く
### リポジトリを作成
Create a new repositoryから作成
Repository nameを入力
Public or Privateの選択
Create repositoryを選択
HTTPSのURLをコピーする
## ターミナルを開く
### gitの初期化
```python
git init
```
### ローカルとリポジトリを紐づける
```python
git remote add origin urlをペースト
```
#### remote origin already existが表示される場合
```python
git remote rm origin
```
### requirements.tetの用意
requirements.tetに、アプリケーションで使用される外部ライブラリを記載する
#### ライブラリのバージョンを確認
streamlitのバージョンを確認する場合、以下のように実行する
```python
pip freeze
pip freeze| grep strea
```
返ってきたバージョンをrequirements.tetに入力する
streamlitの場合、以下のように入力する
```python
streamlit==バージョン名
```
### gitに追加する
```python
git add .
git commit -m'1stcommit
git push origin master
```
これでgitにプッシュされる
以上でリポジトリの作成が完了

## Streamlit sharingを開く
### リポジトリの追加
New appを選択
リポジトリからgitで作成したリポジトリを選択
Branchにmasterからmainを入力
Main file pathにメインとなるファイル名を入力
Deployを選択
以上でwebアプリの公開が完了
"""