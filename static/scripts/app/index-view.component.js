angular.module('MyMusic').component("indexView", {
    template: `
		<a href="#!/register" class="btn btn-primary btn-lg">Registro</a>
        <a href="#!/login" class="btn btn-primary btn-lg">Ingresar</a>
        <br />
        <br />
         <playlist-detail data="playlist" ng-repeat="playlist in $ctrl.playlists"></playlist-detail>
    `,
    controller: ['Consumer', 'Config', function(Consumer, Config) {
        var self = this;

        Consumer.get_public_playlists().then(function(resp){
                self.playlists = resp.data;
            });
    }]
});
