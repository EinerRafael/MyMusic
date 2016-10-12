(function() {
    window.MyMusic = angular.module("MyMusic", ['ngRoute', 'songsList', 'Access', 'Home']);

    window.MyMusic.config(['$locationProvider', '$routeProvider', '$httpProvider',
        function config($locationProvider, $routeProvider, $httpProvider) {

            $httpProvider.defaults.headers.common['Accept'] = 'application/json';
            delete $httpProvider.defaults.headers.common['X-Requested-With'];

            $locationProvider.hashPrefix('!');

            $routeProvider.
            when('/index', {
                template: `
                    <a href="#!/register" class="btn btn-primary btn-lg">Registro</a>
                    <a href="#!/login" class="btn btn-primary btn-lg">Ingresar</a>
                `
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
            }).
            otherwise('/index');
        }
    ]);
})();
