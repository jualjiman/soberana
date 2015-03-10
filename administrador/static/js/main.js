angular.module('eventos',['ngMd5'])
.config(function($locationProvider, $interpolateProvider) {
	$locationProvider.html5Mode(true).hashPrefix('!');
	$interpolateProvider.startSymbol('{[{');
	$interpolateProvider.endSymbol('}]}');

})
.controller('eventos_controller', function($scope, $http, md5){

	$http.get('/eventos-json/').
	success(function(data, status, headers, config) {
		//$scope.data = data;
		console.log("probando..");
		console.log(data);
		//$scope.categorias = _(data).chain().uniq('depto').value();
	}).
	error(function(data, status, headers, config) {

	});

});