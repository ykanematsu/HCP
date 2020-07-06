  <div id="top">
    <header class="fadeintop">
      <div class="bigf">
        <a href='{{url_for("index")}}'<p style="text-shadow:2px 2px 5px #333;">Hiroshima Chemical Predictor</p></a>
      </div>
      <div class="clearfix"></div>
      <section class="box">
       <div class="kakomi-smart2">
           <a href="#psq"><span class="glyphicon glyphicon-share-alt"></span> 分離膜</a><br>
           <a href="#qy"><span class="glyphicon glyphicon-share-alt"></span> 量子収率</a>
         <br>
       </div>
      </section>
      <div id="carousel" class="carousel slide" data-ride="carousel" data-interval="12000">
        <ol class="carousel-indicators">
            <li data-target="#carousel" data-slide-to="0" class="active"></li>
            <li data-target="#carousel" data-slide-to="1" ></li>
            <li data-target="#carousel" data-slide-to="2" ></li>
        </ol>
        <div class="carousel-inner">
          <div id="pic0" class="item active">
            <img srcset="/static/img/top.jpg 1280w, /static/img/top_s.jpg 767w" src="/static/img/top.jpg" decoding="auto">
            <div class="carousel-caption">
              <p>三段峡 <a title="詳細" target="_blank" href="http://www.akioota-navi.jp/html/kankou_mobi_sandankyo_access.html"><span class="glyphicon glyphicon-info-sign"></span></a></p>
            </div>
          </div>
          <div id="pic2" class="item">
            <img srcset="/static/img/top11.jpg 1280w, /static/img/top11_s.jpg 767w" src="/static/img/top11.jpg" decoding=async>
            <div class="carousel-caption">
              <p>原爆ドーム <a title="詳細" target="_blank" href="http://www.city.hiroshima.lg.jp/www/dome/contents/1005000000027/index.html"><span class="glyphicon glyphicon-info-sign"></span></a></p>
            </div>
          </div>
          <div id="pic3" class="item">
            <img srcset="/static/img/top10.jpg 1280w, /static/img/top10_s.jpg 767w" src="/static/img/top10.jpg" decoding="async">
            <div style="z-index:6" class="carousel-caption">
              <p>縮景園 <a title="詳細" target="_blank" href="https://shukkeien.jp/access/"><span class="glyphicon glyphicon-info-sign"></span></a></p>
            </div>
          </div>
        </div>
      </div>
    </header>
    <div class="nav-dummy">
      <nav class="container-fluid navbar navbar-inverse">
        <div class="row">
          <div class="nav navbar-header">
            <button type="button" class="navbar-toggle collapsed pull-left" aria-expanded="false">
              <a title="ページトップへ" href="#"><span class="glyphicon glyphicon-home"></span></a>
            </button>
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
              <span class="icon-bar"></span>
            </button>
          </div>
          <div id="navbar" class="navbar-collapse collapse">
            <ul class="nav nav-pills navbar-nav">
              <li class="hidden-xs"><a title="ページトップへ" href="#top"><span class="glyphicon glyphicon-home"></span></a></li>
              <li><a href="#psq">分離膜</a></li>
              <li><a href="#qy">量子収率</a></li>
              <li><a href="#link">リンク</a></li>
{#
              <li class="dropdown">
                  <a data-toggle="dropdown" href="#link">参加・発表登録</a>
                  <ul class="dropdown-menu" role="menu">
		    <li role="presentation"><a role="menuitem" tabindex="-1" href="#s4-1" class="drop">発表申込</a></li>
		    <li role="presentation"><a role="menuitem" tabindex="-1" href="#s4-2" class="drop">参加登録</a></li>
		    <li role="presentation"><a role="menuitem" tabindex="-1" href="#s4-3" class="drop">要旨投稿</a></li>
		    <li role="presentation"><a role="menuitem" tabindex="-1" href="#s4-4" class="drop">スライド投稿</a></li>
	          </ul>
              </li>
#}
            </ul>
          </div>
        </div>
      </nav>
    </div>
  </div>
