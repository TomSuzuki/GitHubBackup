![LICENSE:undecided](https://img.shields.io/badge/LICENSE-undecided-FD3164.svg?longCache=true)

# GitHubBackup
GitHubのpublicのリポジトリを毎日指定時間にバックアップする。
> 使う場合は`cron`とかで。

## 初期設定
1. `data`フォルダを作成。
1. `data/updated.json`を作成し、中に`{}`を入れる。
1. `setting.json`を作成し以下のように設定する。
```json
{
  "username": "[GitHubのアカウント名]",
  "backup_folder": "[バックアップを取る場所]"
}
```

## 既知の問題
- 取得するリポジトリ数の最大が100個。→これを超えると一部が対象外となる。
