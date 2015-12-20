var main = function(){
$('html').removeClass('js');
$('.more').hide();
$('#title').hide();
$('#title-exp').hide();
$('#title-exp2').hide();
$('#line').hide();
$('.entries').hide();
$('.video-hed').hide();
$('.excerpt').hide();
$('#hed-exp').hide();
$('#hed-exp2').hide();
$('#excerpt-exp').hide();
$('#excerpt-exp2').hide();
$('#excerpt-exp3').hide();
$('#excerpt-exp4').hide();
$('#more-exp').hide();
$('#more-exp2').hide();
$('#choices').hide();
$('#yes').hide();
$('#no').hide();
$('.triangle-down').hide();

$('#title').fadeIn(600);
$('#line').fadeIn(800);

$('#title-exp').delay(800).fadeIn(800);

$('#ok1').click(function(){
	$('#title-exp').hide();
	$('#title-exp2').fadeIn(600);
	$('#title').click(function(){
		$('.triangle-up').toggle();
		$('.triangle-down').toggle();
		$('.entries').fadeToggle(600);
		$('.video-hed').fadeToggle(600);
		$('.excerpt').toggle(600);
		$('#title-exp2').hide();
		$('#hed-exp').fadeIn(800);
	});
});

$('#ok2').click(function(){
	$('#hed-exp').hide();
	$('#hed-exp2').fadeIn(600);
});

$('#ok3').click(function(){
	$(this).hide();
	$('#hed-exp5').hide();
	$('#excerpt-exp').fadeIn(600);
	$('#excerpt-exp2').delay(1000).fadeIn(600);
	$('#excerpt-exp3').delay(1800).fadeIn(600);
	$('#excerpt-exp4').delay(3000).fadeIn(600, function(){
		$('.excerpt').click(function(){
		$(this).next().toggle(300);
		$('#more-exp').fadeIn(800);
		$('#more-exp2').delay(2500).fadeIn(800);
		$('#choices').delay(5000).fadeIn(800);
		});
	});
});


$('#choice1').click(function(){
	$('#choices').hide();
	$('#yes').show(300);
});
$('#choice2').click(function(){
	$('#choices').hide();
	$('#no').show(300);
});
}

$(document).ready(main);