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

	// Load more
	$('#btn-loadmore').click(function(e) {
	  e.preventDefault();
	  //var $this = $(this).hide();
	  //var $spinner = $(this).siblings('.loading-spinner').show();
	  var $counter = $("#num-pag");
	  var $gallery = $("#loadmore-container");
	  
	  var pag = parseInt($counter.val());
	  $.ajax({
	     type: "POST",
	     url: '/mas/',
	     data: {
	        num: pag
	     },
	     success: function (data) {
	        $counter.val(pag + 1);

	        // Get elements from request
	        var $elems = $(data);
	        $gallery.append( $elems.hide().fadeIn(800) );	        
	     },
	     error: function (jqXHR, textStatus) {
	        console.log(textStatus);
	     }
	  });

	});
});
