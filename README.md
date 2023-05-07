<p align="center">
<a href="https://shields.io/"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Sgi114/plant_akinator"></a>
<a href="https://shields.io/"><img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr-raw/Sgi114/plant_akinator"></a>
<a href="https://shields.io/"><img alt="GitHub closed pull requests" src="https://img.shields.io/github/issues-pr-closed-raw/Sgi114/plant_akinator"></a>
<a href="https://shields.io/"><img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/Sgi114/plant_akinator"></a>
<br/><br/>
<a href="https://skillicons.dev"><img alt="My Skills" src="https://skillicons.dev/icons?i=js,ts,html,css,react,materialui,python,mysql,docker"></a>
</p>

<br/>

---

<br/>

## セットアップ

```
make setup
```

## 使用方法

### 起動

```
make start
```

### 停止

```
make stop
```

### 削除

このコマンド実行後に `make start` で再起動すると 約 2.8MB 通信

```
make clean
```

### DB も含めてデータを全削除

このコマンド実行後に `make start` で再起動すると 約 395MB 通信

```
make all-reset
```

### デバッグ

参考サイト：https://zenn.dev/sinozu/articles/8c51091af73cd1b386b8

```
make debug CONTAINER_ID=[デバッグしたいコンテナのID]
```

## URL

### メイン画面

http://localhost/

### phpMyAdmin

http://localhost:8001/

### バックエンド

http://localhost:8000/

<!-- ## 使用方法
```
python backend\main.py
cd frontend
npm start
``` -->

## メモ

#### フロントエンド環境構築

```
npx create-react-app plant-akinator --template=typescript
```
