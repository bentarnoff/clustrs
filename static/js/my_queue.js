var main = function(){
$('html').removeClass('js');
$('#myclustrs_title').find('.triangle-up').hide();
$('#contribute_title').find('.triangle-down').hide();
$('#find_title').find('.triangle-down').hide();
$('#find_title').find('.list').hide();
$('#contribute_title').find('.list').hide();
$('.title').each(function(){
	$(this).click(function (){
		$(this).find(".triangle-up").toggle();
		$(this).find('.triangle-down').toggle();
		$(this).siblings('.list').fadeToggle(500);
		});
	});
}

$(document).ready(main);