# Plant Akinator

## セットアップ
```
pip install -r backend\requirements.txt
cd frontend
npm i --force
```

## 使用方法
### 起動
```
docker-compose up -d
```

### 停止
```
docker-compose stop
```

### 削除
```
docker-compose down --rmi all --volumes --remove-orphans
```

### デバッグ
参考サイト：https://zenn.dev/sinozu/articles/8c51091af73cd1b386b8
```
docker commit [コンテナID] backend_test
docker run --rm -it backend_test bash
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
