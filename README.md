<p align="center">
<img width="600" alt="banner" src="https://user-images.githubusercontent.com/74450836/235341201-1bbf55b6-e049-46c2-ba16-dfdfe2787d87.png">
</p>
<br/>

----

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
```
make clean
```

### DBも含めてデータを全削除
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
