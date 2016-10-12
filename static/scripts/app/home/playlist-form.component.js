angular.module('Home').component("playlistForm", {
    template: `
        <h3>Nueva PlayList</h3>
        <h4>{{$ctrl.user.fullName()}}</h4>
        <span>{{$ctrl.user.email}}</span>
        <form class="form-horizontal col-md-6" ng-submit="$ctrl.register()">
          <fieldset>
            <div class="form-group">
              <label for="inputEmail" class="col-lg-2 control-label">Nombre</label>
              <div class="col-lg-10">
                <input class="form-control" id="inputEmail" placeholder="Nombre" type="text" required ng-model="$ctrl.name">
              </div>
            </div>
            <div class="form-group">
              <label for="inputEmail" class="col-lg-2 control-label">Genero</label>
              <div class="col-lg-10">
                <input class="form-control" id="inputEmail" placeholder="Artista" type="text" required ng-model="$ctrl.gender">
              </div>
            </div>
            <div class="form-group">
              <label for="inputEmail" class="col-lg-2 control-label">Descripción</label>
              <div class="col-lg-10">
                <input class="form-control" id="inputEmail" placeholder="Album" type="text" required ng-model="$ctrl.description">
                <div class="checkbox">
                <label>
                  <input ng-model="$ctrl.is_public" type="checkbox"> Es Pública
                </label>
              </div>
              </div>
            </div>
            <div class="form-group">
              <div class="col-lg-10 col-lg-offset-2">
                <a href="#!/home/songs/" class="btn btn-default">Volver</a>
                <button type="submit" class="btn btn-primary">Agregar</button>
              </div>
            </div>
           </fieldset>
        </form>
        <br />
        <div class="alert alert-dismissible alert-danger" ng-repeat='error in $ctrl.errors'>
          <button type="button" class="close" data-dismiss="alert">&times;</button>
         <strong>{{error.message}}</strong>
         <span>{{error.description}}</span>
        </div>    
    `,
    controller: ['Consumer', 'Storage', '$location', 'Config', function(Consumer, Storage, $location, Config) {
        var self = this;
        self.name = "";
        self.gender = "";
        self.description = "";
        self.is_public = true;

        function initialize() {
            if (!Storage.hasSession()) {
                $location.path("/index");
            }
            self.session = Storage.getSession();
            self.user = self.session.user;
            self.user.fullName = function() {
                return this.first_name + " " + this.last_name;
            }
        }

        self.register = function() {
            var objSend = {
                "user": self.user.id,
                "name": self.name,
                "gender": self.gender,
                "description": self.description,
                'is_public': self.is_public ? 1 : 0
            };
            Consumer.add_playlist(objSend, Storage.getToken()).then(function(resp) {
                $location.path("/home/playlists/");
            });
            return false;
        }

        initialize();
    }]
});
