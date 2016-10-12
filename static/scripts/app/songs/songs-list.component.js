angular.
module('songsList').
component('songsList', {
    template: `
		<h3>Listados de Canciones disponibles</h3>
		<song-detail data="song" ng-repeat="song in $ctrl.songs"></song-detail>
    `,
    controller: ['$routeParams', '$http', function songListController($routeParams, $http) {
    		var self = this;
            self.phoneId = "Some One";
            self.songs = [];
            var urls = {
            	'all': "/api/songs/"
            };

            $http.get(urls.all).success(function(json){
            	self.songs = json;
            })
        }
    ]
});
