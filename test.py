

import time
from lxml import etree


html = '''
<!DOCTYPE html>
<html lang="zh-CN" class="ua-mac ua-webkit">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="renderer" content="webkit">
    <meta name="referrer" content="always">
    <meta name="google-site-verification" content="ok0wCgT20tBBgo9_zat2iAcimtN4Ftf5ccsh092Xeyw" />
    <title>
搜索:天之骄子
</title>
    
    
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="Sun, 6 Mar 2005 01:00:00 GMT">
    
  <link rel="search" type="application/opensearchdescription+xml"
   title="豆瓣小组" href="https://www.douban.com/group/opensearch">

    <script >var _head_start = new Date();</script>
    <script src="https://img3.doubanio.com/f/shire/72ced6df41d4d158420cebdd254f9562942464e3/js/jquery.min.js"></script>
    <script src="https://img3.doubanio.com/f/shire/22ee83f45f94c7a90e73e0ee4acd18f902a6991f/js/douban.js"></script>
    <link href="https://img3.doubanio.com/f/shire/6522c42d2aba9757aeefa0c35cc0cefc9229747c/css/douban.css" rel="stylesheet" type="text/css">
    <style type="text/css">
    
        a:link { color: #259; }
        a:visited { color: #769; }
        a:hover { color: #fff; }
        a:active { color: #fff; }
        
    </style>
    
    <style type="text/css">
.nav{width:100%;min-width:950px;overflow:hidden;zoom:1;margin-bottom:40px}.nav .nav-wrap{border-bottom:1px solid #e5ebe4}.nav .nav-primary,.nav .nav-secondary{width:950px;margin:0 auto;padding-bottom:0;overflow:hidden;zoom:1}.nav .nav-primary{position:relative;padding:10px 0 5px;overflow:hidden;zoom:1}.nav .nav-logo{float:left;height:56px;width:145px;margin:0 13px 0 0;background:url(https://img3.doubanio.com/f/shire/8308f83ca66946299fc80efb1f10ea21f99ec2a5/pics/nav/lg_main_a11_1.png) no-repeat 0 12px;background-image:-webkit-image-set(url(https://img3.doubanio.com/f/shire/8308f83ca66946299fc80efb1f10ea21f99ec2a5/pics/nav/lg_main_a11_1.png) 1x, url(https://img3.doubanio.com/f/shire/8977fa054324c4c7f565447b003ebf75e9b4f9c6/pics/nav/lg_main@2x.png) 2x);background-image:-moz-image-set(url(https://img3.doubanio.com/f/shire/8308f83ca66946299fc80efb1f10ea21f99ec2a5/pics/nav/lg_main_a11_1.png) 1x, url(https://img3.doubanio.com/f/shire/8977fa054324c4c7f565447b003ebf75e9b4f9c6/pics/nav/lg_main@2x.png) 2x);background-image:-ms-image-set(url(https://img3.doubanio.com/f/shire/8308f83ca66946299fc80efb1f10ea21f99ec2a5/pics/nav/lg_main_a11_1.png) 1x, url(https://img3.doubanio.com/f/shire/8977fa054324c4c7f565447b003ebf75e9b4f9c6/pics/nav/lg_main@2x.png) 2x);background-image:-o-image-set(url(https://img3.doubanio.com/f/shire/8308f83ca66946299fc80efb1f10ea21f99ec2a5/pics/nav/lg_main_a11_1.png) 1x, url(https://img3.doubanio.com/f/shire/8977fa054324c4c7f565447b003ebf75e9b4f9c6/pics/nav/lg_main@2x.png) 2x)}.nav .nav-logo a{display:block;width:100%;height:100%;overflow:hidden;line-height:100em}.nav .nav-logo a:hover,.nav .nav-logo a:active{background:none !important}.ua-iphone .nav{-webkit-text-size-adjust:none}.nav-search{position:relative;overflow:hidden;zoom:1;padding:10px 0 15px 0}.nav-search input{-webkit-appearance:none;border:none;background:transparent}.nav-search label{position:absolute;left:11px;top:10px;line-height:30px;cursor:text;color:#bbb;width:auto}.nav-search ::-webkit-input-placeholder{color:#bbb}.nav-search :-moz-placeholder{color:#bbb}.nav-search ::-moz-placeholder{color:#bbb}.nav-search :-ms-input-placeholder{color:#bbb}.nav-search .inp{float:left;width:470px;height:34px;text-align:center;_margin-right:-3px;cursor:text;background:url(https://img3.doubanio.com/f/shire/d45aaa7569335285e298dd7f3c045c8b364a19de/pics/nav1/nav_bg_a1.png) no-repeat 0 0}.nav-search .inp input{background:#fff;width:96%;margin:0;text-align:left;height:30px;padding-left:10px;height:28px\9;line-height:28px\9;outline:none}.nav-search legend{display:none}.nav-search fieldset{border:none;padding:0;margin:0;position:static}.nav-search .inp-btn{position:relative;left:-1px;*top:-1px;width:37px;height:34px;zoom:1;overflow:hidden}.nav-search .inp-btn input{width:100%;height:100%;font-size:0;padding:35px 0 0 0;overflow:hidden;background:url(https://img3.doubanio.com/f/shire/d45aaa7569335285e298dd7f3c045c8b364a19de/pics/nav1/nav_bg_a1.png) no-repeat 0 -40px;color:transparent;cursor:pointer}.nav-search .inp-btn input:hover{background-position:-40px -40px}.nav-search .inp-btn input:active{background-position:0 -40px}.nav-secondary{width:100%;zoom:1}.nav-secondary:after{content:'\0020';display:block;clear:both}.nav-secondary img{vertical-align:middle;margin-right:4px}.nav-secondary ul{margin:9px 0}.nav-secondary li{display:inline;margin-right:30px}.nav-secondary .nav-items{float:none;*padding-bottom:8px;zoom:1;font-size:13px}.nav-secondary .nav-items li{_float:left;_display:inline}#db-nav-book .nav-search .inp{background-image:url(https://img3.doubanio.com/f/shire/d45aaa7569335285e298dd7f3c045c8b364a19de/pics/nav1/nav_bg_a1.png)}#db-nav-book .nav-search .inp-btn input{background-image:url(https://img3.doubanio.com/f/shire/d45aaa7569335285e298dd7f3c045c8b364a19de/pics/nav1/nav_bg_a1.png)}#db-nav-movie .nav-search .inp{background-image:url(https://img3.doubanio.com/f/shire/44552ac9f592ad9d2ef5c8ae708533990e94b605/pics/nav1/nav_mv_bg.png)}#db-nav-movie .nav-search .inp-btn input{background-image:url(https://img3.doubanio.com/f/shire/44552ac9f592ad9d2ef5c8ae708533990e94b605/pics/nav1/nav_mv_bg.png)}#db-nav-group .nav-search .inp{background-image:url(https://img3.doubanio.com/f/shire/44552ac9f592ad9d2ef5c8ae708533990e94b605/pics/nav1/nav_mv_bg.png)}#db-nav-group .nav-search .inp-btn input{background-image:url(https://img3.doubanio.com/f/shire/44552ac9f592ad9d2ef5c8ae708533990e94b605/pics/nav1/nav_mv_bg.png)}#db-nav-music .nav-search .inp{background-image:url(https://img3.doubanio.com/f/shire/b78a848a3825bda97797e3c1816ad3b01139aa1c/pics/nav1/nav_mu_bg.png)}#db-nav-music .nav-search .inp-btn input{background-image:url(https://img3.doubanio.com/f/shire/b78a848a3825bda97797e3c1816ad3b01139aa1c/pics/nav1/nav_mu_bg.png)}

.clearfix:after{content:".";display:block;height:0;visibility:hidden;clear:both}.clearfix{*zoom:1}#db-nav-group{position:relative;background:#f0f6f3;overflow:visible}#db-nav-group .nav-wrap{border:none}#db-nav-group .nav-primary{overflow:visible;padding:12px 0 6px 0}#db-nav-group .nav-logo{background-image:url(https://img3.doubanio.com/f/shire/b5060283627046173eedb53e90e1733059c0a71c/pics/nav/lg_group_a11_2.png);background-image:-webkit-image-set(url(https://img3.doubanio.com/f/shire/b5060283627046173eedb53e90e1733059c0a71c/pics/nav/lg_group_a11_2.png) 1x, url(https://img3.doubanio.com/f/shire/86033885f71d164e11b4ecc2fc06e945fe01c10b/pics/nav/lg_group_a11@2x.png) 2x);background-image:-moz-image-set(url(https://img3.doubanio.com/f/shire/b5060283627046173eedb53e90e1733059c0a71c/pics/nav/lg_group_a11_2.png) 1x, url(https://img3.doubanio.com/f/shire/86033885f71d164e11b4ecc2fc06e945fe01c10b/pics/nav/lg_group_a11@2x.png) 2x);background-image:-ms-image-set(url(https://img3.doubanio.com/f/shire/b5060283627046173eedb53e90e1733059c0a71c/pics/nav/lg_group_a11_2.png) 1x, url(https://img3.doubanio.com/f/shire/86033885f71d164e11b4ecc2fc06e945fe01c10b/pics/nav/lg_group_a11@2x.png) 2x);background-image:-o-image-set(url(https://img3.doubanio.com/f/shire/b5060283627046173eedb53e90e1733059c0a71c/pics/nav/lg_group_a11_2.png) 1x, url(https://img3.doubanio.com/f/shire/86033885f71d164e11b4ecc2fc06e945fe01c10b/pics/nav/lg_group_a11@2x.png) 2x)}#db-nav-group a:link,#db-nav-group a:visited{color:#037b82}#db-nav-group a:hover,#db-nav-group a:active{background-color:#037b82;color:#fff}#db-nav-group .nav-search{position:absolute;right:0;*width:282px}#db-nav-group li{display:inline}#db-nav-group .nav-items{float:left;margin-top:15px}#db-nav-group .nav-items li{margin-right:30px;font-size:15px}#db-nav-group .nav-search label{top:11px;line-height:28px}#db-nav-group .nav-search .inp{width:278px;height:28px;background:#fff;border:1px solid #e1e9e1;text-align:left;-webkit-border-radius:0;-moz-border-radius:0;border-radius:0}#db-nav-group .nav-search .inp input{margin:0;width:242px;height:28px;line-height:"26px	"}#db-nav-group .nav-search .inp-btn{position:absolute;left:auto;top:10px;right:0;width:30px;height:28px;*height:30px;border:1px solid #e1e9e1;border-left:none;background-color:#fff;font-size:0;overflow:hidden}#db-nav-group .nav-search .inp-btn input{width:30px;height:28px;*height:30px;padding:0;margin:0;line-height:100px;background:transparent url(https://img3.doubanio.com/f/shire/f71f15922ebd7c0ff0ea0e7a25577529efd8981a/pics/icon/bn_srh_1.png) no-repeat 50% 50%}.nlst,.nlst h3,.bg-img-green h4{background-color:#f0f6f3}

</style><style type="text/css">
.grid-16-8 .article{width:590px}.grid-16-8 .aside{width:300px}.paginator .thispage{background-color:#6ebfc3}h1{margin-bottom:25px;padding:0;font-weight:normal}.groups{overflow:hidden}.groups .result .pic{float:left;margin-right:25px;padding-top:0}.olt .td-subject{padding:8px 0 6px 3px;font-size:13px}.olt .td-time{width:80px}.olt .td-reply{width:80px}.count{white-space:nowrap}.result{margin:0;padding-bottom:15px;border-top:0;border-bottom:1px dashed #ccc}.result .pic{padding-top:20px}.result .title h3{margin-bottom:0}.result .info{margin-bottom:4px}.result .content{border:0}.result .content p{color:#666}.srh-tabs{border-bottom:1px solid #ccc;letter-spacing:-0.31em;*letter-spacing:normal;word-spacing:-0.43em}.srh-tabs li{display:inline-block;*display:inline;zoom:1;letter-spacing:normal;word-spacing:normal;padding-bottom:10px}.srh-tabs li a{display:block;padding:2px 18px;margin-right:10px;line-height:1.4}.srh-tabs .on a:link,.srh-tabs .on a:visited,.srh-tabs .on a:hover,.srh-tabs .on a:active{background-color:#70c0c0;color:#fff;border-radius:3px}.group-search{overflow:hidden;zoom:1;border-bottom:1px solid #ddd}.group-search fieldset{display:block;padding:8px 0;background:#f8f8f8;text-align:center;border:0}.group-search .inp{width:400px;border:1px solid #ccc;padding:0 2px;height:24px;*line-height:24px}.group-search .bn-srh{border:0;background:#6ebfc3;color:#fff;height:24px;padding:2px 15px;border-radius:3px;cursor:pointer}.side-nav{font-size:14px}
</style><style type="text/css">
.srh-filter { float:right; }
.srh-filter li { display:inline;color:#999; }
.srh-filter li i { margin:0 4px;font-size:14px; }
.srh-filter li.on a:link,
.srh-filter li.on a:visited,
.srh-filter li.on a:hover,
.srh-filter li.on a:active { color:#333;background:transparent;cursor:default; }
</style><style type="text/css">
  .search_report { margin: 15px 10px 20px 0;}
  .search_report a:link { font-size: 14px; }
  .search_report a:link,
  .search_report a:hover,
  .search_report a:visited,
  .search_report a:active { color: #37a; }
  .search_report a:hover { color:#fff; background-color: #37a; }

    #feedback-iframe {
      position: fixed;
      left: 0;
      top: 0;
      width: 100%;
      height: 100%;
      border: none;
      display: none;
      z-index: 999;
    }
  </style><style type="text/css">
@font-face{font-family:"groupicons";src:url(https://img3.doubanio.com/f/group/538e8d0d55ffbf1f775c7c9519c42db2cab4b430/pics/group/fonts/groupicons.eot);src:url(https://img3.doubanio.com/f/group/538e8d0d55ffbf1f775c7c9519c42db2cab4b430/pics/group/fonts/groupicons.eot) format("embedded-opentype"),url(https://img3.doubanio.com/f/group/a66eeba150d7ec8b5eace9c414a1f485b4339151/pics/group/fonts/groupicons.woff) format("woff"),url(https://img3.doubanio.com/f/group/c61ea0a5cc2e9161108f940debbe7b87292a1d02/pics/group/fonts/groupicons.ttf) format("truetype"),url(https://img3.doubanio.com/f/group/0f0f6589afa6948c5f89cc9c611cc7aec2d7498a/pics/group/fonts/groupicons.svg) format("svg");font-weight:normal;font-style:normal}[data-icon]:before,.item-3rd .item-weibo:before,.groupicon-weibo:before,.item-3rd .item-qq:before,.groupicon-qq:before{font-family:"groupicons";speak:none;font-style:normal;font-weight:normal;font-variant:normal;text-transform:none;line-height:1;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale}.item-3rd .item-qq:before,.groupicon-qq:before{content:"\e600"}.item-3rd .item-weibo:before,.groupicon-weibo:before{content:"\e601"}[data-icon]:before{content:attr(data-icon)}#wrapper.landing{padding-bottom:61px}.popup-reg-mask{position:absolute;top:0;left:0;width:100%;height:100%;background:#000;opacity:0.4;filter:alpha(opacity=40)}#g-popup-reg{position:fixed;z-index:100;left:50%;top:20%;margin-left:-170px;overflow:hidden;_position:absolute;_margin-top:0;-webkit-box-shadow:0 0 4px 0 rgba(0,0,0,0.2);-moz-box-shadow:0 0 4px 0 rgba(0,0,0,0.2);-o-box-shadow:0 0 4px 0 rgba(0,0,0,0.2);-ms-box-shadow:0 0 4px 0 rgba(0,0,0,0.2);box-shadow:0 0 4px 0 rgba(0,0,0,0.2)}* html{background-image:url(about:blank);background-attachment:fixed}#g-popup-reg .bd{border:1px solid #eee;background:#fff}#g-popup-reg iframe{width:340px;height:448px}#g-popup-reg .lnk-close{position:absolute;left:10px;top:10px}#g-popup-reg .lnk-close:link,#g-popup-reg .lnk-close:visited,#g-popup-reg .lnk-close:hover,#g-popup-reg .lnk-close:active{padding:0 2px;line-height:1;font-size:18px;color:#aaa}#g-popup-reg .lnk-close:hover{color:#fff}#landing-bar{position:fixed;bottom:0;height:60px;width:100%;border-top:1px solid #dee2de;background:#ecf6ed}#landing-bar .bd{position:relative;width:950px;padding-top:15px;margin:0 auto}#landing-bar p{float:left;margin:0 60px 15px 80px;font-size:18px;color:#072;-webkit-font-smoothing:antialiased}#landing-bar .operation{float:left;margin-right:10px}#landing-bar .operation a{display:inline-block;border:1px solid #538643;padding:3px 16px;margin-right:12px;font-size:14px;background:#3fa156;color:#fff;border-radius:2px}#landing-bar .operation .a_show_login{background:#ecf6ed;color:#3fa156}.item-3rd{font-size:13px;line-height:30px;color:#999}.item-3rd a{border-radius:50%;padding:5px 6px 4px;margin-right:5px;color:#fff;font-size:15px}.item-3rd .item-qq{background:#0097e2}.item-3rd .item-qq img{display:none;*display:inline-block}.item-3rd .item-weibo{background:#f32935}.item-3rd .item-weibo img{display:none;*display:inline-block}#landing-bar .lnk-close{position:absolute;top:0;right:0;padding:0 2px;font-size:40px;line-height:1.4;color:#aaa;font-weight:lighter;-webkit-font-smoothing:antialiased}#landing-bar .lnk-close:hover{background:none}

</style>
    <script></script>

    <link rel="stylesheet" href="https://img3.doubanio.com/f/group/2f4c6f83940e2bbb76f5a23a7d987b9093919799/css/group/init.css">

    <link rel="shortcut icon" href="https://img3.doubanio.com/favicon.ico" type="image/x-icon">
</head>

<body>
  
    
    <script type="text/javascript">var _body_start = new Date();</script>
    
   



    <link href="//img3.doubanio.com/dae/accounts/resources/d3e2921/shire/bundle.css" rel="stylesheet" type="text/css">



<div id="db-global-nav" class="global-nav">
  <div class="bd">
    
<div class="top-nav-info">
  <a href="https://accounts.douban.com/passport/login?source=group" class="nav-login" rel="nofollow">登录/注册</a>
</div>


    <div class="top-nav-doubanapp">
  <a href="https://www.douban.com/doubanapp/app?channel=top-nav" class="lnk-doubanapp">下载豆瓣客户端</a>
  <div id="doubanapp-tip">
    <a href="https://www.douban.com/doubanapp/app?channel=qipao" class="tip-link">豆瓣 <span class="version">6.0</span> 全新发布</a>
    <a href="javascript: void 0;" class="tip-close">×</a>
  </div>
  <div id="top-nav-appintro" class="more-items">
    <p class="appintro-title">豆瓣</p>
    <p class="qrcode">扫码直接下载</p>
    <div class="download">
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=iOS">iPhone</a>
      <span>·</span>
      <a href="https://www.douban.com/doubanapp/redirect?channel=top-nav&direct_dl=1&download=Android" class="download-android">Android</a>
    </div>
  </div>
</div>

    


<div class="global-nav-items">
  <ul>
    <li class="">
      <a href="https://www.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-main&quot;,&quot;uid&quot;:&quot;0&quot;}">豆瓣</a>
    </li>
    <li class="">
      <a href="https://book.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-book&quot;,&quot;uid&quot;:&quot;0&quot;}">读书</a>
    </li>
    <li class="">
      <a href="https://movie.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-movie&quot;,&quot;uid&quot;:&quot;0&quot;}">电影</a>
    </li>
    <li class="">
      <a href="https://music.douban.com" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-music&quot;,&quot;uid&quot;:&quot;0&quot;}">音乐</a>
    </li>
    <li class="">
      <a href="https://www.douban.com/location" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-location&quot;,&quot;uid&quot;:&quot;0&quot;}">同城</a>
    </li>
    <li class="on">
      <a href="https://www.douban.com/group"  data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-group&quot;,&quot;uid&quot;:&quot;0&quot;}">小组</a>
    </li>
    <li class="">
      <a href="https://read.douban.com&#47;?dcs=top-nav&amp;dcm=douban" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-read&quot;,&quot;uid&quot;:&quot;0&quot;}">阅读</a>
    </li>
    <li class="">
      <a href="https://douban.fm&#47;?from_=shire_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-fm&quot;,&quot;uid&quot;:&quot;0&quot;}">FM</a>
    </li>
    <li class="">
      <a href="https://time.douban.com&#47;?dt_time_source=douban-web_top_nav" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-time&quot;,&quot;uid&quot;:&quot;0&quot;}">时间</a>
    </li>
    <li class="">
      <a href="https://market.douban.com&#47;?utm_campaign=douban_top_nav&amp;utm_source=douban&amp;utm_medium=pc_web" target="_blank" data-moreurl-dict="{&quot;from&quot;:&quot;top-nav-click-market&quot;,&quot;uid&quot;:&quot;0&quot;}">豆品</a>
    </li>
  </ul>
</div>

  </div>
</div>
<script>
  ;window._GLOBAL_NAV = {
    DOUBAN_URL: "https://www.douban.com",
    N_NEW_NOTIS: 0,
    N_NEW_DOUMAIL: 0
  };
</script>



    <script src="//img3.doubanio.com/dae/accounts/resources/d3e2921/shire/bundle.js" defer="defer"></script>




      
    









<div id="db-nav-group" class="nav">
  <div class="nav-wrap">
  <div class="nav-primary clearfix">
    <div class="nav-logo">
      <a href="https://www.douban.com/group/">豆瓣小组</a>
    </div>

    <div class="nav-items">
    <ul>
      <li><a href="https://www.douban.com/group/explore">精选</a></li>
      <li><a href="https://www.douban.com/group/explore/culture">文化</a></li>
      <li><a href="https://www.douban.com/group/explore/travel">行摄</a></li>
      <li><a href="https://www.douban.com/group/explore/ent">娱乐</a></li>
      <li><a href="https://www.douban.com/group/explore/fashion">时尚</a></li>
      <li><a href="https://www.douban.com/group/explore/life">生活</a></li>
      <li><a href="https://www.douban.com/group/explore/tech">科技</a></li>
   </ul>
   </div>

    <div class="nav-search">
      <form id='form' action="https://www.douban.com/group/search" method="get">
        <fieldset>
          <legend>搜索：</legend>
          
          <input type="hidden" name="cat" value="1013" />
          <label for="inp-query">小组、话题</label>
          <div class="inp"><input id="inp-query" name="q" size="22" maxlength="60" value=""></div>
          <input type="hidden" name="sort" value="time" />
          <div class="inp-btn"><input type="submit" value="搜索"></div>
        </fieldset>
      </form>
    </div>
  </div>
  </div>

</div>

<script>
Do(function(){
  var nav = $('#db-nav-group');
  var inp=$("#inp-query"),label=inp.closest(".nav-search").find("label");inp[0]&&"placeholder"in inp[0]?(label.hide(),inp.attr("placeholder",label.text())):(""!==inp.val()&&label.hide(),inp.parent().click(function(){inp.focus(),label.hide()}).end().focusin(function(){label.hide()}).focusout(function(){""===$.trim(this.value)?label.show():label.hide()}).keydown(function(){label.hide()})),inp.parents("form").submit(function(){if(!$.trim(inp.val()).length)return!1}),nav.find(".lnk-more, .lnk-account").click(function(n){n.preventDefault();var i,e=$(this),t=e.hasClass("lnk-more")?$("#db-productions"):$("#db-usr-setting");t.data("init")||(i=e.offset(),t.css({"margin-left":i.left-$(window).width()/2-t.width()+e.width()+parseInt(e.css("padding-right"),10)+"px",left:"50%",top:i.top+e.height()+"px"}),t.data("init",1),t.hide(),$("body").click(function(n){var i=$(n.target);i.hasClass("lnk-more")||i.hasClass("lnk-account")||i.closest("#db-usr-setting").length||i.closest("#db-productions").length||t.hide()})),"none"===t.css("display")?($(".dropdown").hide(),t.show()):$(".dropdown").hide()});
});
</script>




    <div id="wrapper">
        

        
<div id="content">
    
    <h1><div>
   天之骄子 小组讨论搜索:天之骄子
  </div></h1>

    <div class="grid-16-8 clearfix">
        
        
        <div class="article">
               



<div class="group-search">
  <form action="/group/search">
  <fieldset>
    <input type="hidden" value="1013" name="cat"/>
    <input type="hidden" value="634832" name="group"/>
    <input type="hidden" value="time" name="sort">
    <input type="text" name="q" value="天之骄子" class="inp">
    <input type="submit" value="搜索" class="bn-srh">
  </fieldset>
  </form>


<div class="srh-filter">
  <ul>
    
    <li class=on>
      <a href="/group/search?cat=1013&amp;group=634832&amp;q=%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90&amp;sort=time">最新发布</a> <i>/</i>
    <li >
      <a href="/group/search?cat=1013&amp;group=634832&amp;q=%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90&amp;sort=relevance">相关度</a>
  </ul>
</div>

</div>

        
            <div class="topics">
                <table class="olt">
                    <tbody>
                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/235084055/" onclick="moreurl(this,{i: '0', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 235084055})" title="人才公寓排队要多久">人才公寓排队要多久</a></td>
    <td class="td-time" title="2021-07-15 14:34:29" nowrap="nowrap"><span class="">55分钟前</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/235032381/" onclick="moreurl(this,{i: '1', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 235032381})" title="求租｜天之骄子">求租｜天之骄子</a></td>
    <td class="td-time" title="2021-07-15 00:34:20" nowrap="nowrap"><span class="">今天00:34</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/234937162/" onclick="moreurl(this,{i: '2', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 234937162})" title="求租天之骄子小户型，无需租赁备案，无需暂住证明，事少不磨叽，中介勿扰">求租天之骄子小户型，无需租赁备案，无需暂住证明...</a></td>
    <td class="td-time" title="2021-07-14 11:18:57" nowrap="nowrap"><span class="">昨天11:18</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/234803948/" onclick="moreurl(this,{i: '3', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 234803948})" title="天之骄子一室户 45平带全套家电 限女生 中介勿扰">天之骄子一室户 45平带全套家电 限女生 中介勿扰</a></td>
    <td class="td-time" title="2021-07-13 10:49:05" nowrap="nowrap"><span class="">07-13</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">3回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/234755989/" onclick="moreurl(this,{i: '4', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 234755989})" title="求租天之骄子一室户八月7号前可入住">求租天之骄子一室户八月7号前可入住</a></td>
    <td class="td-time" title="2021-07-12 22:06:50" nowrap="nowrap"><span class="">07-12</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">1回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/234722272/" onclick="moreurl(this,{i: '5', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 234722272})" title="天之骄子一室一厅一卫户型">天之骄子一室一厅一卫户型</a></td>
    <td class="td-time" title="2021-07-12 17:32:20" nowrap="nowrap"><span class="">07-12</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">1回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/234673205/" onclick="moreurl(this,{i: '6', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 234673205})" title="已租">已租</a></td>
    <td class="td-time" title="2021-07-12 11:24:33" nowrap="nowrap"><span class="">07-12</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">7回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/234655208/" onclick="moreurl(this,{i: '7', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 234655208})" title="天之骄子45平一室户中介勿扰 限女生">天之骄子45平一室户中介勿扰 限女生</a></td>
    <td class="td-time" title="2021-07-12 08:56:23" nowrap="nowrap"><span class="">07-12</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">1回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/234446214/" onclick="moreurl(this,{i: '8', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 234446214})" title="天之骄子人才公寓45平一室户 带家电 中介勿扰">天之骄子人才公寓45平一室户 带家电 中介勿扰</a></td>
    <td class="td-time" title="2021-07-10 16:22:24" nowrap="nowrap"><span class="">07-10</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">1回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/234347784/" onclick="moreurl(this,{i: '9', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 234347784})" title="求租 21年10月15号入住">求租 21年10月15号入住</a></td>
    <td class="td-time" title="2021-07-09 21:56:20" nowrap="nowrap"><span class="">07-09</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/234195654/" onclick="moreurl(this,{i: '10', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 234195654})" title="广兰路地铁口步行5分钟 天之骄子人才公寓 复试两房一厅一厨两卫 5200元 电梯房5楼 可租两年">广兰路地铁口步行5分钟 天之骄子人才公寓 复试两房...</a></td>
    <td class="td-time" title="2021-07-08 21:09:09" nowrap="nowrap"><span class="">07-08</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">6回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/234058482/" onclick="moreurl(this,{i: '11', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 234058482})" title="广兰路地铁口步行5分钟 天之骄子人才公寓 整租最小户型 电梯房中间层 3300元 可租到2022.4.20结束">广兰路地铁口步行5分钟 天之骄子人才公寓 整租最小...</a></td>
    <td class="td-time" title="2021-07-07 22:34:12" nowrap="nowrap"><span class="">07-07</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">4回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/234048027/" onclick="moreurl(this,{i: '12', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 234048027})" title="天之骄子复式转租5200可住2年非中介">天之骄子复式转租5200可住2年非中介</a></td>
    <td class="td-time" title="2021-07-07 21:18:05" nowrap="nowrap"><span class="">07-07</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">3回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/233903409/" onclick="moreurl(this,{i: '13', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 233903409})" title="天之骄子一房一厅出租">天之骄子一房一厅出租</a></td>
    <td class="td-time" title="2021-07-06 20:41:42" nowrap="nowrap"><span class="">07-06</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/233394339/" onclick="moreurl(this,{i: '14', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 233394339})" title="广兰路地铁口 天之骄子人才公寓 复试两房一厅一厨两卫其中北次独卫带阳台 2000元 电梯房5楼 一年一签 另一户住一男生">广兰路地铁口 天之骄子人才公寓 复试两房一厅一厨...</a></td>
    <td class="td-time" title="2021-07-03 08:13:50" nowrap="nowrap"><span class="">07-03</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/233228371/" onclick="moreurl(this,{i: '15', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 233228371})" title="求租 求租 天之骄子一室户">求租 求租 天之骄子一室户</a></td>
    <td class="td-time" title="2021-07-01 23:52:36" nowrap="nowrap"><span class="">07-01</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">1回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/233192224/" onclick="moreurl(this,{i: '16', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 233192224})" title="求租天之骄子，有燃气可做饭最好">求租天之骄子，有燃气可做饭最好</a></td>
    <td class="td-time" title="2021-07-01 19:38:56" nowrap="nowrap"><span class="">07-01</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">16回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/233161717/" onclick="moreurl(this,{i: '17', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 233161717})" title="求租 天之骄子公寓一室户">求租 天之骄子公寓一室户</a></td>
    <td class="td-time" title="2021-07-01 15:52:20" nowrap="nowrap"><span class="">07-01</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">2回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/233027248/" onclick="moreurl(this,{i: '18', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 233027248})" title="天之骄子二手闲置  欢迎自提">天之骄子二手闲置  欢迎自提</a></td>
    <td class="td-time" title="2021-06-30 17:05:02" nowrap="nowrap"><span class="">06-30</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">4回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/232785844/" onclick="moreurl(this,{i: '19', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 232785844})" title="求租天之骄子一室户，7月初入住，长租">求租天之骄子一室户，7月初入住，长租</a></td>
    <td class="td-time" title="2021-06-28 22:42:43" nowrap="nowrap"><span class="">06-28</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">1回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/232728283/" onclick="moreurl(this,{i: '20', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 232728283})" title="天之骄子搬家旧物处理，欢迎豆油">天之骄子搬家旧物处理，欢迎豆油</a></td>
    <td class="td-time" title="2021-06-28 15:21:17" nowrap="nowrap"><span class="">06-28</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">3回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/232423135/" onclick="moreurl(this,{i: '21', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 232423135})" title="求天之骄子长租房">求天之骄子长租房</a></td>
    <td class="td-time" title="2021-06-26 13:17:47" nowrap="nowrap"><span class="">06-26</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/231914827/" onclick="moreurl(this,{i: '22', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 231914827})" title="出租|广兰路天之骄子">出租|广兰路天之骄子</a></td>
    <td class="td-time" title="2021-06-23 09:28:21" nowrap="nowrap"><span class="">06-23</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">1回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/231768274/" onclick="moreurl(this,{i: '23', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 231768274})" title="出租|广兰路天之骄子">出租|广兰路天之骄子</a></td>
    <td class="td-time" title="2021-06-22 09:26:53" nowrap="nowrap"><span class="">06-22</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/231665391/" onclick="moreurl(this,{i: '24', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 231665391})" title="出租|广兰路天之骄子">出租|广兰路天之骄子</a></td>
    <td class="td-time" title="2021-06-21 14:03:44" nowrap="nowrap"><span class="">06-21</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/231589264/" onclick="moreurl(this,{i: '25', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 231589264})" title="7月中旬求租 天之骄子">7月中旬求租 天之骄子</a></td>
    <td class="td-time" title="2021-06-20 22:15:12" nowrap="nowrap"><span class="">06-20</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/231319449/" onclick="moreurl(this,{i: '26', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 231319449})" title="【已出】天之骄子人才公寓搬家转卖冰箱洗衣机">【已出】天之骄子人才公寓搬家转卖冰箱洗衣机</a></td>
    <td class="td-time" title="2021-06-19 00:19:02" nowrap="nowrap"><span class="">06-19</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">3回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/231253792/" onclick="moreurl(this,{i: '27', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 231253792})" title="天之骄子人才公寓68平原始一房一厅">天之骄子人才公寓68平原始一房一厅</a></td>
    <td class="td-time" title="2021-06-18 16:52:22" nowrap="nowrap"><span class="">06-18</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">3回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/231179496/" onclick="moreurl(this,{i: '28', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 231179496})" title="广兰路地铁口 天之骄子人才公寓 复试两房一厅一厨一卫 4200元 南北通透 双阳台 短租到2021.8.7或2021.11.7二选一">广兰路地铁口 天之骄子人才公寓 复试两房一厅一厨...</a></td>
    <td class="td-time" title="2021-06-18 08:27:54" nowrap="nowrap"><span class="">06-18</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/230824326/" onclick="moreurl(this,{i: '29', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 230824326})" title="求天之骄子整租，除了最小户型都可以">求天之骄子整租，除了最小户型都可以</a></td>
    <td class="td-time" title="2021-06-15 22:03:16" nowrap="nowrap"><span class="">06-15</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/230799430/" onclick="moreurl(this,{i: '30', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 230799430})" title="求租天之骄子一室一厅">求租天之骄子一室一厅</a></td>
    <td class="td-time" title="2021-06-15 19:29:32" nowrap="nowrap"><span class="">06-15</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/230190702/" onclick="moreurl(this,{i: '31', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 230190702})" title="个人转，天之骄子复式2室2厅1卫 7月起到9月，可周租，月租，月租金4900">个人转，天之骄子复式2室2厅1卫 7月起到9月，可周...</a></td>
    <td class="td-time" title="2021-06-11 13:42:31" nowrap="nowrap"><span class="">06-11</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">1回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/229701877/" onclick="moreurl(this,{i: '32', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 229701877})" title="求租天之骄子">求租天之骄子</a></td>
    <td class="td-time" title="2021-06-08 11:04:13" nowrap="nowrap"><span class="">06-08</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">1回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/229666077/" onclick="moreurl(this,{i: '33', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 229666077})" title="张江人才公寓转租">张江人才公寓转租</a></td>
    <td class="td-time" title="2021-06-08 00:26:30" nowrap="nowrap"><span class="">06-08</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">79回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/229203721/" onclick="moreurl(this,{i: '34', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 229203721})" title="求租天之骄子一室户">求租天之骄子一室户</a></td>
    <td class="td-time" title="2021-06-04 22:45:57" nowrap="nowrap"><span class="">06-04</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">2回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/228527144/" onclick="moreurl(this,{i: '35', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 228527144})" title="求租，天之骄子一室一厅有厨房更好">求租，天之骄子一室一厅有厨房更好</a></td>
    <td class="td-time" title="2021-05-31 16:55:30" nowrap="nowrap"><span class="">05-31</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/227061578/" onclick="moreurl(this,{i: '36', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 227061578})" title="金科路地铁浦软人才公寓一房 | 高科苑两房 | 天之骄子人才公寓两房出租">金科路地铁浦软人才公寓一房 | 高科苑两房 | 天之...</a></td>
    <td class="td-time" title="2021-05-21 16:07:30" nowrap="nowrap"><span class="">05-21</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/226771831/" onclick="moreurl(this,{i: '37', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 226771831})" title="（本周六可看）广兰路地铁站步行5分钟 天之骄子人才公寓 复试两房一厅一厨两卫 电梯房高层 5500元 一年一签">（本周六可看）广兰路地铁站步行5分钟 天之骄子人...</a></td>
    <td class="td-time" title="2021-05-19 17:34:06" nowrap="nowrap"><span class="">05-19</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">8回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/226559519/" onclick="moreurl(this,{i: '38', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 226559519})" title="广兰路天之骄子，求短租，一个月，5/19日起租">广兰路天之骄子，求短租，一个月，5/19日起租</a></td>
    <td class="td-time" title="2021-05-18 10:30:01" nowrap="nowrap"><span class="">05-18</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">4回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/226426369/" onclick="moreurl(this,{i: '39', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 226426369})" title="《限女生》广兰路地铁口步行5分钟 天之骄子人才公寓 整租一房一厅一卫 55平米 电梯房17楼 可租一年两个月 4200元">《限女生》广兰路地铁口步行5分钟 天之骄子人才公...</a></td>
    <td class="td-time" title="2021-05-17 11:31:46" nowrap="nowrap"><span class="">05-17</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">7回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/226323763/" onclick="moreurl(this,{i: '40', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 226323763})" title="求租天之骄子小户型">求租天之骄子小户型</a></td>
    <td class="td-time" title="2021-05-16 16:33:53" nowrap="nowrap"><span class="">05-16</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">1回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/226271990/" onclick="moreurl(this,{i: '41', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 226271990})" title="求租人才公寓">求租人才公寓</a></td>
    <td class="td-time" title="2021-05-16 10:14:00" nowrap="nowrap"><span class="">05-16</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/226145827/" onclick="moreurl(this,{i: '42', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 226145827})" title="天之骄子人才公寓朝南主卧独卫带阳台出租">天之骄子人才公寓朝南主卧独卫带阳台出租</a></td>
    <td class="td-time" title="2021-05-15 12:20:13" nowrap="nowrap"><span class="">05-15</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/225964126/" onclick="moreurl(this,{i: '43', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 225964126})" title="诚意求租，天之骄子小户型，男生单人入住，租一年+，8月入住，中介勿扰，无需租赁备案，无需暂住证明">诚意求租，天之骄子小户型，男生单人入住，租一年+...</a></td>
    <td class="td-time" title="2021-05-14 09:10:13" nowrap="nowrap"><span class="">05-14</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">1回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/225902092/" onclick="moreurl(this,{i: '44', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 225902092})" title="广兰路地铁口步行5分钟 天之骄子人才公寓 整租一房一厅一卫 55平米 朝北 电梯房17楼 可租两年 4280元">广兰路地铁口步行5分钟 天之骄子人才公寓 整租一房...</a></td>
    <td class="td-time" title="2021-05-13 19:21:31" nowrap="nowrap"><span class="">05-13</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/225696404/" onclick="moreurl(this,{i: '45', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 225696404})" title="天之骄子，独立卫生间、朝南主卧独立阳台，短租两个月，1800，有意者私聊，可看房">天之骄子，独立卫生间、朝南主卧独立阳台，短租两...</a></td>
    <td class="td-time" title="2021-05-12 12:53:30" nowrap="nowrap"><span class="">05-12</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">5回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/225382217/" onclick="moreurl(this,{i: '46', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 225382217})" title="天之骄子45平一室户3300元 可住2年 下周可住">天之骄子45平一室户3300元 可住2年 下周可住</a></td>
    <td class="td-time" title="2021-05-10 12:13:36" nowrap="nowrap"><span class="">05-10</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">34回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/225115028/" onclick="moreurl(this,{i: '47', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 225115028})" title="急租天之骄子！">急租天之骄子！</a></td>
    <td class="td-time" title="2021-05-08 18:11:36" nowrap="nowrap"><span class="">05-08</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                        

<tr class="pl">
    <td class="td-subject"><a class="" href="https://www.douban.com/group/topic/224971656/" onclick="moreurl(this,{i: '48', query: '%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90', from: 'group_topic_by_time', sid: 224971656})" title="天之骄子复式朝南单间出租，">天之骄子复式朝南单间出租，</a></td>
    <td class="td-time" title="2021-05-07 21:08:41" nowrap="nowrap"><span class="">05-07</span></td>
    <td class="td-reply" nowrap="nowrap"><span class="">0回应</span></td>
</tr>

                    </tbody>
                </table>
            </div>
    
    
    

    
        <div class="paginator">
        <span class="prev">
            &lt;前页
        </span>
        
        

                <span class="thispage" data-total-page="7">1</span>
                
            <a href="https://www.douban.com/group/search?start=50&amp;cat=1013&amp;group=634832&amp;sort=time&amp;q=%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90" >2</a>
        
                
            <a href="https://www.douban.com/group/search?start=100&amp;cat=1013&amp;group=634832&amp;sort=time&amp;q=%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90" >3</a>
        
                
            <a href="https://www.douban.com/group/search?start=150&amp;cat=1013&amp;group=634832&amp;sort=time&amp;q=%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90" >4</a>
        
                
            <a href="https://www.douban.com/group/search?start=200&amp;cat=1013&amp;group=634832&amp;sort=time&amp;q=%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90" >5</a>
        
                
            <a href="https://www.douban.com/group/search?start=250&amp;cat=1013&amp;group=634832&amp;sort=time&amp;q=%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90" >6</a>
        
                
            <a href="https://www.douban.com/group/search?start=300&amp;cat=1013&amp;group=634832&amp;sort=time&amp;q=%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90" >7</a>
        
        <span class="next">
            <link rel="next" href="https://www.douban.com/group/search?start=50&amp;cat=1013&amp;group=634832&amp;sort=time&amp;q=%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90"/>
            <a href="https://www.douban.com/group/search?start=50&amp;cat=1013&amp;group=634832&amp;sort=time&amp;q=%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90" >后页&gt;</a>
        </span>

            <span class="count">(共307个结果)</span>
        </div>



        </div>
        <div class="aside">
                
<!-- douban ad begin -->
<div id="dale_group_search_top_right"></div>
<!-- douban ad end -->


  <div class="search_report">
    <a href="javascript:;" id="search-report-btn">&gt; 对结果不满意？让我们知道</a>
  </div>
  <iframe frameborder="0" id="feedback-iframe"></iframe>
  
  <script type="text/javascript">
    Do(function () {
      $('#search-report-btn').click(function () {
        var url = 'https://help.douban.com/feedback_popup?qtype=197&tags=%E5%B0%8F%E7%BB%84&extra=' +
          encodeURIComponent(JSON.stringify({
              q: '天之骄子',
              cat_id: '1013'
            }))
        var $iframe = $('#feedback-iframe')
        if ($iframe.attr('src') !== url) {
          $iframe.attr('src', url)
        }
        $('#feedback-iframe').show()
      })
      window.addEventListener('message', function (event) {
        var origin = event.origin || event.originalEvent.origin;
        if (!origin.match(/^https?:\/\/[a-z0-9-.]+\.douban\.com(?:\/|:|$)/)) {
          // 非法域名
          window.console && console.warn && console.warn('window receive message from illegal origin: ', origin, event)
          return
        }
        if (typeof event.data !== 'string') {
          return
        }
        var data = JSON.parse(event.data)
        if (data.type === 'FEEDBACK_POPUP_CLOSE') {
          $('#feedback-iframe').hide()
        }
      })
    });
  </script>


<div class="side-nav">
<a href="https://www.douban.com/group/634832/">&gt; 回天之骄子小组</a>
</div>

        </div>
        <div class="extra">
            
        </div>
    </div>
</div>

        
<div id="footer">
    
<span id="icp" class="fleft gray-link">
    &copy; 2005－2021 douban.com, all rights reserved 北京豆网科技有限公司
</span>

<a href="https://www.douban.com/hnypt/variformcyst.py" style="display: none;"></a>

<span class="fright">
    <a href="https://www.douban.com/about">关于豆瓣</a>
    · <a href="https://www.douban.com/jobs">在豆瓣工作</a>
    · <a href="https://www.douban.com/about?topic=contactus">联系我们</a>
    · <a href="https://www.douban.com/about/legal">法律声明</a>
    
    · <a href="https://help.douban.com/group" target="_blank">帮助中心</a>
    · <a href="https://www.douban.com/doubanapp/">移动应用</a>
    · <a href="https://www.douban.com/partner/">豆瓣广告</a>
</span>

</div>

    </div>
    

    <script type="text/javascript">

;(function() {
  var mask;
  var popup;
  var current = '';
  var init_popup = function() {
    mask = $('<div class="popup-reg-mask"></div>').appendTo('body');
    mask.css('height', $(document).height());
    popup = $('#g-popup-reg');
    popup.find('.lnk-close').click(function(e) {
        e.preventDefault();
        popup.hide();
        mask.hide();
    });

    if ($.browser.msie && ($.browser.version|0) === 6) {
        var win = $(window).scroll((function() {
            var timer;
            var doc = document.body;
            return function() {
                if (timer) {
                    window.clearTimeout(timer);
                }
                timer = window.setTimeout(function() {
                    popup.css({
                      top: (doc.scrollTop + win.height()/2 - popup.height()/2) + 'px'
                    });
                }, 20);
            };
        })()).trigger('scroll');
    }
  };

  var show_popup = function() {
    if (popup) {
      popup.show();
      mask.show();
    } else {
      $('#g-popup-reg').show();
      init_popup();
    }
  };

  Douban.init_show_register = function (e) {
    var node = $(e);
    node.click(function(e) {
      e.preventDefault();
      show_popup();
      if (current !== 'register') {
        popup.find('iframe').attr('src', reg_url);
      }
      current = 'register';
    });
  };

  Douban.init_show_login = function (e) {
    var node = $(e);
    node.click(function(e) {
      e.preventDefault();
      show_popup();
      if (current !== 'login') {
        popup.find('iframe').attr('src', login_url);
      }
      current = 'login';
    });
  };
})();

$(function() {
  var $landingBar = $('#landing-bar');
  var popup_mark = 'g_reg';
  // 有些页面会自动弹注册框
  if (
  'selenium_main_app_window' === window.name ||
  window.POPUP_REG && !window.name) {
      $('#landing-bar').show();
      $('#wrapper').addClass('landing');
  }
  $landingBar.delegate('a', 'click', function(e) {
      // 第三方登录不处理，其他隐藏landing bar
      if ($(this).parent().is('.item')) {
          return;
      }

      e.preventDefault();
      $landingBar.hide();
      if (window.POPUP_REG) {
        window.name = window.name || popup_mark;
      }
  });
});
</script>
    
<!-- douban ad begin -->





    
<script type="text/javascript">
    (function (global) {
        var newNode = global.document.createElement('script'),
            existingNode = global.document.getElementsByTagName('script')[0],
            adSource = '//erebor.douban.com/',
            userId = '',
            browserId = 'ieXvd44nPZ4',
            criteria = '3:/group/search?group=634832&amp;q=%E5%A4%A9%E4%B9%8B%E9%AA%84%E5%AD%90&amp;cat=1013&amp;sort=time',
            preview = '',
            debug = false,
            adSlots = ['dale_group_search_top_right'];

        global.DoubanAdRequest = {src: adSource, uid: userId, bid: browserId, crtr: criteria, prv: preview, debug: debug};
        global.DoubanAdSlots = (global.DoubanAdSlots || []).concat(adSlots);

        newNode.setAttribute('type', 'text/javascript');
        newNode.setAttribute('src', '//img1.doubanio.com/YWVrMm1iYy9mL2FkanMvN2ZmNmEyM2M0ZDNjMmQxYWVkMjMwZDIwMDU5NWI2YTFkNDc5YjExYi9hZC5yZWxlYXNlLmpz');
        newNode.setAttribute('async', true);
        existingNode.parentNode.insertBefore(newNode, existingNode);
    })(this);
</script>










<!-- douban ad end -->

    
    









<!-- Google Tag Manager -->
<noscript><iframe src="//www.googletagmanager.com/ns.html?id=GTM-5WP579" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='//www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-5WP579');</script>
<!-- End Google Tag Manager -->


<script type="text/javascript">
var _paq = _paq || [];
_paq.push(['trackPageView']);
_paq.push(['enableLinkTracking']);
(function() {
    var p=(('https:' == document.location.protocol) ? 'https' : 'http'), u=p+'://fundin.douban.com/';
    _paq.push(['setTrackerUrl', u+'piwik']);
    _paq.push(['setSiteId', '100001']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.type='text/javascript';
    g.defer=true;
    g.async=true;
    g.src=p+'://img3.doubanio.com/dae/fundin/piwik.js';
    s.parentNode.insertBefore(g,s);
})();
</script>

<script type="text/javascript">
var _gaq = _gaq || [];
_gaq.push(['_setAccount', 'UA-7019765-1']);
_gaq.push(['_setCampNameKey', 'dcn']);
_gaq.push(['_setCampSourceKey', 'dcs']);
_gaq.push(['_setCampMediumKey', 'dcm']);
_gaq.push(['_setCampTermKey', 'dct']);
_gaq.push(['_setCampContentKey', 'dcc']);
_gaq.push(['_addOrganic', 'baidu', 'word']);
_gaq.push(['_addOrganic', 'soso', 'w']);
_gaq.push(['_addOrganic', '3721', 'name']);
_gaq.push(['_addOrganic', 'youdao', 'q']);
_gaq.push(['_addOrganic', 'so.360.cn', 'q']);
_gaq.push(['_addOrganic', 'vnet', 'kw']);
_gaq.push(['_addOrganic', 'sogou', 'query']);
_gaq.push(['_addIgnoredOrganic', '豆瓣']);
_gaq.push(['_addIgnoredOrganic', 'douban']);
_gaq.push(['_addIgnoredOrganic', '豆瓣网']);
_gaq.push(['_addIgnoredOrganic', 'www.douban.com']);
_gaq.push(['_setDomainName', '.douban.com']);


    _gaq.push(['_setCustomVar', 1, 'responsive_view_mode', 'desktop', 3]);

_gaq.push(['_trackPageview']);
_gaq.push(['_trackPageLoadTime']);

window._ga_init = function() {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
};
if (window.addEventListener) {
    window.addEventListener('load', _ga_init, false);
} else {
    window.attachEvent('onload', _ga_init);
}
</script>





    <!-- dae-web-group--default-bb9fbf9dd-wx4x6-->

            





<style>
  @font-face{font-family:"groupicons";src:url(https://img3.doubanio.com/f/group/538e8d0d55ffbf1f775c7c9519c42db2cab4b430/pics/group/fonts/groupicons.eot);src:url(https://img3.doubanio.com/f/group/538e8d0d55ffbf1f775c7c9519c42db2cab4b430/pics/group/fonts/groupicons.eot) format("embedded-opentype"),url(https://img3.doubanio.com/f/group/a66eeba150d7ec8b5eace9c414a1f485b4339151/pics/group/fonts/groupicons.woff) format("woff"),url(https://img3.doubanio.com/f/group/c61ea0a5cc2e9161108f940debbe7b87292a1d02/pics/group/fonts/groupicons.ttf) format("truetype"),url(https://img3.doubanio.com/f/group/0f0f6589afa6948c5f89cc9c611cc7aec2d7498a/pics/group/fonts/groupicons.svg) format("svg");font-weight:normal;font-style:normal}

</style>



<div id="g-popup-reg" class="popup-reg" style="display:none;">
  <div class="bd">
  
  <iframe src="about:blank" frameborder="0" scrolling="no"></iframe>
    <a href="#" class="lnk-close">&times;</a>
  </div>
</div>

<div id="landing-bar" style="display:none;">
    <div class="bd">
        <p>在这里发现跟你一样特别的人，并与之交流...</p>
        <div class="operation">
            <a href="" class="j a_show_register">注册</a>
            <a href="" class="j a_show_login">登录</a>
        </div>
        
        
  
  <div class="item item-3rd">
    <label>
    第三方登录：
    </label>
    <a target="_top" href="https://www.douban.com/accounts/connect/qq/?from=group&amp;redir=http%3A//www.douban.com/accounts/join_and_redir%3Fgroup_id%3D634832" class="item-qq"><img src="https://img3.doubanio.com/pics/connect_qq.png" title="QQ"></a>
    <a target="_top" href="https://www.douban.com/accounts/connect/sina_weibo/?from=group&amp;redir=http%3A//www.douban.com/accounts/join_and_redir%3Fgroup_id%3D634832&amp;fallback=https://www.douban.com/group/634832/" class="item-weibo"><img src="https://img3.doubanio.com/pics/connect_sina_weibo.png" title="新浪微博"></a>
  </div>

        <a href="#" class="lnk-close">&times;</a>
    </div>
</div>


<script>

var login_url = 'https://accounts.douban.com/popup/login?source=group';
var reg_url = 'https://accounts.douban.com/popup/login?source=group#popup_register';
</script>








  <script>_SPLITTEST=''</script>
</body>

</html>


'''

