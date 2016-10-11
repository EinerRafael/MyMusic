(function() {
    window.MyMusic = angular.module("MyMusic", ['ngRoute', 'songsList']);

    window.MyMusic.config(['$locationProvider', '$routeProvider',
        function config($locationProvider, $routeProvider) {
            $locationProvider.hashPrefix('!');

            $routeProvider.
            when('/home', {
                template: ''
            }).
            when('/songs/', {
                template: '<songs-list></songs-list>'
            }).
            otherwise('/phones');
        }
    ]);
})();
