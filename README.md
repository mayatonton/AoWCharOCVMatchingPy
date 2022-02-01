# AoWCharOCVMatchingPy
陣形画像から兵士を画像検索する

インプットの陣形画像から兵士を検索し位置を特定する
未来的には位置から７×７の文字列碁盤目データに変換する目的

以下の例の画像は、「巨大岩」と「見習い魔法使い」の検出結果を矩形で表現したもの

左側の画像の抽出結果は正しいが、右側は「見習い魔法使い」の検出に誤りがあり
「アサシン」や「ゾンビ兵」が誤って「見習い魔法使い」として検出されている

<img src="https://raw.githubusercontent.com/mayatonton/AoWCharOCVMatchingPy/main/out_a.jpg" width=30% height=30% /><img src="https://raw.githubusercontent.com/mayatonton/AoWCharOCVMatchingPy/main/out_b.jpg" width=30% height=30% />
