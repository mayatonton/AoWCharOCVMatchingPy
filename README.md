# AoWCharOCVMatchingPy
2022.02.05
こぶさんにもらったファイルを追加 [1080x2340]

<img src="https://raw.githubusercontent.com/mayatonton/AoWFomationJPG2Text/main/source_img/C.jpg" width=30% height=30% />



iPhoneSE のみ対応、陣形画像の結合には Tailor を利用（https://apps.apple.com/jp/app/tailor-screenshot-stitching/id926653095）


陣形画像から兵士を画像検索する

目的のアウトプット
```
習 習 習 岩 習 習 習
ゴ 剣 船 獣 船 剣 ゴ
投 投 船 獣 船 投 投
バ 投 獣 バ 獣 投 バ
ア ア 投 魔 投 ア ア
弓 弓 骨 骨 弓 弓 弓
ゾ パ 船 岩 船 パ ゾ
```


インプットの陣形画像から兵士を検索し位置を特定する
未来的には位置から７×７の文字列碁盤目データに変換する目的

以下の例の画像は、「巨大岩」と「見習い魔法使い」の検出結果を矩形で表現したもの

~~左側の画像の抽出結果は正しいが、右側は「見習い魔法使い」の検出に誤りがあり~~
~~「アサシン」や「ゾンビ兵」が誤って「見習い魔法使い」として検出されている~~
(対応済み 2022.02.02)

<img src="https://raw.githubusercontent.com/mayatonton/AoWCharOCVMatchingPy/main/out_a.jpg" width=30% height=30% /><img src="https://raw.githubusercontent.com/mayatonton/AoWCharOCVMatchingPy/main/out_b.jpg" width=30% height=30% />
