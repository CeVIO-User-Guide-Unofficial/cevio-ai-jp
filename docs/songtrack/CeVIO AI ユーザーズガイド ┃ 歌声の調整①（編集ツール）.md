


歌声の調整①（編集ツール）
=============


  


 ツールバーの編集ツールや、ピアノロールの右クリックのメニューからは、編集モードの切り替えができます。
   

 [Ctrl]キーを押すと、一時的に編集ツールを変化させることができます。
   

  


![](../../image/ope_05_w.png)

選択ツール
-----


 ドラッグ（マウスの左ボタンを押したまま移動）してコピーや削除の範囲を指定します。
   

 調整画面で範囲指定後、ショートカットキー[Ctrl+C]で範囲内の調整値をコピーします。コピーした内容は、[Ctrl+V]でポジションカーソルの位置に貼り付けられます。
   

 範囲指定後、[Delete]キーで調整値を削除して調整前に戻すことができます。
   

  


![](../../image/st05_17.png.1378885672274.png)

  

**クオンタイズ基準／タイミング基準の範囲指定**
  

 通常はクオンタイズ基準の範囲指定で、タイミング調整画面で選択ツールのときはタイミング基準の範囲指定になります。
   

 [Shift]キーを押しながらドラッグすると、クオンタイズ基準とタイミング基準を切り替えられます。
   

 下段のタイミング表示エリアのクリックやドラッグでも、音符単位／音素単位で範囲選択可能です。タイミング基準で調整をリセットしたり、ボリューム調整画面で休符区間を選択してブレスの音量を下げるときなどに役立ちます。
   

  


![](../../image/V8.6_timing_selection.png)

  

**調整値の上下移動**
  

 タイミング以外の調整画面では、範囲指定後に値を上下にドラッグすると、範囲内の値をそのまま上下に移動することができます。ある範囲のビブラートを全体的に強めたり、弱めたりしたいときなどに便利です。
   

 [Alt]キーを押しながらドラッグすると、クオンタイズ／タイミング補正せずフリー範囲指定できます。
   

  

**ミックスコピー**
  

 調整画面で範囲指定後、右クリックメニューの「ミックスコピー」やショートカットキー[Ctrl+Shift+C]で、既定値の部分も含めてパラメータをコピーすることができます。
   

  

**タイミングのコピーと貼り付け**
  

 タイミングをコピーすると状態ラインが何本目かも記憶されます。たとえば、3本目のラインをコピーして貼り付けたときは、ポジションカーソル以降の3本目に反映されます。
   

 タイミング調整値は元の値に対する相対値のため、貼り付けで崩れやすいですが、ミックスコピーを使うと崩れづらいです。
   

まとめ選択ツール
--------


 ドラッグして範囲を指定してコピーすると、範囲内の音符と調整値、テンポや強弱記号をまとめてコピーできます。その後、ポジションカーソルで位置を指定して貼り付けることで、元の音符や調整値を簡単に再現できます。
   

  


![](../../image/st05_matome.png)

  

**小節単位の貼り付け**
  

 小節単位でまとめ選択後、ポジションカーソルを小節の先頭にして貼り付けると、「小節単位の貼り付け」となり、テンポと強弱記号に加えて拍子と調号も貼り付けられます。貼り付け先の拍子が違うときは小節が伸縮します。
   

 ※たとえば「4/4拍子」の小節をコピーして、「3/4拍子」の小節に貼り付けると1拍長く補正されます。
   

 ※小節単位でコピーしていないときや、ポジションカーソルが小節の先頭ではないときは、拍子と調号の貼り付けや小節の伸縮は行われません。
   

  

**テンポ・拍子の変化**
  

 テンポと拍子は全ソングトラックで共通のため、まとめ選択後の削除／切り取り／貼り付けで、テンポまたは拍子が変化するとプロジェクト内の全ソングトラックが影響を受けます。
   

  

**ミックスコピー**
  

 範囲指定後、右クリックメニューの「ミックスコピー」やショートカットキー[Ctrl+Shift+C]で、既定値の部分も含めた全パラメータと音符をコピーできます。
   

 まとめ選択＋ミックスコピーで、トラックの一部または全体の音符とパラメータを、簡単に別の位置／トラックに複製できます。あるキャストで調整した歌を、別のキャストに貼り付けて歌わせてみることも可能です。
   

 ※調整値としての反映のため、別のキャスト用のパラメータを適用しても、うまく歌えない場合があります。同じキャストでもコピー元と別の場所では完全に同じ歌唱になりません。必要に応じて再調整してください。
   

  


![](../../image/V8.4.5_mixcopy.png)

ペンツール
-----


 ドラッグ操作で値を調整します。調整した値はオレンジ色で表示されます。
   

 ※重ね表示や接続調整中は、有効な値（調整した部分は調整値）のみが表示されます。
   

  

**接続調整モード**
  

 ピッチやボリューム、ビブラートの調整中、[Alt]キーを押しながらドラッグすると、元の値に綺麗に接続するラインを描くことができます。
   

  


![](../../image/20170329_02.png)

  

 ・[Alt]キーを押しながらドラッグすると赤い線が描かれ、[Alt]キーを離すと赤い線と元の線の接続箇所から接続箇所までが調整値として反映されます。
   

  

 ・[Alt]キー押下中は調整値を反映した1本線の表示になるため、有効な値を簡単に確認できます。
   

 ※ドラッグせずに[Alt]キーを離すと、メニューにフォーカスが移りますが、[Alt]キーを長押しすると再度確認できます。
   

ラインツール
------


 ドラッグ操作で直線的に値を調整します。調整した値はオレンジ色で表示されます。
   

 [Shift]キーを押しながらドラッグすると、水平線を引くことができます。
   

 なお、タイミング調整画面では線を引くことはできないため、ペンツールと同じ働きになります。
   

  


![](../../image/st05_10.png)

消しゴムツール
-------


 ドラッグ操作で調整値を削除して、元の値に戻します。
   

 ピッチとビブラートの振幅／周期の調整画面では、[Shift]キーを押しながらドラッグして元の値を削除（無効化）することもできます。
   

  


![](../../image/st05_19.png.1378885685993.png)





