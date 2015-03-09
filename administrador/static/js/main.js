angular.module('eventos',['ngMd5'])
.config(function($locationProvider, $interpolateProvider) {
	$locationProvider.html5Mode(true).hashPrefix('!');
	$interpolateProvider.startSymbol('{[{');
	$interpolateProvider.endSymbol('}]}');

})
.controller('eventos_controller', function($scope, $http, md5){

	$http.get('/eventos/').
	success(function(data, status, headers, config) {
		$scope.data = data;
		$scope.categorias = _(data).chain().uniq('depto').value();
	}).
	error(function(data, status, headers, config) {

	});
	$scope.dep = '';
	$scope.filtroDep = function(dep){
		if (dep) {
			$scope.dep = dep.depto;	
		}else{
			$scope.dep = '';
		};
		
	}

	$scope.email = function  (email) {
		return md5.createHash(email);
	}



});