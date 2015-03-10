angular
	.module(
		'eventos',
		[]
	)
	.config(function ($interpolateProvider) {
		$interpolateProvider.startSymbol('{[{');
		$interpolateProvider.endSymbol('}]}');

	})
	.controller('eventos_controller', ['$scope','$http', function($scope, $http){

		$scope.search = '';
		$http.get('/eventos-json/').
		success(function(data, status, headers, config) {
			$scope.eventos = data;
		}).
		error(function(data, status, headers, config) {

		});
	}]);

// mail checar recuperacion de contraseña con envio de mail

