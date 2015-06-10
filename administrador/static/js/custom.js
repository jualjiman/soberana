var scripts = {};

scripts.boxAutoHeight = function(){
	$selector = $(".boxAutoHeight");
	$selector.height("initial").height( $selector.height() );
}

scripts.hideContactHintInfo = function(){
	$('.alert-info').hide();
	$('.alert-danger').hide();
	$('.alert-warning').hide();
}

scripts.clearContactForm = function(){
	$('#id_nombre').val("");
    $('#id_email').val("");
    $('#id_mensaje').val("");
}


$( window ).resize(function() {
	scripts.boxAutoHeight();
});

$(function(){
	scripts.boxAutoHeight();
	scripts.hideContactHintInfo()

	// Load more
	$('#btn-loadmore').click(function(e) {
	  e.preventDefault();
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

	$("#btnSend").click(function(e){
        e.preventDefault();
        scripts.hideContactHintInfo();

        var name = $('#id_nombre').val();
        var email = $('#id_email').val();
        var message = $('#id_mensaje').val();
        var email_regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;

        if( name !== "" && email !== "" && message !== ""){
            if( email_regex.test(email) === true ){
                $.ajax({
                    type: "POST",
                    url: "/nuestro-instituto/ubicacion-contacto/",  // or just url: "/my-url/path/"
                    data: {
                        csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),
                        name: name,
                        email: email,
                        message: message
                    },
                    success: function(data) {
						scripts.clearContactForm();
                        $('.alert-info').text('Mensaje enviado, Muchas gracias!').hide().fadeIn();
                    },
                    error: function(xhr, textStatus, errorThrown) {
                        $('.alert-danger').text("Algo fallo!, por favor intente más tarde").hide().fadeIn();
                    }
                });
            }
            else{
                $('.alert-warning').text('El formato de email que ingreso es invalido').hide().fadeIn();
            }

        }
        else{
            $('.alert-warning').text('Todos los campos son requeridos').hide().fadeIn();
        }
    });

	initialize();
});
