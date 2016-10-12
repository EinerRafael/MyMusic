angular.module('Home').component("songsView", {
    template: `
		<h3>Listado de Canciones</h3>
        <h4>{{$ctrl.user.fullName()}}</h4>
        <span>{{$ctrl.user.email}}</span>
        <br />
        <a href="#!/home/" class="btn btn-default">Volver</a>
        <a href="#!/home/songs/register" class="btn btn-danger">Agregar</a>
        <br />
        <br />
        <song-detail data="song" ng-repeat="song in $ctrl.songs"></song-detail>        
    `,
    controller: ['Consumer', 'Storage', '$location', 'Config', function(Consumer, Storage, $location, Config) {
        var self = this;
        self.songs = [];

        function initialize() {
            if (!Storage.hasSession()) {
                $location.path("/index");
            }
            self.session = Storage.getSession();
            self.user = self.session.user;
            self.user.fullName = function() {
                return this.first_name + " " + this.last_name;
            }

            Consumer.songs(Storage.getToken()).then(function(resp){
                self.songs = resp.data;
            });
        }

        initialize();
    }]
});
