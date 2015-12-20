var main = function(){
$('html').removeClass('js');
$('.more').hide();
$('.nugget').hide();
$('.triangle-up').hide();
$('.title').hide();
$('.line').hide();
$('.title').fadeIn(500);
$('.line').fadeIn(500);
var i = 500
$('.nugget').each(function(){
	$(this).delay(i).fadeIn(500)
	i = i + 500
});



$('.title').click(function(){
    var href = "/start/";
    $('.triangle-up').toggle();
	$('.triangle-down').toggle();
	$('.nugget').hide(500);
	$('.nugget_title').not(this).hide();
	$('body').fadeOut(500, function(){
			window.location=href;
		});

   return false;
});

$('.excerpt').click(function(){
	$(this).next().toggle(300);
});


}

$(document).ready(main);