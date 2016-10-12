angular.module('Home').component("playlistView", {
    template: `
		<h3>Listado de PlayLists</h3>
        <h4>{{$ctrl.user.fullName()}}</h4>
        <span>{{$ctrl.user.email}}</span>
        <br />
        <a href="#!/home/" class="btn btn-default">Volver</a>
        <a href="#!/home/playlist/register" class="btn btn-danger">Agregar</a>
        <br />
        <br />
        <playlist-detail data="playlist" ng-repeat="playlist in $ctrl.playlists"></playlist-detail>        
    `,
    controller: ['Consumer', 'Storage', '$location', 'Config', function(Consumer, Storage, $location, Config) {
        var self = this;
        self.playlists = [];

        function initialize() {
            if (!Storage.hasSession()) {
                $location.path("/index");
            }
            self.session = Storage.getSession();
            self.user = self.session.user;
            self.user.fullName = function() {
                return this.first_name + " " + this.last_name;
            }

            Consumer.get_playlist_users(self.user.id, Storage.getToken()).then(function(resp){
                self.playlists = resp.data;
            });
        }

        initialize();
    }]
});
