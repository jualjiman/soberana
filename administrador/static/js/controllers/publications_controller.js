angular
	.module(
		'publicaciones',
		[]
	)
	.controller('publicaciones_controller', ['$scope','$http', function($scope, $http){

		$scope.search = '';
		$http.get('/api/publicaciones/')
		.success(function(data, status, headers, config) {
			$scope.publicaciones = data;
		})
		.error(function(data, status, headers, config) {
			console.log("Error al recuperar datos");
		});
	}]);