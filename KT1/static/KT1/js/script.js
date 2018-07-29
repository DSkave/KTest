/* ===================================================================

 * PC向けメニュー

=================================================================== */
$(function($) {
	// 読み込み時処理
	navFix();
	// スクロール時処理
	$(window).on('scroll', function() {
		navFix();
	});

	// ナビゲーション固定
	function navFix() {
		var headerH = $('header').outerHeight(true);
		if ($(this).scrollTop() > headerH) {
			$('nav').addClass('fixed');
		} else {
			$('nav').removeClass('fixed');
		}
	}
});


/* ===================================================================

 * PC/スマホ向けメニュー切り替え

=================================================================== */
$(function($){
	var timer = false;
	var windowWidth = window.innerWidth || document.documentElement.clientWidth || 0;
	var nowWidth;

	// 読み込み時処理
	$(window).on('load', function(){
		headerHight();
		spMenu();
		subNav();
		summay();
	});

	// リサイズ時処理
	$(window).on('resize', function(){
		if (timer !== false) {
			clearTimeout(timer);
		}
		timer = setTimeout(function() {
			nowWidth = window.innerWidth || document.documentElement.clientWidth || 0;
			if ( windowWidth != nowWidth ) {
				headerHight();
				subNav();
				summay();
				windowWidth = window.innerWidth || document.documentElement.clientWidth || 0;
			}
		}, 200);
	});

	// ヘッダー分の余白取得（スマートフォンのみ）
	function headerHight() {
		if ($('#spMenu').css('display') == 'block') {
			var headerH = $('header').outerHeight(true);
			$('body').css({'margin-top' : headerH});
		}else {
			$('body').css({'margin-top' : 0});
		}
	}

	// メニューボタンの表示（
	function spMenu() {
		$('#spMenu').on('click', function(e) {
			$('.gnav').slideToggle(e);
			$('#navBtnIcon').toggleClass('close');
			$('html, body').toggleClass('lock');
		});
	}

	// サブメニューの表示
	function subNav() {
		if ($('#spMenu').css('display') == 'block') {
			$('.subnav > a').off().on('click', function(e) {
				e.preventDefault();
				$(this).next('ul').slideToggle();
				$(this).parent().toggleClass('active');
			});
		} else {
			if('ontouchstart' in document) {
				$('.subnav > a').off().on('click', function(e) {
					e.preventDefault();
				});
			}
		}
	}

	// 要約部分の非表示
	function summay() {
		if ($('#spMenu').css('display') == 'block') {
			var position = 50; // 非表示位置
			var $element = $('.summary');
			if ($(window).scrollTop() > position){
				$element.hide();
			}
			$(window).on('scroll', function(){
				if ($(this).scrollTop() >= position) {
					$element.not(':animated').hide();
				} else {
					$element.not(':animated').show();
				}
				headerHight();
			});
		}
	}
});

/* ===================================================================

 * ページ内リンク

=================================================================== */
$(function($){
	var timer = false;
	$(window).on('load', function(){
		if (timer !== false) {
			clearTimeout(timer);
		}
		timer = setTimeout(function() {
			innerLink();
			innerLinkMenu();
		}, 300);
	});

	function innerLink() {
		var easing = 'swing'; // 動作パターン
		var speed = 500;      // スクロールの速度
		var marginTop = 10;   // スクロール位置の変更

		var url = $(location).attr('href');
		if(url.indexOf('?id=') != -1){
			var id = url.split('?id=');
			var target = $('#' + id[id.length - 1]);
			if(target.length){
				// スマートフォン向け内部リンク
				if($('#spMenu').css('display') == 'block') {
					var fixEle = $('header');
					var fixHeight = fixEle.outerHeight(true);
					if($('.summary').css('display') == 'block') {
						var position = target.offset().top- fixHeight -marginTop;
					}
				// PC向け内部リンク
				} else {
					var fixEle = $('nav');
					var fixHeight = fixEle.outerHeight(true);
					if($('nav').css('position') == 'fixed') {
						var position = target.offset().top - fixHeight - marginTop;
					} else {
						var position = target.offset().top - fixHeight - fixHeight - marginTop;
					}
				}
				$('html, body').animate({scrollTop:position}, speed, easing);
			}
		}
	}

	function innerLinkMenu() {
		// メニューの表示・非表示
		$('.gnav a[href^="#"]').on('click', function(e) {
			if($('#spMenu').css('display') == 'block') {
				$('.gnav').slideToggle(e);
				$('#navBtnIcon').toggleClass('close');
				$('html, body').toggleClass('lock');
			}
		});
	}
});
