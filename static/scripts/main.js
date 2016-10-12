(function() {
    window.MyMusic = angular.module("MyMusic", ['ngRoute', 'songsList', 'Access', 'Home']);

    window.MyMusic.config(['$locationProvider', '$routeProvider', '$httpProvider',
        function config($locationProvider, $routeProvider, $httpProvider) {

            $httpProvider.defaults.headers.common['Accept'] = 'application/json';
            delete $httpProvider.defaults.headers.common['X-Requested-With'];

            $locationProvider.hashPrefix('!');

            $routeProvider.
            when('/index', {
                template: '<index-view></index-view>'
            }).
            when('/login', {
                template: '<login-form></login-form>'
            }).
            when('/register', {
                template: '<register-form></register-form>'
            }).
            when('/songs/', {
                template: '<songs-list></songs-list>'
            }).
            when('/home', {
                template: '<home-view></home-view>'
            })
            .when('/home/songs/', {
                template: '<songs-view></songs-view>'
            })
            .when('/home/songs/register', {
                template: '<song-form></song-form>'
            })
            .when('/home/playlists/', {
                template: '<playlist-view></playlist-view>'
            })
            .when('/home/playlist/register', {
                template: '<playlist-form></playlist-form>'
            })
            .otherwise('/index');
        }
    ]);
})();
