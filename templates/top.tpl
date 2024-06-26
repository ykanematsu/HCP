  <div id="top">
    <header class="fadeintop">
      <div class="bigf">
        <a href='{{url_for("index")}}'<p style="text-shadow:2px 2px 5px #333;">Hiroshima Chemical Predictor</p></a>
      </div>
      <div class="clearfix"></div>
      <div id="carousel" class="carousel slide carousel-fade " data-bs-ride="carousel" data-bs-interval="10000">
        <div class="carousel-indicators">
            <button data-bs-target="#carousel" data-bs-slide-to="0" class="active"></button>
            <button data-bs-target="#carousel" data-bs-slide-to="1" ></button>
            <button data-bs-target="#carousel" data-bs-slide-to="2" ></button>
        </div>
        <div class="carousel-inner">
          <div id="pic0" class="carousel-item active">
            <img srcset="/static/img/top.jpg 1280w, /static/img/top_s.jpg 767w" src="/static/img/top.jpg" decoding="auto">
            <div class="carousel-caption d-none d-md-block">
              <p>三段峡 <a title="詳細" target="_blank" href="http://www.akioota-navi.jp/html/kankou_mobi_sandankyo_access.html"><i class="bi bi-info-circle-fill"></i></a></p>
            </div>
          </div>
          <div id="pic2" class="carousel-item">
            <img srcset="/static/img/top11.jpg 1280w, /static/img/top11_s.jpg 767w" src="/static/img/top11.jpg" decoding=async>
            <div class="carousel-caption d-none d-md-block">
              <p>原爆ドーム <a title="詳細" target="_blank" href="http://www.city.hiroshima.lg.jp/www/dome/contents/1005000000027/index.html"><i class="bi bi-info-circle-fill"></i></a></p>
            </div>
          </div>
          <div id="pic3" class="carousel-item">
            <img srcset="/static/img/top10.jpg 1280w, /static/img/top10_s.jpg 767w" src="/static/img/top10.jpg" decoding="async">
            <div class="carousel-caption d-none d-md-block">
              <p>縮景園 <a title="詳細" target="_blank" href="https://shukkeien.jp/access/"><i class="bi bi-info-circle-fill"></i></a></p>
            </div>
          </div>
        </div>
      </div>
    </header>
  </div>
      <nav id="nav" class="navbar sticky-top navbar-expand-md navbar-dark bg-dark px-3 mb-3">
        <div class="container-fluid">
           <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
              <span class="navbar-toggler-icon"></span>
           </button>
          <div id="navbarNav" class="navbar-collapse collapse justify-content-center">
            <ul class="nav nav-pills">
              <li><a class="nav-link d-none d-md-block" title="ページトップへ" href="#top"><i class="bi bi-house-fill"></i></a></li>
              <li><a class="nav-link" href="#psq">分離膜</a></li>
              <li><a class="nav-link" href="#qy">量子収率</a></li>
              <li><a class="nav-link" href="#link">リンク</a></li>
            </ul>
          </div>
        </div>
      </nav>