root = etree.HTML(html)
# xpath = '//table[@class="olt"]//tr[@class="pl"]'
# link_nodes = root.xpath(xpath)
# for node in link_nodes:
#     subject = node.xpath('//td[@class="td-subject"]')
#     time = node.xpath('//td[@class="td-time"]')
#     reply = node.xpath('//td[@class="td-reply"]')
#     print(subject[0].get('href'))



xpath = '//table[@class="olt"]//a[@title]'
linkNodes = root.xpath(xpath)
xpathTime = '//table[@class="olt"]//td[@class="td-time"]'
linkNodesTime = root.xpath(xpathTime)
for i in range(len(linkNodes)):
    print(linkNodes[i].get('href'))
    print(linkNodes[i].get('title'))
    print(linkNodesTime[i].get('title'))


time_stamp_1 = time.mktime(time.strptime('2021-07-08 21:09:09', '%Y-%m-%d %H:%M:%S'))
time_stamp_2 = time.mktime(time.strptime('2021-06-01 00:00:00', '%Y-%m-%d %H:%M:%S'))
time_stamp_3 = time.mktime(time.strptime('2022-06-01 00:00:00', '%Y-%m-%d %H:%M:%S'))

if int(time_stamp_1) > int(time_stamp_2):
    print('time_stamp_1')
else:
    print('time_stamp_2')

if int(time_stamp_1) > int(time_stamp_3):
    print('time_stamp_1')
else:
    print('time_stamp_3')
