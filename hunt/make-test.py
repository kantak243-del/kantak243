#!/usr/bin/env python3
"""index.html からテスト版 test.html を生成する。

テスト版の違い:
  - 主人公の体力が減らない（のけぞり・ふっとびは起きる）
  - セーブは本番と別の保存場所（アカウント保存も使わない）
  - 画面下に「テスト版」の表示

ゲーム本体を直したら、このスクリプトを実行して test.html を作り直す:
  python3 hunt/make-test.py
"""
from pathlib import Path

here = Path(__file__).parent
src = (here / "index.html").read_text(encoding="utf-8")

swaps = [
    ("const TEST_MODE = false;", "const TEST_MODE = true;"),
    ("<title>焔尾竜討伐</title>", "<title>焔尾竜討伐テスト版</title>"),
]
for old, new in swaps:
    if src.count(old) != 1:
        raise SystemExit(f"index.html に「{old}」がちょうど1つ見つかりません")
    src = src.replace(old, new)

header = "<!-- 自動生成ファイル: 直接編集せず hunt/make-test.py で index.html から作り直す -->\n"
(here / "test.html").write_text(header + src, encoding="utf-8")
print("test.html を生成しました")
