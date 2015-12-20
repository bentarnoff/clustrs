var main = function(){
$('html').removeClass('js');
$('.title').hide();
$('.line').hide();
$('.entries').hide();
$('.title').fadeIn(500);
$('.line').fadeIn(500);
$('.entries').delay(500).fadeIn(500);

$('#sign_up').find('.triangle-up').hide();
$('#login').find('.triangle-up').hide();

//$('#login_box').load('/dashboard/login .content-box *')

$('#sign_up').click(function(){
	$(this).find(".triangle-up").toggle();
	$(this).find('.triangle-down').toggle();
	$('#sign_up_box_hed').fadeToggle(200);
	$('#sign_up_box').fadeToggle(200);
});

$('#login').click(function(){
	$(this).find(".triangle-up").toggle();
	$(this).find('.triangle-down').toggle();
	$('#login_box_hed').fadeToggle(200);
	$('#login_box').fadeToggle(200);
});



}
$(document).ready(main);