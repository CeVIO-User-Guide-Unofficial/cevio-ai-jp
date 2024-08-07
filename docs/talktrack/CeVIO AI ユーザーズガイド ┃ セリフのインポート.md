


セリフのインポート
=========


  


 あらかじめセリフを記述したテキストファイルを作成しておいて、インポートすることができます。
   

 インポートするトークトラックを選択してから、メニューの「ファイル」→「インポート」→「セリフのテキスト読み込み」を選んで、ファイルを指定してください。
   



 ファイル形式について
 

 表計算ソフトで作成できるCSV形式のほか、セリフだけ記述したテキストファイル、1行ずつ「キャスト名,セリフ」や「キャスト名,セリフ,プリセット」を記述したテキストファイルも読み込めます。
   

  

**・区切り文字には、タブ／半角カンマ（,）が使用できます（混在可）。** 
  

  

**・キャスト名には「さとうささら」などキャスト設定可能な名前を記述します。** 
  

  

**・1列目(1つ目の区切り文字の前)の内容がキャスト名に一致するとキャスト設定、それ以外はセリフとして読み込まれます。** 
  

  

**・3列目(2つ目の区切り文字の後ろ)の内容がプリセット名に一致するとプリセット設定、それ以外はカンマを含むセリフとして読み込まれます。** 
  

  

**・1文200文字を超えると自動的に分割され、最大1000行まで読み込み可能です。** 
  

  

**・ファイルの拡張子は「.txt」または「.csv」で保存してください。** 
  

  

  

![](../../image/035_w.png)
  







 キャスト名について
 

 キャスト指定には以下の表記が使用可能です。
   

  

 さとうささら　　　　小春六花　　　　　　弦巻マキ (日)
   

 IA　　　　　　　　　夏色花梨　　　　　　弦巻マキ (英)
   

 OИE　　　　　　　　フィーちゃん　　　　ロサ (ROSA)
   

  

 ※「ONE」も「OИE」として使用可能。
   







 文字コードについて
 

 メモ帳やGoogleスプレッドシートでは「UTF\-8」でファイルが保存され、エクセルのCSVファイルは「Shift\-JIS」で「CSV UTF\-8」も選べます。必要に応じて、
 [オプション](../../option/) 
 の「トーク設定」の「テキストファイルの文字コード」の「読み込み」で文字コードを指定してください。
 





 コンディションと感情
 

 インポートファイルにプリセット指定がない場合、インポートされたセリフには、選択行の感情や大きさ、速さなどのパラメーターが適用されます。あらかじめ好みの設定にしてからインポートすると簡単です。
   

 インポート後でも、\[Alt]キーを押しながらプリセットを選択すると、そのトラックのキャストに一括設定できます。
 







