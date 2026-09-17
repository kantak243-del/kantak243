#!/usr/bin/env python3
"""
楽天ROOM投稿文ジェネレーター

商品名・ジャンル・特徴などを入力すると、Claude APIを使って
楽天ROOM向けの紹介文・キャッチコピー・ハッシュタグを自動生成します。

事前準備:
    pip install anthropic
    export ANTHROPIC_API_KEY="sk-ant-..."

使い方:
    python rakuten_room_generator.py
    (対話形式で商品情報を入力すると投稿文を生成します)

    または引数で直接指定:
    python rakuten_room_generator.py --name "商品名" --genre "ジャンル" --features "特徴・おすすめポイント"
"""

import argparse
import os
import sys

from anthropic import Anthropic

MODEL = "claude-sonnet-5"

SYSTEM_PROMPT = """あなたは楽天ROOMで商品を紹介する投稿文を書くアシスタントです。
以下のルールで日本語の投稿文を作成してください。

- 親しみやすく自然な口調で、読者におすすめする文章にする
- 冒頭で商品の魅力を簡潔に伝える
- 実際に使った/読んだ体験談風の一言を自然に含める（誇張・虚偽にならない範囲で）
- 「※価格・在庫などは商品ページでご確認ください。」という注意書きを文末に入れる
- 最後に関連するハッシュタグを7〜10個程度、日本語で提案する（#を付ける）
- 誇大表現や断定的な効果効能の主張はしない
- 出力は投稿文本文とハッシュタグのみ。前置きや説明文は不要
"""


def generate_post(name: str, genre: str, features: str) -> str:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("エラー: 環境変数 ANTHROPIC_API_KEY が設定されていません。", file=sys.stderr)
        sys.exit(1)

    client = Anthropic(api_key=api_key)

    user_message = (
        f"商品名: {name}\n"
        f"ジャンル: {genre}\n"
        f"特徴・おすすめポイント: {features}\n\n"
        "上記の商品について、楽天ROOM投稿文を作成してください。"
    )

    response = client.messages.create(
        model=MODEL,
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )

    return "".join(block.text for block in response.content if block.type == "text")


def main():
    parser = argparse.ArgumentParser(description="楽天ROOM投稿文ジェネレーター")
    parser.add_argument("--name", help="商品名")
    parser.add_argument("--genre", help="ジャンル・カテゴリ")
    parser.add_argument("--features", help="特徴・おすすめポイント")
    args = parser.parse_args()

    name = args.name or input("商品名を入力してください: ").strip()
    genre = args.genre or input("ジャンル・カテゴリを入力してください: ").strip()
    features = args.features or input("特徴・おすすめポイントを入力してください: ").strip()

    if not name:
        print("商品名は必須です。", file=sys.stderr)
        sys.exit(1)

    print("\n投稿文を生成中...\n")
    post = generate_post(name, genre, features)
    print("=" * 40)
    print(post)
    print("=" * 40)


if __name__ == "__main__":
    main()
