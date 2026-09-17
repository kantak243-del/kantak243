# kantak243

## 楽天ROOM投稿文ジェネレーター (rakuten_room_generator.py)

商品名・ジャンル・特徴を入力すると、Claude APIを使って楽天ROOM向けの
紹介文・キャッチコピー・ハッシュタグを自動生成するツールです。

### 準備

```bash
pip install -r requirements.txt
export ANTHROPIC_API_KEY="sk-ant-..."
```

Anthropic APIキーは https://console.anthropic.com/ で取得できます。

### 使い方

対話形式:

```bash
python rakuten_room_generator.py
```

引数指定:

```bash
python rakuten_room_generator.py --name "商品名" --genre "ジャンル" --features "特徴・おすすめポイント"
```
