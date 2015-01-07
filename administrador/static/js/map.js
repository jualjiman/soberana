$(function(){
	initialize();
});

//contact map
function initialize() {
	var ubicacion = new google.maps.LatLng(16.859502, -99.811303);
	var mapOptions = {
	  	center: ubicacion,
	  	zoom: 13,
	  	mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	var map = new google.maps.Map($("#map-content")[0], mapOptions);
}