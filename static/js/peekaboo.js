var main = function(){
$('html').removeClass('js');
$('.triangle-down').hide();
$('.title').each(function(){
	$(this).click(function (){
		event.preventDefault();
		var href= $(this).attr('href');
		$(this).find(".triangle-up").toggle();
		$(this).find('.triangle-down').toggle();
		$('.nugget_title').not(this).hide(500);
		$('.content-box').load(this.href + '*', function(){
			$('.content-box').fadeIn(100);

		});
      return false;
	});
	});
$('#register').one('click', function (){
		event.preventDefault();
		var href= $(this).attr('href');
		$('.content-box').load(this.href, function (){
			$('.content-box').fadeIn(100);
		});
		$(this).removeAttr('href');
	return false;
});
}

$(document).ready(main);