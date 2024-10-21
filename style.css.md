/* 全体のbody設定 */
html{
  margin:0 auto;
  padding:5px;
  line-height: 120%;
  font-weight:normal;
  font-family: "Lucida Grande", "segoe UI", "ヒラギノ角ゴ ProN W3", "Hiragino Kaku Gothic ProN", Meiryo, Verdana, Arial, sans-serif;
  font-size: 13px;
  color:#3b3b3b;
}

body{
  margin:0 auto;
  width : 1000px;
  font-weight:normal;
  font-family: "Lucida Grande", "segoe UI", "ヒラギノ角ゴ ProN W3", "Hiragino Kaku Gothic ProN", Meiryo, Verdana, Arial, sans-serif;
  font-size: 13px;
  color:#3b3b3b;
}

img{
  max-width: 100%;
}

/* リンク色（通常） */
a:link{
  text-decoration:none;
  color:#128bd1;
}

/* リンク色（訪問済み） */
a:visited{
  text-decoration:none;
  cursor:auto;
  color:#128bd1;
}

/* リンク色（マウスオーバー時） */
a:hover{
  text-decoration: underline;
  color:#e5006e;
}

/* サイトヘッダー */
.header{
  margin:0 auto;
  height: 88px;
  text-align: left;
}

/* メインブロック要素 */
.main{
  background-color: #FFFFFF;
  display: flex;
}

/* ナビゲーションボックス */
.left_nav{
  min-width : 220px;
  line-height: 60%;
}

/* ナビゲーションアコーディオン */

input[name=navinput]{
  display: none;
}

.listnav01:hover,
.listnav02:hover,
.listnav03:hover,
.listnav04:hover{
  color: #999;
}
.listnav01:before,
.listnav02:before,
.listnav03:before,
.listnav04:before{
  content: "▼  ";
}
#nav01:checked ~ .title .listnav01:before,
#nav02:checked ~ .title .listnav02:before,
#nav03:checked ~ .title .listnav03:before,
#nav04:checked ~ .title .listnav04:before{
  content: "▶  ";
}
.box{
  height: auto;
  opacity: 1;
  overflow: hidden;
  padding: 0px 12px;
  line-height: 160%;
}
#nav01:checked ~ .box01,
#nav02:checked ~ .box02,
#nav03:checked ~ .box03,
#nav04:checked ~ .box04{
  height: 0;
  opacity: 0;
  background: #FFFFFF;
  padding: 0 10px;
  line-height: 120%;
}

/* 見出し設定 */

h1{
  color:#e5006f;
  font-size: 20px;
  margin: 0 0 0.5rem 0;
}

h2 {
  position: relative;
  padding: 0.5rem 0;
  color:#0082cd;
  font-size: 16px;
}

h2:after {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height: 2px;
  content: '';
  border-radius: 2px;
  background-image: -webkit-gradient(linear, right top, left top, from(#ffd900), to(#22d8ff));
  background-image: -webkit-linear-gradient(right, #ffd900 0%, #22d8ff 100%);
  background-image: linear-gradient(to left, #ffd900 0%, #22d8ff 100%);
}

h3 {
  color:#0083ce;
  font-size: 16px;
  margin: 0.5rem 0;
}

.box30 {
    width : 600px;
    margin: 1.5em 0;
    background: #FFFFFF;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.22);
}
.box30 .box-title {
    font-size: 14px;
    background: #898989;
    padding: 5px 10px;
    text-align: left;
    color: #FFF;
}
.box30 p {
    font-size: 12px;
    padding: 10px 10px;
    margin: 0;
    line-height: 140%;
    font-family: monospace;
}
.box30 blockquote {
    font-size: 12px;
    line-height: 140%;
    font-family: monospace;
}

/* 右ウィンドウ要素 */
.window{
  width : 770px;
  background: #fcfcfc;
}

/* 右ウィンドウ内メインコンテンツ要素 */
.content{
  padding: 16px 16px;
}
.main_text{
  line-height: 180%;
  padding-left: 0px;
}

.content a:link{
  text-decoration: underline;
}

/* サイトフッター */
.footer{
  margin:0 auto;
  height: 20px;
  background: #FFFFFF;
  text-align: center;
  padding: 10px;
}