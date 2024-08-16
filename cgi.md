

---

@charset "euc-jp";
body 
{
	-webkit-text-size-adjust: 100%;
	background-color:#F6C8BF;
	font-family: Osaka,"ＭＳ Ｐゴシック","MS PGothic","ヒラギノ角ゴ Pro W3", "Hiragino Kaku Gothic Pro";
	margin: 4px;
}


a
{
	text-decoration: none;
}

.htmlall
{
	width:100%;
	text-align:center;
	margin: 0 auto;
}

/*ヘッダ*/
.htmlheader
{
	max-width: 500px;
	min-width: 260px;
	padding: 10px 0px 10px 0px;
	text-align:center;
	background-color:#FFFFEF;
	margin: 0 auto;

/*
	サイドバナー表示用
	background-image: url("banner.gif");
	background-repeat: no-repeat;
	background-position: left middle;

	box-shadow: 2px 2px 3px 1px #666;
	-moz-box-shadow: 2px 2px 3px 1px #666;
	-webkit-box-shadow: 2px 2px 3px 1px #666;
*/
	border-radius: 10px;
	-webkit-border-radius: 10px;
	-moz-border-radius: 10px;
}

/*選択枠*/
.htmlmain
{
	max-width: 400px;
	min-width: 260px;
	text-align:left;
	background-color:#FFFFEF;
	margin: 10px auto;
	padding: 10px 10px 10px 10px;

	border-radius: 10px;
	-webkit-border-radius: 10px;
	-moz-border-radius: 10px;
}

/*フッタ(病院名表示部分)*/
.htmlfooter
{
	width:100%;
	padding: 10px 0px 10px 0px;
	font-size:small;
	text-align:center;
	margin: 0 auto;
}


/*ヘッダ・病院名*/
.headerAhName
{
	font-size: 150%;
	padding-bottom:10px;
/*
	トップバナー表示用
	display:none;
*/
}

/*ヘッダ・タイトル*/
.headerTitle
{
	font-size: 150%;
/*
	トップバナー表示用
	padding-top:40px;
	padding-bottom:10px;
	background-image: url("banner.gif");
	background-repeat: no-repeat;
	background-position: center top;
*/
}

/*ページタイトル*/
.pageTitle
{
	font-weight:bold;
}

/*コンテンツ枠*/
.content
{
	max-width: 500px;
	min-width: 260px;
	margin: 0 auto;
	text-align:center;
	padding-top:10px;
}

input
{
	vertical-align:top;
}

/*送信ボタン(submit)*/
input[type="submit"]
{
	font-size: 120%;
	font-weight: bold;
	background-color: #0099CC;
	border: 1px solid #000000;
	color:#FFFFFF;
	padding: 6px 12px 6px 12px;
	margin:5px;
	min-width:130px;
	
	box-shadow: 2px 2px 3px 1px #666;
	-moz-box-shadow: 2px 2px 3px 1px #666;
	-webkit-box-shadow: 2px 2px 3px 1px #666;
}

input[type="submit"]:hover
{
	background-color: #FF0000;
}

input[type="submit"]:disabled
{
	background-color: #CCCCCC;
}

/*入力枠(通常)*/
input[type="text"]
{
	font-size: 130%;
}

/*入力枠(TEL)*/
input[type="tel"]
{
	font-size: 130%;
}

/*入力枠(パスワード)*/
input[type="password"]
{
	font-size: 130%;
}

/*入力枠(メール)*/
input[type="email"]
{
	font-size: 130%;
}


.submitDiv
{
	text-align:center;
	margin:0;
	padding:0;
}

/* 各メッセージ枠 */
.message
{
	text-align:center;
	padding-top:10px;
}


/*枠内のリンク*/
.htmlmain a
{
	display:inline-block;
	font-size: 100%;
	font-weight: bold;
	background-color: #0099CC;
	border: 1px solid #000000;
	color:#FFFFFF;
	padding: 3px 12px 3px 12px;
	margin:5px;
	min-width:110px;
	
	box-shadow: 2px 2px 3px 1px #666;
	-moz-box-shadow: 2px 2px 3px 1px #666;
	-webkit-box-shadow: 2px 2px 3px 1px #666;
}

.htmlmain a:hover
{
	background-color: #FF0000;
}

.htmlmain a:disabled
{
	background-color: #CCCCCC;
}

label
{
	display:inline-block;
	font-weight: bold;
	padding: 3px 12px 3px 12px;
	margin:5px;
}

/*待ち状況に戻るリンク*/
#linkWaitReturn a
{
	display:inline-block;
	font-size: 100%;
	font-weight: nolmal;
	background-color: transparent;
	border: none;
	color:blue;
	padding: 3px 12px 3px 12px;
	margin:5px;
	min-width:0px;
	box-shadow: none;
	-moz-box-shadow: none;
	-webkit-box-shadow: none;
}

/*1つ前に戻るリンク*/
#linkReturn a
{
	display:inline-block;
	font-size: 100%;
	font-weight: nolmal;
	background-color: transparent;
	border: none;
	color:blue;
	padding: 3px 12px 3px 12px;
	margin:5px;
	min-width:0px;
	box-shadow: none;
	-moz-box-shadow: none;
	-webkit-box-shadow: none;
}

/*現在日時*/
.nowTime
{
	font-weight:bold;
}



/*戻るリンク枠*/
.retLink
{
	max-width: 450px;
	min-width: 300px;
	padding: 10px 0px 0px 0px;
	text-align:center;
	margin: 0 auto;
}


---
