angular
	.module(
		'soberana',
		[
			'eventos',
			'publicaciones'
		]
	)
	.config(['$interpolateProvider', function ($interpolateProvider) {
		$interpolateProvider.startSymbol('{[{');
		$interpolateProvider.endSymbol('}]}');
	}]);