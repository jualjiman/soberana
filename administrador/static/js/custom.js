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
	  //var pag = parseInt($("#num-pag").val());

	  var $gallery = $("#loadmore-container");
	  console.log($gallery);
	  alert("ya");
	  // $.ajax({
	  //    type: "POST",
	  //    url: '/mas/',
	  //    data: {
	  //       num: pag
	  //    },
	  //    success: function (data) {
	  //       $("#num-pag").val(pag + 1);
	  //       // Get elements from request
	  //       var $elems = $('<div>'+data+'</div>').find('.gl-item');
	  //       // append elements to container
	  //       $gallery.append( $elems );
	  //          // add and lay out newly appended elements
	  //          refresh_items_order_data();
	  //       $gallery.isotope( 'appended', $elems );
	           
	  //       process_images_load();
	        
	  //    },
	  //    complete: function () {
	  //       $spinner.hide();
	  //    },
	  //    error: function (jqXHR, textStatus) {
	  //       console.log(textStatus);
	  //    }
	  // });

	});
});