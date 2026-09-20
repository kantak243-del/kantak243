# kantak243

## X バズ投稿エンジン

Xのバズ投稿を収集→分析→型化→投稿量産→リスト獲得→教育→セールスまでのファネルを
Claude Codeのスキルとして運用するためのリポジトリ。

- スキル本体: [`.claude/skills/x-buzz-engine/SKILL.md`](.claude/skills/x-buzz-engine/SKILL.md)
- 収集データ: [`data/buzz-posts/collected-posts.csv`](data/buzz-posts/collected-posts.csv)
- 分析結果: [`data/buzz-posts/pattern-analysis.md`](data/buzz-posts/pattern-analysis.md)

使い方: `collection-guide.md` の手順でバズ投稿を集めてCSVに貼り付けた後、
Claude Codeに「バズ投稿を分析して」と依頼すると、型の抽出から投稿案の量産、
リスト獲得〜セールスレター作成までをスキルが支援する。
