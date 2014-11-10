var scripts = {};

scripts.sliderOnResize = function (){
	if($(window).width() > 1500){
		$("#slider").addClass("container");
	}else{
		$("#slider").removeClass("container");
	}
};

$( window ).resize(function() {
	scripts.sliderOnResize();
});

$(function(){
	scripts.sliderOnResize();
});