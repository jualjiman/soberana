angular
	.module(
		'eventos',
		[]
	)
	.controller('eventos_controller', ['$scope','$http', function($scope, $http){

		$scope.search = '';
		$http.get('/api/eventos/')
		.success(function(data, status, headers, config) {
			$scope.eventos = data;
		})
		.error(function(data, status, headers, config) {
			console.log("Error al recuperar datos");
		});
	}]);