var scripts = {};

scripts.boxAutoHeight = function(){
	$selector = $(".boxAutoHeight");
	$selector.height("initial").height( $selector.height() );
}


$( window ).resize(function() {
	scripts.boxAutoHeight();
	scripts.sliderOnResize();
});

$(function(){
	scripts.boxAutoHeight();
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
	        $gallery.append( $elems.hide().fadeIn(500) );	        
	     },
	     error: function (jqXHR, textStatus) {
	        console.log(textStatus);
	     }
	  });

	});

	initialize();
});
