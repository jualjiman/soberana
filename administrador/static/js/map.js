//contact map
function initialize() {
	var ubicacion = new google.maps.LatLng(16.859502, -99.811303);
	var mapOptions = {
	  	center: ubicacion,
	  	zoom: 13,
	  	mapTypeId: google.maps.MapTypeId.ROADMAP
	};
	var map = new google.maps.Map($("#map-content")[0], mapOptions);
	var marker = new google.maps.Marker({
			//Coordinate of the marker's location
			position: new google.maps.LatLng(16.859502, -99.811303),
			map: map,
			//Text that will be displayed when the mouse hover on the marker
			title:"Instituto Tecnológico de Acapulco"
		});
}